# MCPs (Model Context Protocol) e APIs para Estudantes

## 📋 Índice
1. [O que é MCP](#o-que-é-mcp)
2. [GitHub Copilot e MCPs](#github-copilot-e-mcps)
3. [Servidores MCP Populares](#servidores-mcp-populares)
4. [APIs com Créditos para Estudantes](#apis-com-créditos-para-estudantes)
5. [Configuração Prática](#configuração-prática)
6. [Casos de Uso](#casos-de-uso)

## 🎯 O que é MCP

O **Model Context Protocol (MCP)** é um protocolo aberto desenvolvido pela Anthropic que permite que aplicações de IA (Claude, GitHub Copilot, etc.) se conectem a diferentes fontes de dados e ferramentas de forma padronizada.

### Arquitetura

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Cliente   │ ◄─────► │   Servidor  │ ◄─────► │  Recursos   │
│  (Copilot)  │   MCP   │    MCP      │         │   (Dados)   │
└─────────────┘         └─────────────┘         └─────────────┘
```

## 💻 GitHub Copilot e MCPs

### Acesso Gratuito via GitHub Education

O GitHub Education Pack inclui:
- ✅ **GitHub Copilot** completamente grátis
- ✅ **GitHub Copilot Chat** no VS Code
- ✅ **Suporte a MCPs** para extensibilidade
- ✅ **Sem necessidade de Claude pago**

### Setup no VS Code

```json
// .vscode/settings.json
{
  "github.copilot.chat.mcp.enabled": true,
  "github.copilot.chat.mcp.servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./"]
    }
  }
}
```

## 🔧 Servidores MCP Populares

### 1. Servidor GitHub (@modelcontextprotocol/server-github)

**Funcionalidades**:
- Criar issues e pull requests
- Buscar em repositórios
- Ler conteúdo de arquivos
- Gerenciar branches

**Setup**:
```bash
npm install -g @modelcontextprotocol/server-github
```

**Configuração**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "seu_token_aqui"
      }
    }
  }
}
```

### 2. Servidor Filesystem (@modelcontextprotocol/server-filesystem)

**Funcionalidades**:
- Ler e escrever arquivos
- Listar diretórios
- Buscar em arquivos

**Economia**: Automatização de tarefas → **R$ 2.000-5.000/ano**

### 3. Servidor PostgreSQL (@modelcontextprotocol/server-postgres)

**Funcionalidades**:
- Consultar bancos de dados
- Analisar schemas
- Gerenciar dados

### 4. Servidor Memory (@modelcontextprotocol/server-memory)

**Funcionalidades**:
- Contexto persistente entre conversas
- Aprendizado de preferências
- Histórico de projetos

## 💰 APIs com Créditos para Estudantes

### OpenAI

| Recurso | Estudante | Regular | Economia |
|---------|-----------|---------|----------|
| GPT-4 API | Créditos grátis* | $0.03/1K tokens | R$ 6.000-10.000/ano |
| GPT-3.5 | Créditos grátis* | $0.002/1K tokens | R$ 2.000-4.000/ano |
| DALL-E 3 | Créditos inclusos | $0.04/image | R$ 1.000-2.000/ano |

*Via programas educacionais e hackathons

### Anthropic Claude

| Recurso | Estudante | Regular | Economia |
|---------|-----------|---------|----------|
| Claude API | $500-2.000 créditos | $15/1M tokens | R$ 3.000-12.000/ano |
| Claude Pro | Grátis (Education) | $20/mês | R$ 1.200/ano |

**Como aplicar**: [Anthropic AI for Science Program](https://www.anthropic.com/research)

### Google Gemini

| Recurso | Estudante | Regular | Economia |
|---------|-----------|---------|----------|
| Gemini Pro API | 1.500 req/dia grátis | $0.001/1K chars | R$ 4.000-8.000/ano |
| GCP Credits | $300 iniciais | - | R$ 1.800 |
| Vertex AI | Créditos inclusos | Variável | R$ 5.000-10.000/ano |

### Azure OpenAI

| Recurso | Estudante | Regular | Economia |
|---------|-----------|---------|----------|
| Azure Credits | $100-200/ano | - | R$ 600-1.200/ano |
| OpenAI Models | Incluído | Variável | R$ 3.000-6.000/ano |

### Cohere

| Recurso | Estudante | Regular | Economia |
|---------|-----------|---------|----------|
| Production Key | Free trial | $0.40/1M tokens | R$ 2.000-5.000/ano |
| Embeddings | Grátis limitado | $0.10/1M tokens | R$ 1.000-3.000/ano |

### Hugging Face

| Recurso | Estudante | Regular | Economia |
|---------|-----------|---------|----------|
| Inference API | Grátis | Variável | R$ 2.000-4.000/ano |
| AutoTrain | Grátis limitado | $0.50/hora | R$ 3.000-6.000/ano |
| Spaces GPU | PRO grátis* | $0.60/hora | R$ 5.000-10.000/ano |

*Via programas educacionais

## 🚀 Configuração Prática

### Setup Completo com GitHub Education

**Passo 1: Ativar GitHub Education**
```bash
# Acesse
https://education.github.com/pack

# Verifique com email .edu
# Aguarde aprovação (geralmente 1-3 dias)
```

**Passo 2: Configurar GitHub Copilot**
```bash
# Instalar extensões no VS Code
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

**Passo 3: Setup de MCPs**
```bash
# Criar diretório de config
mkdir -p ~/.config/github-copilot

# Criar arquivo de config
cat > ~/.config/github-copilot/mcp.json << 'EOF'
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "~/projects"]
    }
  }
}
EOF
```

**Passo 4: Obter Token GitHub**
```bash
# Acesse: https://github.com/settings/tokens
# Crie token com permissões:
# - repo (full control)
# - read:user
# - read:project

