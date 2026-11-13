---
id: docs-especificacoes-ui-spec
title: UI-SPEC — Especificação de UI/UX do COGME
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- constitution.md Art. 2 (hierarquia: Constituição > ADRs > Planos > Specs > Código)
- spec-004 (backend-mvp-v1) §8
- spec-005 (container-layers-v1) §12
- spec-008 (frontend-v1)
- spec-009 (uat-produto-v1)
last-revised: '2026-11-13'
lgpd-class: n/a
tags:
- ui-ux
- especificacoes
- design-system
---

# UI-SPEC — Especificação de UI/UX do COGME

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira  
**Stack:** FastAPI + Jinja2 (server-side) + Vanilla JS + CSS (sem build step)  
**Target:** Profissionais que recebem em moeda estrangeira (devs, freelancers, consultores)  
**Contexto:** Ferramenta de cálculo/Conversor — uso pontual, orientado a tarefa, desktop-first com mobile funcional

---

## 1. Design System (MASTER)

### 1.1 Style Direction
**Primário:** Minimalism & Swiss Style (clean, spacious, grid-based, high contrast)  
**Secundário:** Flat Design (para botões, cards — sem sombras complexas)  
**Anti-style:** Neumorphism (baixo contraste, acessibilidade arriscada), Dark Mode OLED (não é dashboard noturno)

### 1.2 Pattern: Minimal Single Column / Hero + Features + CTA
- Single CTA focus
- Large typography hierarchy
- Generous whitespace (spacing scale 16-64px)
- Mobile-first breakpoints: 375 / 768 / 1024 / 1440
- Sticky CTA no hero (simulador)

### 1.3 Color Tokens (CSS Custom Properties)
```css
:root {
  /* Brand — Navy professional + Blue CTA (trust) */
  --color-primary: #0F172A;           /* Navy 900 — headlines, primary actions */
  --color-primary-hover: #1E293B;     /* Navy 800 */
  --color-accent: #0369A1;            /* Blue 700 — CTA, links, focus ring */
  --color-accent-hover: #0284C7;      /* Blue 600 */
  --color-accent-light: #E0F2FE;      /* Blue 50 — hover backgrounds */

  /* Semantic */
  --color-success: #059669;           /* Emerald 600 — positive values */
  --color-success-light: #ECFDF5;     /* Emerald 50 */
  --color-warning: #D97706;           /* Amber 600 — stale cache */
  --color-warning-light: #FFFBEB;     /* Amber 50 */
  --color-destructive: #DC2626;       /* Red 600 — errors */
  --color-destructive-light: #FEF2F2; /* Red 50 */

  /* Neutral scale */
  --color-bg: #F8FAFC;                /* Slate 50 — page background */
  --color-surface: #FFFFFF;           /* White — cards, forms */
  --color-surface-hover: #F1F5F9;     /* Slate 100 */
  --color-border: #E2E8F0;            /* Slate 200 */
  --color-border-focus: #0369A1;      /* Blue 700 — focus ring */
  --color-text: #0F172A;              /* Navy 900 — body text */
  --color-text-muted: #64748B;        /* Slate 500 — labels, helpers */
  --color-text-placeholder: #94A3B8;  /* Slate 400 */

  /* Typography scale (fluid clamp) */
  --fs-xs: clamp(0.7rem, 0.68rem + 0.1vw, 0.75rem);     /* 11-12px */
  --fs-sm: clamp(0.8125rem, 0.78rem + 0.16vw, 0.875rem); /* 13-14px */
  --fs-base: clamp(0.9375rem, 0.89rem + 0.24vw, 1rem);   /* 15-16px */
  --fs-lg: clamp(1.125rem, 1.05rem + 0.37vw, 1.25rem);   /* 18-20px */
  --fs-xl: clamp(1.5rem, 1.35rem + 0.75vw, 2rem);        /* 24-32px */
  --fs-2xl: clamp(2rem, 1.7rem + 1.5vw, 3rem);           /* 32-48px */

  /* Spacing scale (4px base) */
  --space-1: 4px;   --space-2: 8px;   --space-3: 12px;
  --space-4: 16px;  --space-5: 20px;  --space-6: 24px;
  --space-8: 32px;  --space-10: 40px; --space-12: 48px;
  --space-16: 64px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;

  /* Shadows (subtle, Swiss) */
  --shadow-sm: 0 1px 2px rgba(15,23,42,0.05);
  --shadow-md: 0 4px 12px rgba(15,23,42,0.08);
  --shadow-lg: 0 12px 24px rgba(15,23,42,0.1);

  /* Transitions */
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --easing: cubic-bezier(0.4, 0, 0.2, 1);
}
```

