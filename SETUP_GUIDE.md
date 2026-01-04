# 🎨 Guia Completo de Configuração

## ✅ Checklist de Deploy

### 1️⃣ Criar Repositório no GitHub
- [ ] Nome: **brunoobueno** (igual ao seu username)
- [ ] Visibilidade: **Public**
- [ ] Não inicializar com README

### 2️⃣ Fazer Upload
```bash
cd "c:\Users\Bueno\Desktop\projetos 02.12\githubPro\brunoobueno"
git init
git add .
git commit -m "🚀 Initial: Complete professional profile"
git remote add origin https://github.com/brunoobueno/brunoobueno.git
git push -u origin main
```

### 3️⃣ Configurar GitHub Actions

#### Ativar Workflows
1. **Settings** → **Actions** → **General**
2. Workflow permissions:
   - ✅ "Read and write permissions"
   - ✅ "Allow GitHub Actions to create and approve pull requests"
3. **Save**

#### Executar Workflows Manualmente (primeira vez)
1. Vá em **Actions**
2. Execute cada workflow:
   - ✅ Generate Snake Animation
   - ✅ Update Recent Activity
   - ✅ Profile Stats & Metrics
   - ✅ Update Latest Commits & Deploys
   - ✅ Update Latest Deployments

---

## 🔑 Configurações de Secrets (Opcional)

### WakaTime (Atividade de Codificação)

**O que é:** Mostra quanto tempo você passa codando em cada linguagem/projeto.

**Setup:**
1. Crie conta em [wakatime.com](https://wakatime.com)
2. Instale extensão WakaTime no VS Code
3. Configure sua API key
4. No GitHub: **Settings** → **Secrets and variables** → **Actions**
5. Adicione secret:
   - Name: `WAKATIME_API_KEY`
   - Value: [sua chave da WakaTime]

**Nota:** Opcional, mas mostra sua atividade de coding em tempo real!

---

### Metrics Token (GitHub Metrics Avançadas)

**O que é:** Gera visualizações avançadas de suas estatísticas.

**Setup:**
1. Vá em **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Generate new token (classic)
3. Selecione escopos:
   - ✅ `public_repo`
   - ✅ `read:user`
   - ✅ `repo:status`
4. Copy token
5. No repo, vá em **Settings** → **Secrets and variables** → **Actions**
6. Adicione:
   - Name: `METRICS_TOKEN`
   - Value: [token copiado]

**Nota:** Também opcional, mas adiciona métricas visuais incríveis.

---

## 🎨 Personalização Pós-Deploy

### Adicionar Banner Personalizado

1. **Crie um banner** (1280x640px):
   - Use [Canva](https://canva.com)
   - Ou veja `assets/BANNER_GUIDE.md`

2. **Salve como** `assets/banner.png`

3. **Adicione no README** (topo):
```markdown
<div align="center">

![Banner](./assets/banner.png)

# Bruno Bueno
...
```

---

### Adicionar Screenshots/GIFs dos Projetos

1. **Tire screenshots** ou grave GIFs dos seus projetos
2. **Salve em** `assets/projects/`
3. **Atualize Featured Projects**:

```markdown
### 🩺 SofiaMed AI

<img src="./assets/projects/sofiaemed-demo.gif" width="500" />

> Intelligent medical assistant...
```

---

### Customizar Cores e Temas

**Trocar tema dos stats:**

No README, substitua `theme=dark` por:
```markdown
theme=radical       # Pink/Purple
theme=tokyonight    # Blue/Purple
theme=dracula       # Purple vampiro
theme=gruvbox       # Brown/Orange
theme=synthwave     # Neon cyberpunk
```

**Exemplo:**
```markdown
![Stats](https://github-readme-stats.vercel.app/api?username=brunoobueno&theme=tokyonight...)
```

---

## 🔧 Troubleshooting

### Snake não aparece?
1. Vá em **Actions** → **Generate Snake Animation**
2. Verifique se rodou sem erros
3. Aguarde 5-10 minutos
4. Force refresh: Ctrl+Shift+R

### Stats não carregam?
- Provavelmente cache do GitHub
- Aguarde alguns minutos
- Ou adicione `&cache_seconds=1800` na URL

### WakaTime não atualiza?
1. Verifique se secret `WAKATIME_API_KEY` está configurado
2. Certifique-se que a extensão WakaTime está ativa no VS Code
3. Aguarde 1-2 horas de coding para aparecer dados

### Activity section vazia?
- GitHub Actions precisa rodar pelo menos 1x
- Execute manualmente: Actions → workflow → Run workflow
- Ou faça um commit/push para trigger

---

## 📊 Automações Ativas

Após configuração completa, você terá:

| Feature | Update | Status |
|---------|--------|--------|
| 🐍 Snake animation | 6 horas | Auto |
| 📊 GitHub stats | Real-time | Auto |
| 🔥 Latest commits | 2 horas | Auto |
| 🚀 Latest releases | 2 horas | Auto |
| ⚡ Recent activity | 30 min | Auto |
| 💻 WakaTime coding | 1 hora | Auto (se configurado) |
| 📈 Deployment status | Diário | Auto |
| 🏆 Trophies | Real-time | Auto |

---

## 🎯 Links para Atualizar

Antes do deploy, revise e atualize esses links nos arquivos:

### README.md e README.pt-BR.md
- ✅ LinkedIn: `https://www.linkedin.com/in/bruno-bueno-1711351a0/` (já atualizado)
- ✅ Instagram: `https://www.instagram.com/brunoobueno/` (já atualizado)
- ✅ Email: `bruno@brunobueno.tech`
- ✅ Website: `https://brunobueno.tech`

### scripts/update_deployments.py
Verifique se os nomes dos repos estão corretos:
```python
PRODUCTION_REPOS = {
    'erpnext-brasil': 'Industrial ERP',
    'smtp-alquimia': 'Email Infrastructure',
    # ... etc
}
```

---

## 🚀 Resultado Final

Depois de tudo configurado, seu perfil terá:

✅ Header com badges e links sociais  
✅ Live activity badge (SVG dinâmico)  
✅ Seção "About" profissional  
✅ Featured Projects com cards visuais  
✅ Projetos organizados por categoria (Research/Industrial/Products)  
✅ Latest Deployments (auto-update)  
✅ Tech stack com badges  
✅ GitHub stats completos  
✅ Streak stats  
✅ Language distribution  
✅ Snake animation (cobrinha)  
✅ GitHub trophies  
✅ WakaTime coding activity (se configurado)  
✅ Latest commits em tempo real  
✅ Latest releases  
✅ Recent activity (últimas 5 ações)  
✅ Seção de contato com todos os links  
✅ View counter  
✅ Bilíngue (EN/PT-BR)  

**Tudo atualiza automaticamente! 🎉**

---

## 📱 Preview Mobile

O profile é responsivo e funciona bem em:
- 📱 Mobile
- 💻 Desktop
- 🖥️ Tablet

Teste em: `https://github.com/brunoobueno`

---

## 🆘 Precisa de Ajuda?

1. Verifique `VISUAL_ELEMENTS.md` para detalhes de cada elemento
2. Veja `BANNER_GUIDE.md` para criar banners
3. Confira `REPO_README_TEMPLATE.md` para padronizar outros repos

---

**Está tudo pronto para deploy! 🚀**

Faça o upload, configure as Actions, e em alguns minutos seu perfil estará incrível!
