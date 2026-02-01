# Portfolio Design Theme Reference

Use this file as the single source of truth when styling any page or component.

---

## Core Identity

**Style:** Clean, minimal, graph-paper aesthetic. Not a typical dark dev portfolio — uses light backgrounds with strong black line work and white cards. Inspired by notebook/whiteboard design language.

---

## Page Background

- **Background color:** `#e8e8e8` (light gray)
- **Grid pattern:** CSS grid lines using:
  ```css
  background-image:
    linear-gradient(rgba(0,0,0,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,0,0,0.06) 1px, transparent 1px);
  background-size: 24px 24px;
  ```
- This grid background applies to **all section backgrounds** (not just skills)

---

## Cards

All content cards (skills, projects, blog posts, timeline items, contact) follow this pattern:

- **Background:** `#ffffff` (white)
- **Border:** `2.5px solid #111111` (strong black frame)
- **Border radius:** `4px` (sharp, not rounded)
- **Padding:** `1.75rem`
- **Hover effect:** `transform: translateY(-4px)` + `box-shadow: 6px 6px 0px #111111` (solid black offset shadow)
- **Transition:** `all 0.3s ease`

---

## Typography

- **Font family:** `'Inter', sans-serif`
- **Headings (h1, h2):** `#111111`, bold
- **Card titles (h3):** `#111111`, `font-weight: 700`, `font-size: 1.15rem`
- **Body text:** `#444444`, `font-size: 0.92rem`, `line-height: 1.65`
- **Secondary/muted text:** `#777777`, `font-size: 0.85rem`
- **Section titles:** centered, `#111111`

---

## Colors

| Role              | Value       | Usage                              |
|-------------------|-------------|-------------------------------------|
| Page background   | `#e8e8e8`   | All page/section backgrounds        |
| Card background   | `#ffffff`   | All cards                           |
| Border / frames   | `#111111`   | Card borders, icon backgrounds      |
| Heading text      | `#111111`   | h1, h2, h3                         |
| Body text         | `#444444`   | Paragraphs, descriptions            |
| Muted text        | `#777777`   | Secondary info, dates, subtitles    |
| Accent (primary)  | `#435fce`   | Links, highlights, gradient start   |
| Accent (secondary)| `#8616b9`   | Badges, gradient end                |

---

## Icons

- Displayed inside a square container
- **Container size:** `48px x 48px`
- **Container background:** `#111111`
- **Container border-radius:** `4px`
- **Icon color:** `#ffffff`
- **Icon size:** `28px`
- Source: Bootstrap Icons (inline SVG)

---

## Buttons

### Primary button
- **Background:** `#111111`
- **Text:** `#ffffff`
- **Border:** `2.5px solid #111111`
- **Border radius:** `4px`
- **Hover:** `box-shadow: 4px 4px 0px #111111`, `translateY(-2px)`

### Outline button
- **Background:** `transparent`
- **Text:** `#111111`
- **Border:** `2.5px solid #111111`
- **Border radius:** `4px`
- **Hover:** `background: #111111`, `color: #ffffff`

---

## Badges / Pills (tech stack, tags)

- **Background:** `#f0f0f0`
- **Text:** `#444444`
- **Border:** `1px solid #cccccc`
- **Border radius:** `4px`
- **Font size:** `0.75rem`
- **Padding:** `0.2rem 0.6rem`

---

## Hero Section

The hero uses a solid dark background — no gradients, no rounded corners:

- **Background:** `#111111` (solid black, same as navbar)
- **Text:** `#ffffff`
- **Border radius:** `0` (no rounding)
- **No hover effect** on the section itself
- **Label badge:** monospace, uppercase, `#222` background with `#333` border
- **Subtitle:** `#999999` (muted gray)

Hero buttons are inverted (white on dark):
- Primary: white background, `#111` text
- Outline: `#555` border, `#ccc` text, fills white on hover

---

## Navbar

- **Background:** `#111111` (stays dark, frames the page)
- **Text/links:** `#ffffff`
- **Active link:** slightly lighter background `#333`

---

## Footer

- **Background:** `#111111` (matches navbar)
- **Text:** `#ffffff`
- **Links:** `#ffffff`

---

## Hover & Transitions

- All interactive elements: `transition: all 0.3s ease`
- Cards hover: `translateY(-4px)` + solid black offset shadow
- Buttons hover: `translateY(-2px)` + solid black offset shadow
- No blur/glow shadows — always solid, sharp offset shadows (`Xpx Xpx 0px #111`)

---

## Layout

- **Max container width:** `1000px`
- **Grid:** Bootstrap 5 grid system
- **Card grids:** `2 columns (col-md-6)` for skills, `3 columns (col-md-4)` for projects
- **Spacing:** Bootstrap `g-4` gap between cards
- **Sections:** `padding: 4rem 0`

---

## Responsive (mobile)

- Cards stack to single column
- Skill cards: icon + text stack vertically on mobile
- Navbar collapses to hamburger menu
- Font sizes scale down naturally (no custom breakpoints needed beyond Bootstrap)

---

## What NOT to use

- No dark card backgrounds (`#1a1a1a`) — use white
- No rounded corners beyond `4px` (except hero section)
- No gradient borders or gradient text
- No blur/glow box-shadows — always solid offset
- No gradient backgrounds on cards
- No purple/blue gradient tech badges — use flat gray pills