### 1.4 Typography
**Font Family:** IBM Plex Sans (Google Fonts) — financial, trustworthy, professional  
**Weights:** 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold)  
**Base:** 16px / 1.5 line-height  
**Hierarchy:**
- H1: `--fs-2xl` / 700 / `--color-primary` / letter-spacing -0.02em
- H2: `--fs-xl` / 600 / `--color-primary`
- H3: `--fs-lg` / 600 / `--color-primary`
- Body: `--fs-base` / 400 / `--color-text` / 1.6
- Label: `--fs-sm` / 500 / `--color-text-muted` / uppercase / letter-spacing 0.02em
- Mono (numbers): `--fs-base` / 500 / `font-variant-numeric: tabular-nums`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### 1.5 Icon System
**Library:** Lucide (SVG, 24×24, stroke-width 2) — clean, consistent, no emoji  
**Usage:** Inline SVG com `aria-hidden="true"` + texto acessível adjacente  
**Key icons:** calculator, file-text, download, alert-circle, info, chevron-down, loader-2

---

## 2. Page Specifications

### 2.1 `/` — Simulador (Página Principal)

**Layout:** Single column, max-width 640px, centered  
**Sections:**
1. **Hero (sticky top no mobile):** Logo + headline + subheadline
2. **Form Card:** Grid 2-col em ≥768px, 1-col mobile
3. **Result Card:** Aparece após submit bem-sucedido
4. **Notice/Footer:** Disclaimer legal

**Form Fields (ordem lógica):**
| Campo | Tipo | Obrigatório | Validação | Notas |
|-------|------|-------------|-----------|-------|
| Moeda | Select (USD/EUR) | Sim | Enum | Default USD |
| Regime | Select (5 opts) | Sim | Enum | Toggle quantity |
| Valor/unidade | Number (step 0.01) | Sim | >0, ≤1B, 2 casas | BRL |
| Quantidade | Number (step 1) | Cond. | >0, ≤100k, 2 casas | Hide se fixed |
| Spread % | Number (step 0.0001) | Sim | 0-100, 4 casas | Default 2 |
| IOF % | Number (step 0.0001) | Sim | 0-100, 4 casas | Default 0.38 |

**Interactions:**
- Regime change → toggle quantity field (smooth slide, 200ms)
- Inline validation on blur (verde check / vermelho erro + `aria-describedby`)
- Submit → loading state (spinner + "Calculando…", disable button)
- Error → focus error summary (role="alert", links para campos)
- Success → result card slide-down (250ms), scroll suave

**Result Card:**
- Grid 2-col: label (muted) + value (tabular-nums, bold no total)
- Stale badge (amber) se `quote.stale=true`
- Notice legal fixa no rodapé do card

### 2.2 `/invoice` — Emissão de Invoice

**Layout:** Two-section form (Simulação + Partes/Documento), max-width 720px  
**Sections:**
1. **Simulação** (reutiliza campos do simulador + hidden inputs)
2. **Partes e Documento** —fieldset agrupado:
   - Emitente (nome*, documento, endereço)
   - Cliente (nome*, documento, endereço)
   - Número invoice*, Data emissão*, Descrição*

**Interactions:**
- Mesmo toggle quantity por regime
- Validação inline on blur + `aria-describedby`
- Submit → loading "Gerando…" → PDF download automático
- 503 → retry button inline no error global
- Success → toast "PDF baixado" + result summary card

