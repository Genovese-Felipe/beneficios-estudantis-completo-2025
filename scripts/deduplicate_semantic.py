#!/usr/bin/env python3
"""
Semantic Duplicate Detection Script

Generated with assistance from GitHub Copilot (AI assistant) on 2025-10-09
Note: Copilot is powered by AI; mistakes are possible. Review carefully.

This script computes embeddings using sentence-transformers and finds
near-duplicate documents based on semantic similarity.

Outputs:
- semantic_duplicates.csv: Detected semantically similar documents
- embeddings.npy: Cached document embeddings (optional)

Usage:
    python scripts/deduplicate_semantic.py [--input INPUT] [--threshold THRESHOLD]

Requirements:
    Python 3.7+
    sentence-transformers>=2.2.0
    numpy>=1.20.0
    scipy>=1.7.0
    Optional: faiss-cpu or hnswlib for faster search

Installation:
    pip install sentence-transformers numpy scipy
    
    # Optional: For faster nearest neighbor search
    pip install faiss-cpu
    # or
    pip install hnswlib
"""

import os
import sys
import csv
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# Check for required dependencies
try:
    import numpy as np
except ImportError:
    print("Error: numpy is required. Install with: pip install numpy", file=sys.stderr)
    sys.exit(1)

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Error: sentence-transformers is required.", file=sys.stderr)
    print("Install with: pip install sentence-transformers", file=sys.stderr)
    sys.exit(1)

try:
    from scipy.spatial.distance import cosine
except ImportError:
    print("Error: scipy is required. Install with: pip install scipy", file=sys.stderr)
    sys.exit(1)

# Optional dependencies
try:
    import faiss
    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False

try:
    import hnswlib
    HNSWLIB_AVAILABLE = True
except ImportError:
    HNSWLIB_AVAILABLE = False


def load_documents(input_path: Path) -> List[Dict]:
    """
    Load documents from CSV file or directory.
    
    Args:
        input_path: Path to CSV file (repo_index.csv) or directory with markdown files
        
    Returns:
        List of document dictionaries with 'path' and 'content' keys
    """
    documents = []
    
    if input_path.is_file() and input_path.suffix == '.csv':
        # Load from CSV (assumes repo_index.csv format)
        print(f"Loading documents from CSV: {input_path}")
        with open(input_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                doc_path = Path(row['path'])
                if doc_path.suffix in ['.md', '.txt', '.rst']:
                    try:
                        with open(row['absolute_path'], 'r', encoding='utf-8') as doc_file:
                            content = doc_file.read()
                            if content.strip():
                                documents.append({
                                    'path': row['path'],
                                    'content': content,
                                    'size': int(row['size_bytes'])
                                })
                    except (IOError, OSError, UnicodeDecodeError) as e:
                        print(f"Warning: Could not read {row['path']}: {e}", file=sys.stderr)
    
    elif input_path.is_dir():
        # Load markdown files from directory
        print(f"Loading documents from directory: {input_path}")
        for md_file in input_path.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.strip():
                        documents.append({
                            'path': str(md_file.relative_to(input_path)),
                            'content': content,
                            'size': md_file.stat().st_size
                        })
            except (IOError, OSError, UnicodeDecodeError) as e:
                print(f"Warning: Could not read {md_file}: {e}", file=sys.stderr)
    
    else:
        print(f"Error: Invalid input path: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Loaded {len(documents)} documents")
    return documents


def compute_embeddings(documents: List[Dict], model_name: str = 'all-MiniLM-L6-v2') -> np.ndarray:
    """
    Compute embeddings for documents using sentence-transformers.
    
    Args:
        documents: List of document dictionaries with 'content' key
        model_name: Name of the sentence-transformers model to use
        
    Returns:
        NumPy array of embeddings, shape (n_documents, embedding_dim)
    """
    print(f"Loading model: {model_name}")
    model = SentenceTransformer(model_name)
    
    print(f"Computing embeddings for {len(documents)} documents...")
    # Extract content and limit length to avoid memory issues
    texts = [doc['content'][:10000] for doc in documents]  # Limit to 10k chars
    
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=32,
        convert_to_numpy=True
    )
    
    print(f"Embeddings computed: shape {embeddings.shape}")
    return embeddings


def find_similar_pairs_bruteforce(embeddings: np.ndarray, 
                                  documents: List[Dict],
                                  threshold: float = 0.85) -> List[Tuple[int, int, float]]:
    """
    Find similar document pairs using brute-force comparison.
    
    Args:
        embeddings: Document embeddings array
        documents: Original documents list
        threshold: Similarity threshold (0-1, higher = more similar)
        
    Returns:
        List of (doc1_idx, doc2_idx, similarity) tuples
    """
    print(f"Finding similar pairs (threshold={threshold})...")
    similar_pairs = []
    n_docs = len(embeddings)
    
    for i in range(n_docs):
        for j in range(i + 1, n_docs):
            # Compute cosine similarity
            similarity = 1 - cosine(embeddings[i], embeddings[j])
            
            if similarity >= threshold:
                similar_pairs.append((i, j, similarity))
        
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1}/{n_docs} documents...", end='\r')
    
    print(f"\nFound {len(similar_pairs)} similar pairs")
    return similar_pairs


