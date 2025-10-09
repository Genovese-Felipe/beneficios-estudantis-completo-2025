# Dados Extraídos / Extracted Data

## Propósito / Purpose

Esta subpasta contém dados limpos e estruturados extraídos das conversas originais, organizados em formatos legíveis por máquina (JSON, YAML) e por humanos (Markdown).

This subfolder contains clean, structured data extracted from original conversations, organized in machine-readable (JSON, YAML) and human-readable (Markdown) formats.

## Conteúdo / Contents

### topics-summary.json
Resumo estruturado de todos os tópicos discutidos nas conversas originais, com hierarquia e relacionamentos.

### tools-catalog.json
Catálogo completo de ferramentas mencionadas com:
- Nome e provedor
- Categoria
- Valor econômico (free tier, créditos, descontos)
- URL oficial
- Requisitos de elegibilidade
- Data de verificação

### economic-calculations.json
Detalhamento de todos os cálculos econômicos:
- Valores individuais por ferramenta
- Agregações por categoria
- Conversões de moeda (USD ↔ BRL)
- Metodologia de cálculo
- Fontes de dados

### conversation-insights.md
Insights chave extraídos das conversas:
- Decisões importantes tomadas
- Mudanças de direção identificadas
- Lições aprendidas
- Recomendações futuras

## Formato dos Dados / Data Format

### JSON Structure Example
```json
{
  "tool_name": {
    "provider": "Company Name",
    "category": "cloud_computing",
    "free_tier": {
      "amount": 100,
      "currency": "USD",
      "type": "credits"
    },
    "eligibility": "verified_students",
    "url": "https://...",
    "verified": true,
    "verified_date": "2025-01-08",
    "source": "conversation_1_line_2450"
  }
}
```

## Uso / Usage

### Para Análise Avançada / For Advanced Analysis
- Carregar JSONs em Python/JavaScript para processamento
- Executar análises estatísticas
- Gerar visualizações
- Treinar modelos de ML

### Para Validação / For Validation
- Verificar consistência entre conversas e documentação
- Auditar cálculos econômicos
- Confirmar URLs e valores
- Rastrear mudanças ao longo do tempo

### Para Futuros Assistentes de IA / For Future AI Assistants
- Acesso rápido a dados estruturados
- Evitar re-parsing de conversas longas
- Dados validados e verificados
- Formato padronizado para consultas

## Manutenção / Maintenance

### Quando Atualizar / When to Update
- Novos programas/ferramentas descobertos
- Valores ou preços alterados
- URLs quebradas ou redirecionadas
- Mudanças em requisitos de elegibilidade
- Novas conversas adicionadas

### Como Atualizar / How to Update
1. Verificar fonte original (conversas ou documentação oficial)
2. Atualizar JSON/YAML correspondente
3. Adicionar nota de atualização com data
4. Incrementar versão se mudanças significativas
5. Documentar mudanças em CHANGELOG.md

## Versionamento / Versioning

Dados seguem semantic versioning:
- **MAJOR**: Mudanças incompatíveis na estrutura
- **MINOR**: Novos dados adicionados
- **PATCH**: Correções de valores existentes

Versão atual / Current version: **1.0.0**

## Última Atualização / Last Updated
2025-01-08
