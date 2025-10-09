#!/usr/bin/env python3
"""
Conversation Normalization Script

Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09
Note: Copilot is powered by AI; mistakes are possible. Review carefully.

This script parses, normalizes, and exports conversation messages found in
markdown files or GitHub issues into JSONL/NDJSON format for further analysis.

Outputs:
- conversations.jsonl: Normalized conversation data in JSON Lines format
- metadata.json: Metadata about the extraction process

Usage:
    python scripts/normalize_conversations.py [--input-dir DIR] [--output-dir DIR]

Requirements:
    Python 3.7+
    Standard library only (no external dependencies)
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict


@dataclass
class Message:
    """Represents a single message in a conversation."""
    role: str  # 'user', 'assistant', 'system'
    content: str
    timestamp: Optional[str] = None
    metadata: Optional[Dict] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary, excluding None values."""
        result = asdict(self)
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class Conversation:
    """Represents a complete conversation."""
    conversation_id: str
    source_file: str
    messages: List[Message]
    extracted_at: str
    metadata: Optional[Dict] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary with messages as dicts."""
        return {
            'conversation_id': self.conversation_id,
            'source_file': self.source_file,
            'messages': [msg.to_dict() for msg in self.messages],
            'extracted_at': self.extracted_at,
            'metadata': self.metadata if self.metadata else {}
        }


class MarkdownConversationParser:
    """Parser for extracting conversations from markdown files."""
    
    # Common patterns for identifying roles in conversations
    USER_PATTERNS = [
        r'^#+\s*(?:user|human|question|q)(?:\s*:)?\s*$',
        r'^(?:user|human|question|q)\s*:',
        r'^\*\*(?:user|human|question|q)\*\*\s*:?',
    ]
    
    ASSISTANT_PATTERNS = [
        r'^#+\s*(?:assistant|ai|agent|copilot|answer|a)(?:\s*:)?\s*$',
        r'^(?:assistant|ai|agent|copilot|answer|a)\s*:',
        r'^\*\*(?:assistant|ai|agent|copilot|answer|a)\*\*\s*:?',
    ]
    
    SYSTEM_PATTERNS = [
        r'^#+\s*(?:system|note)(?:\s*:)?\s*$',
        r'^(?:system|note)\s*:',
    ]
    
    def __init__(self):
        self.user_regex = [re.compile(p, re.IGNORECASE) for p in self.USER_PATTERNS]
        self.assistant_regex = [re.compile(p, re.IGNORECASE) for p in self.ASSISTANT_PATTERNS]
        self.system_regex = [re.compile(p, re.IGNORECASE) for p in self.SYSTEM_PATTERNS]
    
    def detect_role(self, line: str) -> Optional[str]:
        """
        Detect if a line indicates a role change.
        
        Args:
            line: Line of text to analyze
            
        Returns:
            Role name ('user', 'assistant', 'system') or None
        """
        line = line.strip()
        
        for regex in self.user_regex:
            if regex.match(line):
                return 'user'
        
        for regex in self.assistant_regex:
            if regex.match(line):
                return 'assistant'
        
        for regex in self.system_regex:
            if regex.match(line):
                return 'system'
        
        return None
    
    def parse_markdown_file(self, filepath: Path) -> Optional[Conversation]:
        """
        Parse a markdown file and extract conversation.
        
        Args:
            filepath: Path to markdown file
            
        Returns:
            Conversation object or None if no valid conversation found
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except (IOError, OSError) as e:
            print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
            return None
        
        lines = content.split('\n')
        messages = []
        current_role = None
        current_content = []
        
        for line in lines:
            detected_role = self.detect_role(line)
            
            if detected_role:
                # Save previous message if exists
                if current_role and current_content:
                    content_text = '\n'.join(current_content).strip()
                    if content_text:
                        messages.append(Message(
                            role=current_role,
                            content=content_text
                        ))
                
                # Start new message
                current_role = detected_role
                current_content = []
                
                # Check if content starts on same line after role marker
                role_line_cleaned = re.sub(r'^#+\s*(?:\*\*)?\w+(?:\*\*)?\s*:?\s*', '', line, flags=re.IGNORECASE).strip()
                if role_line_cleaned:
                    current_content.append(role_line_cleaned)
            else:
                # Accumulate content for current role
                if current_role is not None:
                    current_content.append(line)
        
        # Save final message
        if current_role and current_content:
            content_text = '\n'.join(current_content).strip()
            if content_text:
                messages.append(Message(
                    role=current_role,
                    content=content_text
                ))
        
        # Only return conversation if we found at least one message
        if messages:
            conversation_id = filepath.stem
            return Conversation(
                conversation_id=conversation_id,
                source_file=str(filepath),
                messages=messages,
                extracted_at=datetime.now().isoformat(),
                metadata={
                    'file_size': filepath.stat().st_size,
                    'message_count': len(messages)
                }
            )
        
        return None
    
    def extract_simple_qa(self, filepath: Path) -> Optional[Conversation]:
        """
        Extract simple question-answer pairs from documents.
        
        This is a fallback method for documents that don't follow
        strict conversation format but contain Q&A content.
        
        Args:
            filepath: Path to markdown file
            
        Returns:
            Conversation object or None
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except (IOError, OSError) as e:
            return None
        
        # Look for Q: / A: patterns
        qa_pattern = re.compile(r'^(?:q(?:uestion)?)\s*[:.]?\s*(.+?)(?=^a(?:nswer)?[:.]|\Z)', 
                               re.MULTILINE | re.IGNORECASE | re.DOTALL)
        answer_pattern = re.compile(r'^a(?:nswer)?\s*[:.]?\s*(.+?)(?=^q(?:uestion)?[:.]|\Z)', 
                                   re.MULTILINE | re.IGNORECASE | re.DOTALL)
        
        messages = []
        
        # Simple extraction - not perfect but handles basic cases
        sections = re.split(r'\n(?=(?:q(?:uestion)?|a(?:nswer)?)\s*[:.])', content, flags=re.IGNORECASE)
        
        for section in sections:
            section = section.strip()
            if re.match(r'^q(?:uestion)?\s*[:.]', section, re.IGNORECASE):
                content_text = re.sub(r'^q(?:uestion)?\s*[:.]?\s*', '', section, flags=re.IGNORECASE).strip()
                if content_text:
                    messages.append(Message(role='user', content=content_text))
            elif re.match(r'^a(?:nswer)?\s*[:.]', section, re.IGNORECASE):
                content_text = re.sub(r'^a(?:nswer)?\s*[:.]?\s*', '', section, flags=re.IGNORECASE).strip()
                if content_text:
                    messages.append(Message(role='assistant', content=content_text))
        
        if messages:
            return Conversation(
                conversation_id=f"{filepath.stem}_qa",
                source_file=str(filepath),
                messages=messages,
                extracted_at=datetime.now().isoformat(),
                metadata={'extraction_method': 'simple_qa'}
            )
        
        return None


def process_directory(input_dir: Path, parser: MarkdownConversationParser) -> List[Conversation]:
    """
    Process all markdown files in a directory.
    
    Args:
        input_dir: Directory to scan for markdown files
        parser: Parser instance to use
        
    Returns:
        List of extracted conversations
    """
    conversations = []
    markdown_files = list(input_dir.rglob('*.md'))
    
    print(f"Found {len(markdown_files)} markdown files in {input_dir}")
    
    for filepath in markdown_files:
        print(f"Processing: {filepath.name}...", end=' ')
        
        # Try structured conversation parsing first
        conversation = parser.parse_markdown_file(filepath)
        
        # Fallback to simple Q&A extraction if no structured conversation found
        if not conversation:
            conversation = parser.extract_simple_qa(filepath)
        
        if conversation:
            conversations.append(conversation)
            print(f"✓ Extracted {len(conversation.messages)} messages")
        else:
            print("✗ No conversation found")
    
    print(f"\nTotal conversations extracted: {len(conversations)}")
    return conversations


def write_jsonl(conversations: List[Conversation], output_path: Path):
    """
    Write conversations to JSONL file.
    
    Args:
        conversations: List of Conversation objects
        output_path: Path to output JSONL file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for conv in conversations:
            json_line = json.dumps(conv.to_dict(), ensure_ascii=False)
            f.write(json_line + '\n')
    
    print(f"Conversations written to: {output_path}")


