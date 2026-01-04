# GitHub Profile - Visual Elements Guide

## 🎨 Elementos Visuais Implementados

### 1. 🐍 Snake Animation (Eating Contributions)
Aquela animação clássica onde a cobrinha "come" seus quadradinhos de contribuição do GitHub.

**Como funciona:**
- GitHub Action roda automaticamente a cada 6 horas
- Gera SVG animado baseado no seu contribution graph
- Salva em branch separada (`output`)

**Arquivo:** `.github/workflows/snake.yml`

**Preview:**
```
🟩🟩🟩🟩🟩🟩🟩 ← Cobrinha come os commits!
```

---

### 2. 📊 GitHub Stats Cards

#### Stats Gerais
- Total de commits
- PRs, Issues
- Repos públicos
- Contribuições privadas (se ativado)

#### Streak Stats
- Dias consecutivos de commits
- Maior sequência
- Contribuições totais

#### Language Distribution
- % de cada linguagem
- Baseado em todos os repos
- Atualiza automaticamente

---

### 3. 📈 Activity Graph
Gráfico de linha mostrando sua atividade ao longo do tempo.

**Features:**
- Última semana/mês de commits
- Cores personalizadas (tema GitHub Dark)
- Atualiza em tempo real

---

### 4. ⚡ Recent Activity (Auto-Update)
Lista suas últimas ações no GitHub:
- ⭐ Starred repos
- 🔀 Pull requests
- 💬 Issues comentadas
- 📝 Commits recentes

**Atualização:** A cada 30 minutos via GitHub Actions

---

### 5. 🔥 Live Activity Badge (SVG Customizado)
Badge SVG gerado dinamicamente mostrando:
- Projetos ativos (última semana)
- Commits dos últimos 7 dias
- Timestamp de atualização

**Localização:** `stats/live-activity.svg`

---

### 6. 📊 Real-time Stats (JSON)
Dados em tempo real salvos em JSON para possíveis integrações futuras.

**Dados inclusos:**
```json
{
  "user": {
    "public_repos": 45,
    "followers": 123,
    "following": 89
  },
  "recent_commits": [...],
  "active_projects": [...],
  "contributions": {
    "commits_pushed": 87,
    "pull_requests": 12,
    "issues": 5
  }
}
```

---

## 🎨 Personalizações Disponíveis

### Temas para Stats Cards

**Dark Themes:**
```markdown
theme=dark           # GitHub Dark (atual)
theme=radical        # Pink/Purple
theme=tokyonight     # Blue/Purple
theme=dracula        # Purple
theme=gruvbox        # Brown/Orange
theme=onedark        # Dark blue
theme=cobalt         # Deep blue
theme=synthwave      # Neon pink/blue
theme=highcontrast   # Black & white
theme=nightowl       # Dark blue
```

**Light Themes:**
```markdown
theme=default        # White
theme=vue            # Green
theme=solarized-light
theme=graywhite
```

### Cores Customizadas

Você pode personalizar cada elemento:
```markdown
&bg_color=0D1117          # Fundo
&title_color=58A6FF       # Títulos
&text_color=C9D1D9        # Texto
&icon_color=1F6FEB        # Ícones
&hide_border=true         # Remover borda
```

### Esconder Elementos

```markdown
&hide=stars,commits,prs,issues    # Esconder stats específicos
&hide=contribs                    # Esconder contribuições
```

---

## 🚀 GitHub Actions Configurados

| Workflow | Frequência | Função |
|----------|-----------|--------|
| `snake.yml` | 6 horas | Gera animação da cobrinha |
| `update-activity.yml` | 30 minutos | Atualiza atividade recente |
| `stats.yml` | 1 hora | Atualiza estatísticas em tempo real |
| `update-deployments.yml` | Diário | Atualiza status de deploys |

---

## 🎯 Como Funciona em Tempo Real

### Fluxo de Atualização:

```
GitHub API
    ↓
GitHub Actions (automático)
    ↓
Scripts Python
    ↓
Gera SVGs/JSONs
    ↓
Commit automático
    ↓
README atualizado!
```

### O que atualiza sozinho:
✅ Contribution graph (quadradinhos)
✅ Snake animation
✅ Recent Activity (últimas 5 ações)
✅ Stats cards (commits, PRs, etc)
✅ Activity graph
✅ Streak stats
✅ Language distribution
✅ Deployment status

### O que é estático:
❌ Seções de texto (About, Tech Stack, etc)
❌ Links (LinkedIn, email, website)
❌ Estrutura dos repos (Research/Industrial/Products)

---

## 📸 Adicionar Imagens Customizadas

### Banner no topo:
```markdown
![Banner](./assets/banner.png)
```
**Dimensões recomendadas:** 1280x640px ou 1920x1080px

### Logo/Avatar animado:
```markdown
<img src="./assets/avatar.gif" width="200" />
```

### Badges customizados:
```markdown
![Badge](https://img.shields.io/badge/AI-Researcher-blue?style=for-the-badge&logo=tensorflow)
```

### GIFs de demonstração:
```markdown
<img src="./assets/demo.gif" alt="Demo" width="600"/>
```

---

## 🔧 Configuração Pós-Deploy

### 1. Ativar GitHub Actions
No repositório, vá em:
- **Settings** → **Actions** → **General**
- Workflow permissions: **Read and write permissions** ✅
- Save

### 2. Primeira execução manual
- Vá em **Actions**
- Selecione cada workflow
- Clique em "Run workflow"

### 3. Aguarde 5-10 minutos
As animações e stats começarão a aparecer!

### 4. Troubleshooting
Se algo não aparecer:
```bash
# Verificar se os workflows rodaram
GitHub → Actions → Verificar status

# Re-executar workflow manualmente
Actions → [Nome do workflow] → Run workflow
```

---

## 🎨 Dicas de Design

### 1. Consistência de Cores
Use a paleta do GitHub Dark:
- `#0D1117` - Fundo
- `#58A6FF` - Azul primário
- `#1F6FEB` - Azul secundário
- `#C9D1D9` - Texto claro
- `#8B949E` - Texto secundário

### 2. Espaçamento
- Use `---` para separar seções
- Use `<br>` para espaço vertical extra
- Use tabelas para layout lado a lado

### 3. Hierarquia Visual
```markdown
# H1 - Muito raro (só nome)
## H2 - Seções principais
### H3 - Subseções
**Bold** - Destacar termos importantes
`code` - Tecnologias, comandos
```

---

## 🚀 Próximos Passos

Após fazer o deploy, você pode:

1. **Adicionar banner customizado**
   - Criar em Canva/Figma
   - Salvar em `assets/banner.png`
   - Adicionar no topo do README

2. **Criar badges customizados**
   - shields.io para badges estáticos
   - Badgen.net para badges dinâmicos

3. **Integrar com site pessoal**
   - Link direto para repos específicos
   - Embed dos stats no site

4. **Adicionar GIFs de projetos**
   - Screen recordings
   - Demos animados
   - Tutoriais visuais

---

**Tudo atualiza em tempo real! 🔥**

Seus commits, projetos ativos, e atividade aparecem automaticamente sem você fazer nada!