### 2.3 PDF Invoice (Download)

**Template:** `invoice.html` — A4, 18mm margens, DejaVu Sans  
**Typography:** 10pt base, tabular-nums em valores  
**Sections:** Header (logo + nº + data) → Partes (2-col) → Descrição → Valores moeda original → Cotação → Conversão BRL → Notice legal  
**Stale warning:** Amber box se cotação desatualizada  
**Page numbering:** `@bottom-center` counter

---

## 3. Component Specifications

### 3.1 Form Field (Base)
```html
<div class="field">
  <label for="field-id" class="label">
    Label <span class="required" aria-hidden="true">*</span>
    <span class="sr-only">(obrigatório)</span>
  </label>
  <input 
    id="field-id" 
    name="field-name" 
    type="text" 
    class="input"
    aria-describedby="field-id-hint field-id-error"
    required
  >
  <p id="field-id-hint" class="hint">Texto de ajuda</p>
  <p id="field-id-error" class="error" role="alert" aria-live="polite"></p>
</div>
```

**States:**
- Default: border `--color-border`
- Hover: border `--color-border` + `--color-text-muted` (40%)
- Focus: border `--color-border-focus`, ring `0 0 0 3px var(--color-accent-light)`, outline none
- Invalid: border `--color-destructive`, ring `0 0 0 3px var(--color-destructive-light)`
- Disabled: opacity 0.5, cursor not-allowed

### 3.2 Button (Primary / Secondary / Ghost)
```css
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-2);
  font: 500 var(--fs-base) var(--font-family);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  border: none; cursor: pointer;
  transition: background var(--duration-fast) var(--easing), transform var(--duration-fast);
}
.btn:active { transform: scale(0.98); }
.btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }
.btn-primary { background: var(--color-primary); color: white; }
.btn-primary:hover:not(:disabled) { background: var(--color-primary-hover); }
.btn-secondary { background: var(--color-surface); color: var(--color-primary); border: 1px solid var(--color-border); }
.btn-secondary:hover:not(:disabled) { background: var(--color-surface-hover); }
.btn-ghost { background: transparent; color: var(--color-accent); }
.btn-ghost:hover:not(:disabled) { background: var(--color-accent-light); }
```

### 3.3 Select (Custom Styled)
```css
.select {
  appearance: none;
  background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748B' stroke-width='2'><path d='M6 9l6 6 6-6'/></svg>");
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
  background-size: 20px;
  padding-right: var(--space-10);
}
```

### 3.4 Card (Form / Result)
```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  padding: var(--space-6);
}
```

### 3.5 Alert / Toast
```css
.alert {
  display: flex; align-items: flex-start; gap: var(--space-3);
  padding: var(--space-4); border-radius: var(--radius-md);
  font-size: var(--fs-sm); line-height: 1.5;
}
.alert-error { background: var(--color-destructive-light); color: var(--color-destructive); border: 1px solid #FECACA; }
.alert-warning { background: var(--color-warning-light); color: var(--color-warning); border: 1px solid #FCD34D; }
.alert-success { background: var(--color-success-light); color: var(--color-success); border: 1px solid #A7F3D0; }
.alert-info { background: var(--color-accent-light); color: var(--color-accent); border: 1px solid #BAE6FD; }
```

### 3.6 Loading Spinner
```css
.spinner {
  width: 20px; height: 20px;
  border: 2px solid transparent; border-top-color: currentColor;
  border-radius: 50%; animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .spinner { animation: none; border-top-color: transparent; border-color: currentColor; } }
```

---

## 4. Interaction & Motion Spec

### 4.1 Transitions (Respeita `prefers-reduced-motion`)
| Elemento | Propriedade | Duração | Easing |
|----------|-------------|---------|--------|
| Button hover/focus | background, transform | 150ms | ease-out |
| Input focus ring | box-shadow, border-color | 150ms | ease-out |
| Field error appear | opacity, transform-y | 200ms | ease-out |
| Quantity toggle | height, opacity, padding | 250ms | cubic-bezier(0.4,0,0.2,1) |
| Result card enter | opacity, transform-y | 300ms | cubic-bezier(0.16,1,0.3,1) |
| Toast enter/exit | opacity, transform-y | 200ms | ease-out |