def write_metadata(conversations: List[Conversation], output_path: Path):
    """
    Write metadata about the extraction process.
    
    Args:
        conversations: List of Conversation objects
        output_path: Path to output metadata JSON file
    """
    total_messages = sum(len(conv.messages) for conv in conversations)
    role_counts = {'user': 0, 'assistant': 0, 'system': 0}
    
    for conv in conversations:
        for msg in conv.messages:
            role_counts[msg.role] = role_counts.get(msg.role, 0) + 1
    
    metadata = {
        'extraction_timestamp': datetime.now().isoformat(),
        'total_conversations': len(conversations),
        'total_messages': total_messages,
        'role_distribution': role_counts,
        'source_files': [conv.source_file for conv in conversations]
    }
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"Metadata written to: {output_path}")


def main():
    """Main execution function."""
    parser_cli = argparse.ArgumentParser(
        description='Normalize conversations from markdown files to JSONL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process default directory (99-REGISTROS-HISTORICOS/)
  python scripts/normalize_conversations.py
  
  # Process custom directory
  python scripts/normalize_conversations.py --input-dir conversations/
  
  # Custom output directory
  python scripts/normalize_conversations.py --output-dir outputs/conversations/
        """
    )
    
    parser_cli.add_argument(
        '--input-dir',
        type=str,
        default='99-REGISTROS-HISTORICOS',
        help='Input directory containing markdown files (default: 99-REGISTROS-HISTORICOS/)'
    )
    
    parser_cli.add_argument(
        '--output-dir',
        type=str,
        default='artifacts',
        help='Output directory for JSONL files (default: artifacts/)'
    )
    
    args = parser_cli.parse_args()
    
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    
    if not input_dir.exists():
        print(f"Error: Input directory does not exist: {input_dir}", file=sys.stderr)
        sys.exit(1)
    
    print("=" * 70)
    print("Conversation Normalization")
    print("=" * 70)
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 70)
    print()
    
    # Initialize parser and process files
    parser = MarkdownConversationParser()
    conversations = process_directory(input_dir, parser)
    
    if not conversations:
        print("\nNo conversations found. Exiting.")
        sys.exit(0)
    
    # Write outputs
    write_jsonl(conversations, output_dir / 'conversations.jsonl')
    write_metadata(conversations, output_dir / 'conversations_metadata.json')
    
    print("\n" + "=" * 70)
    print("Normalization complete!")
    print("=" * 70)


if __name__ == '__main__':
    main()
