# PROTOCOLOS DE OPERAÇÃO / OPERATION PROTOCOLS

## Visão Geral / Overview

Este documento estabelece protocolos e diretrizes para operações futuras neste repositório, especialmente para agentes de IA e assistentes automatizados.

This document establishes protocols and guidelines for future operations in this repository, especially for AI agents and automated assistants.

---

## 1. PRINCÍPIOS FUNDAMENTAIS / CORE PRINCIPLES

### 1.1 Transparência / Transparency
- Todas as conversas e decisões devem ser documentadas
- Mudanças significativas devem ser registradas no CHANGELOG.md
- Processo de tomada de decisão deve ser rastreável

### 1.2 Imutabilidade de Registros Históricos / Immutability of Historical Records
- Conversas originais em `00-FUNDAMENTOS/conversas/` NUNCA devem ser modificadas
- Mantém integridade histórica e auditoria
- Exceção: Apenas para correções críticas com documentação explícita

### 1.3 Versionamento Semântico / Semantic Versioning
- MAJOR (x.0.0): Mudanças incompatíveis na estrutura
- MINOR (0.x.0): Novas funcionalidades compatíveis
- PATCH (0.0.x): Correções de bugs

---

## 2. PROTOCOLOS PARA AGENTES DE IA / AI AGENT PROTOCOLS

### 2.1 Fluxo de Trabalho Padrão / Standard Workflow

```
1. LER / READ: .ai-guide.json de cada pasta relevante
2. ENTENDER / UNDERSTAND: Contexto e propósito através de OVERVIEW.md
3. PLANEJAR / PLAN: Documentar plano em issue ou PR description
4. EXECUTAR / EXECUTE: Fazer mudanças incrementais
5. VALIDAR / VALIDATE: Verificar consistência e links
6. DOCUMENTAR / DOCUMENT: Atualizar CHANGELOG.md e READMEs
7. REPORTAR / REPORT: Commit com mensagens descritivas
```

### 2.2 Antes de Fazer Mudanças / Before Making Changes

**SEMPRE / ALWAYS:**
1. Ler toda a documentação relevante
2. Verificar se há duplicatas ou conflitos
3. Entender dependências entre arquivos
4. Planejar mudanças minimamente invasivas
5. Criar backup se necessário

**NUNCA / NEVER:**
1. Deletar arquivos sem verificar referências
2. Modificar conversas históricas originais
3. Fazer mudanças massivas sem plano documentado
4. Ignorar .ai-guide.json dos diretórios
5. Commitar sem mensagens descritivas

### 2.3 Técnicas Validadas de Copilot / Validated Copilot Techniques

**Técnicas Usadas Neste Projeto:**

1. **Análise Profunda de Contexto**
   - Leitura completa de conversas de 11.000+ linhas
   - Extração de insights e padrões
   - Identificação de objetivos originais

2. **Reorganização Estrutural**
   - Renomeação lógica de pastas (99 → 00)
   - Criação de hierarquia consistente
   - Remoção de duplicatas

3. **Documentação Multilíngue**
   - OVERVIEW.md em inglês
   - README.md em português
   - .ai-guide.json para máquinas

4. **Geração de Conteúdo Técnico**
   - Documentos detalhados (11-19KB)
   - Tabelas comparativas
   - Exemplos práticos de código
   - Cálculos econômicos

5. **Validação Cruzada**
   - Checagem de dados entre conversas e documentos
   - Verificação de valores (créditos cloud, preços)
   - Confirmação de links e referências

6. **Metadados Estruturados**
   - JSON para configuração e orientação
   - YAML para dados tabulares
   - Markdown para documentação narrativa

---

## 3. ORGANIZAÇÃO DE ARQUIVOS / FILE ORGANIZATION

### 3.1 Nomenclatura / Naming Conventions

**Pastas / Folders:**
```
00-PREFIX-nome/     # Numeração + descrição em kebab-case
```

**Arquivos / Files:**
```
UPPER-CASE-KEBAB.md     # Documentação em maiúsculas
lowercase-kebab.json     # Configs em minúsculas
.ai-guide.json          # Arquivos hidden para IA
```

### 3.2 Estrutura de Pastas / Folder Structure

```
00-FUNDAMENTOS/          # Base histórica e conversas
01-VISAO-GERAL/          # Visões gerais e sumários
02-GITHUB-EDUCATION/     # GitHub Education Pack específico
03-GITHUB-SKILLS/        # Habilidades técnicas GitHub/Copilot
04-TECH-PROFUNDO/        # Conteúdo técnico detalhado
```

### 3.3 Arquivos Obrigatórios por Pasta / Required Files per Folder

Cada pasta numerada DEVE conter:
- `README.md` - Descrição em português
- `OVERVIEW.md` - Overview em inglês
- `.ai-guide.json` - Guia para agentes de IA

---

## 4. EXTRAÇÃO DE DADOS / DATA EXTRACTION