### 4.2 Focus Management
- Submit error → focus error summary (`role="alert" tabindex="-1"`)
- Modal/overlay → trap focus, restore on close
- Skip link no topo: "Pular para conteúdo principal"

### 4.3 Keyboard Navigation
- Tab order: lógico (topo → baixo)
- Enter em button = submit
- Escape fecha toast/modal
- Setas em select nativo

---

## 5. Accessibility Requirements (WCAG 2.1 AA)

### 5.1 Contrast
- Texto normal: ≥4.5:1 (atendido: `#0F172A` on `#F8FAFC` = 13.6:1)
- Texto grande (≥18px bold): ≥3:1
- UI components (borders, focus rings): ≥3:1
- Estados de erro: `#DC2626` on `#FEF2F2` = 5.9:1 ✓

### 5.2 Semantic HTML
- `<main>`, `<section>`, `<fieldset>` + `<legend>` para grupos
- `<label for="id">` em todos os inputs
- `<output>` para valores calculados (result card)
- `role="alert"` para error summary e toast
- `aria-live="polite"` para stale warning e notice

### 5.3 Form Accessibility
- `required` + `aria-required="true"` + visual `*` + `(obrigatório)` sr-only
- `aria-describedby` ligando input → hint + error
- `autocomplete` apropriado (name, email, off para sensíveis)
- Error summary no topo com links para `#field-id`

### 5.4 Touch Targets
- Mínimo 44×44px (botões, inputs, links)
- Espaçamento 8px entre alvos adjacentes

### 5.5 Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
  .spinner { animation: none; border-color: currentColor; }
}
```

---

## 6. Responsive Breakpoints

| Breakpoint | Container | Grid | Notas |
|------------|-----------|------|-------|
| ≤480px | 100% - 32px | 1-col | Full-width inputs, sticky CTA bottom |
| 481-768px | 100% - 40px | 1-col | Hero compacto |
| 769-1024px | 640px | 2-col (form) | Side-by-side labels/inputs |
| ≥1025px | 640px | 2-col | Max-width centralizado |

```css
.wrap { width: min(100% - 2rem, 640px); margin: 0 auto; }
@media (max-width: 480px) { .wrap { padding: 1rem; } }
.field-grid { display: grid; grid-template-columns: 1fr; gap: var(--space-4); }
@media (min-width: 769px) { .field-grid { grid-template-columns: repeat(2, 1fr); } }
```

---

## 7. Dark Mode (Opcional — Futuro)

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0F172A;
    --color-surface: #1E293B;
    --color-surface-hover: #334155;
    --color-border: #334155;
    --color-text: #F8FAFC;
    --color-text-muted: #94A3B8;
    --color-text-placeholder: #64748B;
    --color-primary: #F8FAFC;
    --color-primary-hover: #E2E8F0;
    --color-accent: #38BDF8;
    --color-accent-hover: #0EA5E9;
    --color-accent-light: #0369A1;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
    --shadow-lg: 0 12px 24px rgba(0,0,0,0.5);
  }
}
```
**Nota:** Implementar somente após validação light mode. Requer testes de contraste completos.

---

## 8. Implementation Checklist (Por Componente)

### 8.1 Base Setup
- [ ] CSS custom properties em `:root` (app.css)
- [ ] IBM Plex Sans import + preconnect
- [ ] Reset/normalize moderno (box-sizing, margin 0)
- [ ] Fluid typography clamp functions
- [ ] Spacing/radius/shadow tokens

### 8.2 Layout
- [ ] `.wrap` container responsivo
- [ ] Header: logo + nav (2 links) — sticky no mobile
- [ ] Main: single column centered
- [ ] Footer: notice legal fixo

### 8.3 Form Components
- [ ] Input/Select/Textarea base styles
- [ ] Focus ring visível (3px, `--color-accent-light`)
- [ ] Invalid state (border + ring vermelho)
- [ ] Disabled state
- [ ] Label + required indicator + sr-only
- [ ] Hint + error slots (`aria-describedby`)

