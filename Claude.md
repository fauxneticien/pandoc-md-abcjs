# Claude.md

## Project Overview

This is a proof-of-concept for writing about music in Markdown using ABC notation. It uses Pandoc to convert Markdown documents containing ABC music notation into interactive HTML with rendered sheet music and audio playback capabilities.

The primary use case is writing prose about music (e.g., Irish folk music, fiddle, tenor banjo) with embedded, playable music examples.

## Tech Stack

- **Pandoc** - Document converter (external system dependency)
- **ABC Notation** - Text-based music notation format
- **abcjs v6.6.0** - JavaScript library for rendering ABC notation (loaded from CDN)
- **Lua** - Pandoc filter scripting
- **Vanilla JavaScript** - Client-side interactivity (no build system)

## Project Structure

```
├── index.md              # Example input markdown with ABC notation
├── index.html            # Generated HTML output
├── template.html         # Pandoc HTML template
├── abcjs-helpers.js      # JavaScript for rendering and playback
├── abcjs-passthrough.lua # Pandoc filter for ABC code blocks
└── README.md             # Project documentation
```

## Key Files

| File | Purpose |
|------|---------|
| `abcjs-helpers.js` | Core JavaScript that renders ABC notation to SVG, handles audio playback, cursor tracking, and interactive features |
| `abcjs-passthrough.lua` | Lua filter that preserves `abcjs` code blocks as raw HTML divs |
| `template.html` | HTML5 template including abcjs library, styles, and script loading |

## Build Command

```bash
pandoc index.md \
  -o index.html \
  --standalone \
  --from markdown \
  --to html5 \
  --template=template.html \
  --lua-filter=abcjs-passthrough.lua
```

## Dependencies

- **Pandoc** must be installed on the system
- **abcjs** is loaded from CDN (no npm/package.json)

## Development Notes

- No build system, transpiler, or package manager - this is intentionally minimal
- No automated tests
- The JavaScript in `abcjs-helpers.js` runs on page load and processes all `abcjs` code blocks
- ABC notation blocks in Markdown should use the `abcjs` language identifier in fenced code blocks