def find_similar_pairs_faiss(embeddings: np.ndarray,
                             documents: List[Dict],
                             threshold: float = 0.85,
                             k: int = 10) -> List[Tuple[int, int, float]]:
    """
    Find similar document pairs using FAISS for faster search.
    
    Args:
        embeddings: Document embeddings array
        documents: Original documents list
        threshold: Similarity threshold (0-1, higher = more similar)
        k: Number of nearest neighbors to search
        
    Returns:
        List of (doc1_idx, doc2_idx, similarity) tuples
    """
    print(f"Building FAISS index for {len(embeddings)} documents...")
    
    # Normalize embeddings for cosine similarity
    faiss.normalize_L2(embeddings)
    
    # Build index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner product = cosine similarity after normalization
    index.add(embeddings.astype('float32'))
    
    print(f"Searching for similar pairs (threshold={threshold})...")
    similar_pairs = []
    
    # Search k nearest neighbors for each document
    distances, indices = index.search(embeddings.astype('float32'), k + 1)
    
    seen_pairs = set()
    for i, (dists, idxs) in enumerate(zip(distances, indices)):
        for dist, idx in zip(dists, idxs):
            if idx == i:  # Skip self
                continue
            
            similarity = float(dist)
            if similarity >= threshold:
                # Ensure we don't add duplicate pairs
                pair_key = tuple(sorted([i, idx]))
                if pair_key not in seen_pairs:
                    similar_pairs.append((i, idx, similarity))
                    seen_pairs.add(pair_key)
    
    print(f"Found {len(similar_pairs)} similar pairs")
    return similar_pairs


def write_duplicates_report(similar_pairs: List[Tuple[int, int, float]],
                           documents: List[Dict],
                           output_path: Path):
    """
    Write semantic duplicates report to CSV.
    
    Args:
        similar_pairs: List of (doc1_idx, doc2_idx, similarity) tuples
        documents: Original documents list
        output_path: Path to output CSV file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['document1', 'document2', 'similarity', 'size1', 'size2', 'recommendation'])
        
        for idx1, idx2, similarity in sorted(similar_pairs, key=lambda x: x[2], reverse=True):
            doc1 = documents[idx1]
            doc2 = documents[idx2]
            
            # Provide recommendation
            if similarity > 0.95:
                recommendation = "Very likely duplicate - review for merge/delete"
            elif similarity > 0.90:
                recommendation = "Likely duplicate - review content carefully"
            elif similarity > 0.85:
                recommendation = "Possibly similar - review for consolidation"
            else:
                recommendation = "Similar content - consider review"
            
            writer.writerow([
                doc1['path'],
                doc2['path'],
                f"{similarity:.4f}",
                doc1['size'],
                doc2['size'],
                recommendation
            ])
    
    print(f"Semantic duplicates report written to: {output_path}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Detect semantic duplicates using embeddings',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process from repo_index.csv
  python scripts/deduplicate_semantic.py --input artifacts/repo_index.csv
  
  # Process from directory
  python scripts/deduplicate_semantic.py --input . --threshold 0.90
  
  # Use specific model
  python scripts/deduplicate_semantic.py --input . --model all-mpnet-base-v2

Note:
  This script requires additional dependencies:
    pip install sentence-transformers numpy scipy
  
  For faster processing with large repositories:
    pip install faiss-cpu
        """
    )
    
    parser.add_argument(
        '--input',
        type=str,
        default='artifacts/repo_index.csv',
        help='Input CSV file or directory (default: artifacts/repo_index.csv)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='artifacts',
        help='Output directory (default: artifacts/)'
    )
    
    parser.add_argument(
        '--threshold',
        type=float,
        default=0.85,
        help='Similarity threshold 0-1 (default: 0.85)'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='all-MiniLM-L6-v2',
        help='Sentence-transformers model name (default: all-MiniLM-L6-v2)'
    )
    
    parser.add_argument(
        '--use-faiss',
        action='store_true',
        help='Use FAISS for faster search (requires faiss-cpu)'
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    
    if not input_path.exists():
        print(f"Error: Input path does not exist: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    if args.use_faiss and not FAISS_AVAILABLE:
        print("Warning: FAISS not available, falling back to brute-force search")
        print("Install FAISS with: pip install faiss-cpu")
        args.use_faiss = False
    
    print("=" * 70)
    print("Semantic Duplicate Detection")
    print("=" * 70)
    print(f"Input: {input_path}")
    print(f"Output directory: {output_dir}")
    print(f"Similarity threshold: {args.threshold}")
    print(f"Model: {args.model}")
    print(f"Using FAISS: {args.use_faiss}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 70)
    print()
    
    # Load documents
    documents = load_documents(input_path)
    
    if len(documents) < 2:
        print("Error: Need at least 2 documents to compare")
        sys.exit(1)
    
    # Compute embeddings
    embeddings = compute_embeddings(documents, args.model)
    
    # Find similar pairs
    if args.use_faiss:
        similar_pairs = find_similar_pairs_faiss(embeddings, documents, args.threshold)
    else:
        similar_pairs = find_similar_pairs_bruteforce(embeddings, documents, args.threshold)
    
    # Write report
    write_duplicates_report(similar_pairs, documents, output_dir / 'semantic_duplicates.csv')
    
    print("\n" + "=" * 70)
    print("Semantic deduplication complete!")
    print("=" * 70)


if __name__ == '__main__':
    main()
