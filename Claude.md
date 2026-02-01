# Claude.md

## Project Overview

This is a proof-of-concept for writing about music in Markdown using ABC notation. It uses Pandoc to convert Markdown documents containing ABC music notation into interactive HTML with rendered sheet music and audio playback capabilities.

The primary use case is writing prose about music (e.g., Irish folk music, fiddle, tenor banjo) with embedded, playable music examples.

## Tech Stack

- **Pandoc** - Document converter (external system dependency)
- **ABC Notation** - Text-based music notation format
- **abcjs v6.6.0** - JavaScript library for rendering ABC notation (loaded from CDN)
- **Lua** - Pandoc filter scripting
- **ES Modules** - Client-side plugin architecture (no build system)

## Project Structure

```
├── pandoc/                    # Pandoc templates and filters
│   ├── template.html          # HTML5 template
│   ├── passthrough.lua        # Generic passthrough filter for plugins
│   └── generate_index.py      # Index page generator
│
├── docs/                      # Served content (GitHub Pages)
│   ├── plugins/
│   │   ├── main.js            # Plugin entry point (ES module)
│   │   └── abcjs/             # ABC music notation plugin
│   │       ├── abcjs.js
│   │       ├── abcjs.css
│   │       └── manifest.json
│   ├── posts/                 # Blog posts
│   │   └── YYYY-MM-DD/
│   │       ├── index.md       # Source
│   │       └── index.html     # Generated
│   └── index.html             # Post index
│
├── taskfile.yaml              # Build tasks
└── README.md
```

## Key Files

| File | Purpose |
|------|---------|
| `pandoc/passthrough.lua` | Lua filter that passes through code blocks for client-rendered plugins |
| `pandoc/template.html` | HTML5 template with CDN deps and plugin script loading |
| `docs/plugins/main.js` | ES module entry point that imports and initializes plugins |
| `docs/plugins/abcjs/abcjs.js` | ABC notation rendering, audio playback, cursor tracking |

## Build Command

```bash
pandoc docs/posts/2026-01-24/index.md \
  -o docs/posts/2026-01-24/index.html \
  --standalone \
  --from markdown \
  --to html5 \
  --template=pandoc/template.html \
  --lua-filter=pandoc/passthrough.lua
```

## Dependencies

- **Pandoc** must be installed on the system
- **abcjs** is loaded from CDN (no npm/package.json)
- **Task** (go-task) for build automation (optional)

## Development Notes

- No build system, transpiler, or package manager - intentionally minimal
- Plugins use ES modules with `export default`
- Add new plugins by:
  1. Creating `docs/plugins/<name>/<name>.js`
  2. Adding to `plugins` array in `pandoc/passthrough.lua`
  3. Importing in `docs/plugins/main.js`
