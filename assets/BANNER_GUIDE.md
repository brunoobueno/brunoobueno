# Exemplo de Banner para GitHub Profile

## 🎨 Como Criar um Banner

### Opção 1: Canva (Fácil)
1. Acesse [canva.com](https://canva.com)
2. Crie design 1280x640px ou 1920x1080px
3. Temas sugeridos:
   - Dark mode (fundo #0D1117)
   - Gradiente azul (#58A6FF → #1F6FEB)
   - Minimalista com logo/nome
4. Exporte como PNG
5. Salve em `assets/banner.png`

### Opção 2: Figma (Profissional)
1. Template disponível: [GitHub Profile Banner](https://figma.com)
2. Personalize com:
   - Seu nome
   - Tagline
   - Tech stack icons
   - Gradientes
3. Export → PNG → 2x

### Opção 3: Código (SVG)
Crie um banner em SVG programaticamente:

```svg
<svg width="1280" height="640" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0D1117" />
      <stop offset="100%" style="stop-color:#1F6FEB" />
    </linearGradient>
  </defs>
  
  <rect width="1280" height="640" fill="url(#bg)" />
  
  <text x="640" y="280" font-family="Arial" font-size="72" fill="#58A6FF" 
        text-anchor="middle" font-weight="bold">
    BRUNO BUENO
  </text>
  
  <text x="640" y="340" font-family="Arial" font-size="32" fill="#C9D1D9" 
        text-anchor="middle">
    AI Researcher (ITA) • Industrial AI Lead
  </text>
  
  <text x="640" y="400" font-family="Arial" font-size="24" fill="#8B949E" 
        text-anchor="middle" font-style="italic">
    Building production-grade AI for real industrial environments
  </text>
</svg>
```

## 📐 Dimensões Recomendadas

| Tipo | Largura | Altura | Uso |
|------|---------|--------|-----|
| Banner Wide | 1920px | 1080px | Desktop |
| Banner Standard | 1280px | 640px | Recomendado |
| Banner Compact | 1200px | 400px | Mobile-friendly |
| Avatar/Logo | 500px | 500px | Quadrado |

## 🎨 Paleta de Cores GitHub Dark

```css
Background:    #0D1117
Cards:         #161B22
Borders:       #30363D
Primary:       #58A6FF
Secondary:     #1F6FEB
Text:          #C9D1D9
Text Muted:    #8B949E
Success:       #3FB950
Warning:       #D29922
Error:         #F85149
```

## ✨ Elementos Populares

### 1. Typing Animation
```markdown
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=58A6FF&center=true&vCenter=true&width=435&lines=AI+Researcher+%40+ITA;Industrial+AI+Lead;DevOps+%26+Infrastructure)](https://git.io/typing-svg)
```

### 2. Animated Wave
```markdown
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png">
```

### 3. Tech Stack Icons
```markdown
<p align="center">
  <img src="https://skillicons.dev/icons?i=python,ts,react,docker,kubernetes,postgres,aws" />
</p>
```

## 🖼️ Como Adicionar no README

### No topo (recomendado):
```markdown
<div align="center">

![Banner](./assets/banner.png)

# Bruno Bueno
...
```

### Como background section:
```markdown
<div align="center">
  <img src="./assets/banner.png" style="width: 100%; max-width: 1200px;" />
</div>
```

## 📦 Assets Sugeridos

Crie esses arquivos em `assets/`:
- `banner.png` - Banner principal
- `avatar.gif` - Avatar animado (opcional)
- `logo.svg` - Logo pessoal
- `tech-icons/` - Ícones customizados de tecnologias

## 🔗 Recursos Úteis

- **Icons**: [shields.io](https://shields.io), [skill-icons](https://skillicons.dev)
- **Fonts**: [Google Fonts](https://fonts.google.com)
- **Colors**: [GitHub Primer](https://primer.style/design/foundations/color)
- **Inspiration**: [awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme)

---

**Dica:** Mantenha o banner simples e profissional. Menos é mais!
