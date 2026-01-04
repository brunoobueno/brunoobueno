# Instruções de Deploy

## 📦 Como publicar no GitHub

### 1. Criar o repositório

No GitHub, crie um novo repositório:
- Nome: **brunoobueno** (exatamente igual ao seu username)
- Visibilidade: **Public**
- ✅ Não inicialize com README (vamos fazer upload do nosso)

### 2. Fazer upload dos arquivos

```bash
cd "c:\Users\Bueno\Desktop\projetos 02.12\githubPro\brunoobueno"

# Inicializar git
git init

# Adicionar todos os arquivos
git add .

# Commit inicial
git commit -m "🚀 Initial commit: Professional GitHub profile"

# Conectar ao repositório remoto
git remote add origin https://github.com/brunoobueno/brunoobueno.git

# Enviar para o GitHub
git push -u origin main
```

### 3. Verificar o perfil

Acesse: https://github.com/brunoobueno

O README.md será exibido automaticamente no topo do seu perfil!

## 🔧 Configurações Opcionais

### Ativar GitHub Actions (Auto-update de deploys + animações)

**IMPORTANTE:** Sem isso, as animações e updates em tempo real não funcionam!

1. Vá em **Settings** → **Actions** → **General**
2. Em "Workflow permissions", selecione:
   - ✅ "Read and write permissions"
   - ✅ "Allow GitHub Actions to create and approve pull requests"
3. Salve as alterações
4. Vá em **Actions** e execute cada workflow manualmente pela primeira vez:
   - `Generate Snake Animation`
   - `Update Recent Activity`
   - `Profile Stats & Metrics`
   - `Update Latest Deployments`

### Aguarde 5-10 minutos
Após rodar os workflows, as animações começarão a aparecer!

### Verificar se funcionou
- Snake animation: `https://github.com/brunoobueno/brunoobueno/blob/output/github-contribution-grid-snake-dark.svg`
- Se aparecer, está funcionando! ✅

### Personalizar Links

Edite os arquivos README e atualize:
- LinkedIn URL
- Email
- Website (brunobueno.tech)
- Nome dos repositórios

### Ajustar Cores dos Badges

No README, você pode personalizar as cores dos badges:
- `color=58A6FF` → Azul GitHub
- `color=green` → Verde
- `color=red` → Vermelho
- etc.

## 📸 Preview Local

Você pode visualizar o README localmente usando:
- VS Code com extensão "Markdown Preview Enhanced"
- grip (ferramenta de preview GitHub): `pip install grip && grip README.md`

## 🎨 Customizações Futuras

### Adicionar Banner Personalizado

1. Crie uma imagem (1280x640px recomendado)
2. Salve em `assets/banner.png`
3. Adicione no topo do README:
```markdown
![Banner](./assets/banner.png)
```

### Adicionar GIFs / Animações

```markdown
<div align="center">
  <img src="https://media.giphy.com/media/YOUR_GIF_ID/giphy.gif" width="600"/>
</div>
```

### Trocar Tema dos Stats

No README, altere `theme=dark` para:
- `theme=radical`
- `theme=tokyonight`
- `theme=dracula`
- `theme=gruvbox`

## 🔄 Manutenção

### Atualizar manualmente os deploys

```bash
python scripts/update_deployments.py
git add README.md README.pt-BR.md
git commit -m "📊 Update deployment status"
git push
```

### Adicionar novo repositório à lista

Edite `scripts/update_deployments.py` e adicione nos dicionários:
```python
PRODUCTION_REPOS = {
    'novo-repo': 'Descrição',
    # ...
}
```

## ✅ Checklist Pós-Deploy

- [ ] Repositório criado com nome correto
- [ ] README.md aparece no perfil
- [ ] Links funcionando (LinkedIn, email, etc)
- [ ] Badges carregando corretamente
- [ ] Versão PT-BR acessível
- [ ] GitHub Actions configurado (opcional)
- [ ] Repositórios linkados existem

---

**Dúvidas?** Abra uma issue ou me contate!