### 4.1 De Conversas para Dados Estruturados / From Conversations to Structured Data

**Processo:**
1. Identificar tópicos e subtópicos
2. Extrair menções a ferramentas com URLs
3. Categorizar por tipo (cloud, IA, dev tools, etc)
4. Validar valores econômicos
5. Estruturar em JSON/YAML
6. Documentar fonte e data de extração

**Formato de Saída / Output Format:**
```json
{
  "tool_name": {
    "category": "cloud_computing",
    "provider": "Microsoft",
    "free_tier": "$100 credits",
    "target": "students",
    "url": "https://...",
    "source": "conversation_1",
    "verified": true,
    "extracted_date": "2025-01-08"
  }
}
```

### 4.2 Validação de Dados / Data Validation

**Checklist:**
- [ ] URLs válidas e acessíveis
- [ ] Valores monetários em BRL e USD
- [ ] Datas em formato ISO (YYYY-MM-DD)
- [ ] Categorias consistentes
- [ ] Referências cruzadas corretas
- [ ] Nenhuma informação sensível

---

## 5. DOCUMENTAÇÃO TÉCNICA / TECHNICAL DOCUMENTATION

### 5.1 Estrutura de Documento Técnico / Technical Document Structure

```markdown
# TÍTULO

## 🎯 Visão Geral (Overview)
- Propósito
- Público-alvo
- Valor econômico

## 📋 Índice (Table of Contents)

## 🚀 [Seções Principais]

## 💰 Economia (Economics)

## 📚 Recursos (Resources)

## ⚡ Quick Start

## 🔗 Links

## 📝 Última Atualização (Last Updated)
```

### 5.2 Qualidade de Conteúdo / Content Quality

**Padrões:**
- Mínimo 5KB de conteúdo substantivo
- Exemplos práticos com código
- Tabelas comparativas quando aplicável
- Links verificados
- Cálculos justificados
- Fontes citadas

---

## 6. CONTROLE DE QUALIDADE / QUALITY CONTROL

### 6.1 Checklist Pré-Commit / Pre-Commit Checklist

- [ ] Todos os links funcionando
- [ ] Nenhum arquivo duplicado
- [ ] Nomenclatura consistente
- [ ] .gitignore atualizado
- [ ] CHANGELOG.md atualizado
- [ ] Sem informações sensíveis
- [ ] Markdown validado (sem erros de sintaxe)
- [ ] Referências cruzadas corretas

### 6.2 Revisão Regular / Regular Review

**Mensalmente:**
- Verificar links quebrados
- Atualizar valores e preços
- Revisar disponibilidade de programas
- Adicionar novos recursos identificados

**Anualmente:**
- Auditoria completa de conteúdo
- Remoção de programas descontinuados
- Atualização de cálculos econômicos
- Versão MAJOR se necessário

---

## 7. CONTRIBUIÇÕES EXTERNAS / EXTERNAL CONTRIBUTIONS

### 7.1 Processo de Contribuição / Contribution Process

1. Abrir issue descrevendo proposta
2. Esperar aprovação do maintainer
3. Fork do repositório
4. Criar branch descritiva
5. Fazer mudanças seguindo protocolos
6. Testes e validação local
7. Pull Request com descrição detalhada
8. Code review
9. Merge após aprovação

### 7.2 Padrões de Commit / Commit Standards

```
feat: Nova funcionalidade
fix: Correção de bug
docs: Mudanças em documentação
style: Formatação, sem mudança de código
refactor: Refatoração de código
test: Adição de testes
chore: Manutenção geral
```

---

## 8. SEGURANÇA E PRIVACIDADE / SECURITY AND PRIVACY

### 8.1 Informações Proibidas / Prohibited Information

**NUNCA commitar / NEVER commit:**
- Senhas ou tokens
- Chaves de API
- Informações pessoais identificáveis
- Dados proprietários de terceiros
- Credenciais de qualquer tipo

### 8.2 Licenciamento / Licensing

- Todo conteúdo deve respeitar licenças originais
- Citar fontes apropriadamente
- Usar apenas dados públicos
- Respeitar propriedade intelectual

---

## 9. TROUBLESHOOTING

### 9.1 Problemas Comuns / Common Issues

**Links Quebrados:**
```bash
# Verificar todos os links
find . -name "*.md" -exec grep -H "http" {} \; | sort
```

**Arquivos Duplicados:**
```bash
# Encontrar duplicatas
find . -type f -name "*.md" | sed 's|.*/||' | sort | uniq -d
```

**Inconsistências:**
```bash
# Verificar estrutura de pastas
tree -L 2 -d
```

---

## 10. CONTATO E SUPORTE / CONTACT AND SUPPORT

Para questões sobre estes protocolos:
1. Abrir issue no repositório
2. Marcar com label `question` ou `protocol`
3. Aguardar resposta do maintainer

---

## Última Atualização / Last Updated
2025-01-08

## Versão / Version
1.0.0

## Mantido por / Maintained by
Genovese-Felipe