# Adicione ao seu .bashrc ou .zshrc
export GITHUB_TOKEN="seu_token_aqui"
```

### Exemplo de Servidor MCP Customizado

```javascript
// meu-servidor.js
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server({
  name: "servidor-estudante",
  version: "1.0.0",
});

// Definir ferramenta
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "resumir_artigo",
        description: "Resumir artigos científicos em português",
        inputSchema: {
          type: "object",
          properties: {
            url: { type: "string", description: "URL do artigo" },
            nivel: { type: "string", enum: ["basico", "intermediario", "avancado"] }
          },
          required: ["url"]
        }
      }
    ]
  };
});

// Implementar ferramenta
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "resumir_artigo") {
    const { url, nivel = "intermediario" } = request.params.arguments;
    
    // Implementar lógica aqui
    const resumo = await resumirArtigo(url, nivel);
    
    return {
      content: [{ type: "text", text: resumo }]
    };
  }
});

// Iniciar servidor
const transport = new StdioServerTransport();
await server.connect(transport);
```

## 💡 Casos de Uso para Estudantes

### 1. Assistente de Pesquisa

```json
{
  "mcpServers": {
    "pesquisa": {
      "command": "node",
      "args": ["./servidor-pesquisa.js"]
    }
  }
}
```

**Funcionalidades**:
- Buscar papers no arXiv, IEEE, ACM
- Resumir artigos científicos
- Extrair citações e referências
- Comparar metodologias

**Economia**: R$ 5.000-10.000/ano (tempo economizado)

### 2. Code Review Automático

**Funcionalidades**:
- Análise de qualidade de código
- Detecção de bugs e vulnerabilidades
- Sugestões de refatoração
- Verificação de estilo

**Economia**: R$ 3.000-8.000/ano

### 3. Gerador de Documentação

**Funcionalidades**:
- README automático
- Documentação de APIs
- Diagramas de arquitetura
- Comentários em código

**Economia**: R$ 2.000-5.000/ano

### 4. Integração com Banco de Dados

**Funcionalidades**:
- Consultas SQL naturais
- Otimização de queries
- Análise de performance
- Geração de relatórios

**Economia**: R$ 4.000-10.000/ano

## 📊 Comparação: MCPs vs Soluções Tradicionais

| Aspecto | MCPs | Tradicional | Vantagem MCP |
|---------|------|-------------|--------------|
| Setup | Minutos | Horas/Dias | ⚡ 10-20x mais rápido |
| Custo | Grátis* | $50-200/mês | 💰 100% economia |
| Flexibilidade | Alta | Baixa | 🔧 Customizável |
| Manutenção | Baixa | Alta | 🎯 Automatizado |
| Aprendizado | Moderado | Alto | 📚 Mais acessível |

*Com GitHub Education Pack

## 🔐 Segurança e Melhores Práticas

### Gerenciamento de Tokens

```bash
# Nunca commite tokens
# Use variáveis de ambiente
echo "GITHUB_TOKEN=..." >> ~/.env
echo "OPENAI_KEY=..." >> ~/.env

