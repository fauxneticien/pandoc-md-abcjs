# Source Files

This directory contains the core processing scripts and templates used to convert Markdown with ABC music notation into interactive HTML.

## Files

### `abcjs-passthrough.lua`
A Pandoc Lua filter that intercepts code blocks with the `abcjs` class during markdown-to-HTML conversion. It wraps the ABC notation content as `<pre><code class="abcjs">` HTML, preventing Pandoc from escaping or modifying the notation.

### `abcjs-helpers.js`
Client-side JavaScript that runs when the generated HTML page loads. It:
- Finds all `<pre><code class="abcjs">` blocks created by Pandoc
- Renders them as interactive SVG sheet music using the abcjs library
- Adds playback controls (play, pause, loop, tempo)
- Displays cursor tracking during playback
- Provides tablature toggle for violin fingering

### `template.html`
The Pandoc HTML5 template that defines the output structure for generated pages. It includes:
- References to the abcjs library (CDN)
- CSS styles for music notation display
- Reference to `abcjs-helpers.js` for client-side rendering
