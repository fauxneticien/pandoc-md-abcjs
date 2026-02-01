# Pandoc

This directory contains pandoc templates and filters for converting Markdown to HTML.

## Files

### `passthrough.lua`

A Pandoc Lua filter that passes through code blocks for client-rendered plugins. Code blocks with classes matching registered plugins (e.g., `abcjs`, `mermaid`) are output as `<pre><code class="...">` HTML, preserving the content for browser-side rendering.

To add a new plugin, add its class name to the `plugins` table:

```lua
local plugins = {
  "abcjs",
  "mermaid",  -- add new plugins here
}
```

### `template.html`

The Pandoc HTML5 template that defines the output structure. It includes:
- CDN references for plugin dependencies (e.g., abcjs library)
- Plugin stylesheets from `docs/plugins/<name>/<name>.css`
- ES module script loading `docs/plugins/main.js`

### `generate_index.py`

Generates `docs/index.html` by scanning `docs/posts/` for post directories and creating a chronological index page.

## Build Process

```
docs/posts/*/index.md  -->  pandoc + passthrough.lua + template.html  -->  docs/posts/*/index.html
                                                                                    |
                                                                                    v
                                                                        docs/plugins/main.js (browser)
                                                                                    |
                                                                                    v
                                                                        docs/plugins/<name>/<name>.js
```