### 8.4 Buttons
- [ ] Primary / Secondary / Ghost variants
- [ ] Loading state (spinner + texto)
- [ ] Disabled state
- [ ] Active press (scale 0.98)

### 8.5 Cards
- [ ] Form card (border + shadow-sm)
- [ ] Result card (grid 2-col, tabular-nums)
- [ ] Stale badge (amber)
- [ ] Notice legal

### 8.6 Interactions
- [ ] Regime toggle (slide animation)
- [ ] Inline validation on blur
- [ ] Error summary focus management
- [ ] Submit loading → success/error
- [ ] PDF download automático
- [ ] Retry button no 503

### 8.7 Accessibility
- [ ] Skip link
- [ ] Semantic landmarks
- [ ] Focus order lógico
- [ ] ARIA labels/describedby/live
- [ ] `prefers-reduced-motion` respetado
- [ ] Contraste 4.5:1 verificado

### 8.8 PDF Template
- [ ] A4 margins corretos
- [ ] DejaVu Sans embedded
- [ ] Tabular-nums em valores
- [ ] Page numbering
- [ ] Stale warning box

---

## 9. Acceptance Criteria (UAT-05 / spec-009)

| Critério | Teste |
|----------|-------|
| **Responsivo** | 375px / 768px / 1024px / 1440px — sem scroll horizontal |
| **Acessibilidade** | axe-core 0 violations AA; navegação teclado completa |
| **Contraste** | Todos textos ≥4.5:1; focus rings ≥3:1 |
| **Touch** | Botões/inputs ≥44×44px; espaçamento 8px |
| **Motion** | `prefers-reduced-motion` desativa animações |
| **Forms** | Validação inline on blur; error summary focável; required indicado |
| **Loading** | Submit → spinner + disable → success/error toast |
| **PDF** | Download automático; A4 correto; valores tabular-nums |
| **Stale** | Badge amber visível quando `quote.stale=true` |
| **Performance** | CSS <15KB gzipped; sem JS blocking; LCP <2.5s |

---

## 10. Migration Plan (Incremental)

| Fase | Escopo | Entregável |
|------|--------|------------|
| **1. Tokens & Base** | CSS variables, typography, reset, container | `app.css` refatorado |
| **2. Components** | Input, Select, Button, Card, Alert | Componentes reutilizáveis |
| **3. Simulador** | `/` — hero, form, result, interactions | Index.html + JS atualizado |
| **4. Invoice Form** | `/invoice` — two-section form | invoice_form.html + JS |
| **5. PDF Template** | `invoice.html` — styling consistente | Template atualizado |
| **6. Accessibility** | Skip link, ARIA, focus mgmt, reduced motion | Auditoria axe-core |
| **7. Dark Mode** | (Opcional) Media query + tokens | `@media (prefers-color-scheme: dark)` |

---

## 11. Risks & Mitigations

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Dark mode quebra contraste | Média | Alto | Implementar apenas Fase 7, após testes AA |
| PDF template fonts | Baixa | Médio | DejaVu Sans já instalado no Docker; testar geração |
| JS vanilla maintenance | Média | Baixo | Manter módulos IIFE simples; documentar padrões |
| Mobile sticky CTA | Baixa | Baixo | `position: sticky; bottom: 0` com safe-area-inset |

---

## 12. Referências

- **Design System Source:** ui-ux-pro-max — Minimalism & Swiss Style + Calculator/Converter pattern
- **Typography:** IBM Plex Sans — financial/trustworthy mood
- **Icons:** Lucide SVG — 24×24, stroke-width 2
- **WCAG 2.1 AA:** Contrast, Focus, Forms, Motion, Semantics
- **Specs irmãs:** spec-004 (backend), spec-005 (containers), spec-008 (frontend), spec-009 (UAT)

---

**Fim da especificação.**  
Próximo passo: implementar Fase 1 (Tokens & Base) → validar com design review → prosseguir incremental.