# Adicione ao .gitignore
echo ".env" >> .gitignore
echo "**/mcp.secrets.json" >> .gitignore
```

### Separar Configs Sensíveis

```json
// mcp.json (público)
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "envFile": ".env"
    }
  }
}
```

### Limitar Permissões

- ✅ Use tokens com escopo mínimo necessário
- ✅ Expire tokens periodicamente
- ✅ Revise logs de acesso
- ✅ Use 2FA em todas as contas

## 📈 Economia Total Estimada

| Categoria | Economia Anual | Detalhes |
|-----------|----------------|----------|
| APIs IA | R$ 20.000-40.000 | OpenAI, Claude, Gemini, Cohere |
| MCPs Customizados | R$ 5.000-15.000 | Automação e produtividade |
| GitHub Copilot | R$ 5.000-10.000 | Incluído grátis |
| Ferramentas Dev | R$ 3.000-8.000 | IDEs, testing, deploy |
| **TOTAL** | **R$ 33.000-73.000/ano** | Com GitHub Education Pack |

## 🎓 Recursos para Aprender

### Documentação Oficial
- [MCP Documentation](https://modelcontextprotocol.io)
- [MCP GitHub](https://github.com/modelcontextprotocol)
- [MCP Servers Examples](https://github.com/modelcontextprotocol/servers)

### Tutoriais Recomendados
1. **Building Your First MCP Server** (15min) - [Link](https://modelcontextprotocol.io/quickstart)
2. **GitHub Copilot MCP Integration** (30min) - VS Code Docs
3. **Advanced MCP Patterns** (45min) - Community tutorials

### Comunidades
- Discord: MCP Community
- GitHub Discussions: modelcontextprotocol/sdk
- Reddit: r/machinelearning, r/coding
- Stack Overflow: [mcp] tag

## ✅ Checklist Rápido

- [ ] Ativar GitHub Education Pack
- [ ] Instalar GitHub Copilot no VS Code
- [ ] Configurar servidores MCP básicos (filesystem, github)
- [ ] Obter créditos em APIs de IA (OpenAI, Claude, Gemini)
- [ ] Criar servidor MCP customizado para seu projeto
- [ ] Explorar servidores MCP da comunidade
- [ ] Documentar setup e workflows
- [ ] Participar de comunidades MCP

## 🎯 Próximos Passos

1. **Instale**: GitHub Copilot + MCPs hoje mesmo
2. **Explore**: Teste diferentes servidores MCP
3. **Crie**: Seu próprio servidor para necessidades específicas
4. **Compartilhe**: Contribua com a comunidade
5. **Aprenda**: Cursos gratuitos sobre IA e automação

---

**Última atualização**: 2025-01-08
**Mantido por**: Comunidade de Estudantes Tech Brasil
**Contribua**: [GitHub Issues](https://github.com/Genovese-Felipe/beneficios-estudantis-completo-2025/issues)
