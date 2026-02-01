# Plugins

This directory contains modular plugins for rendering domain-specific content in Markdown posts.

## Plugin Structure

Each plugin is a self-contained directory with the following files:

```
plugins/<plugin-name>/
├── manifest.json    # Plugin metadata and dependencies
├── <plugin>.js      # Client-side rendering code
└── <plugin>.css     # Plugin-specific styles
```

## manifest.json

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "What this plugin does",
  "codeblock": "plugin-name",     // The code fence language identifier
  "rendering": "client",          // "client" or "server"
  "cdn": [                        // External dependencies
    { "type": "script", "src": "https://..." },
    { "type": "stylesheet", "href": "https://..." }
  ],
  "entrypoint": "plugin.js",      // Main JavaScript file
  "styles": "plugin.css"          // CSS file (optional)
}
```

## Creating a New Plugin

1. Create a new directory: `plugins/<your-plugin>/`
2. Create `manifest.json` with plugin metadata
3. Create `<plugin>.js` that registers with `window.MarkdownPlugins`
4. Create `<plugin>.css` for styles (optional)
5. Add the plugin name to `plugins.yaml`
6. Copy assets to `docs/js/` and `docs/css/`

## JavaScript Plugin Pattern

Plugins register themselves with the global `MarkdownPlugins` object:

```javascript
(function() {
  window.MarkdownPlugins = window.MarkdownPlugins || {};

  window.MarkdownPlugins.yourplugin = {
    name: 'yourplugin',

    render: function(codeEl, idx) {
      // codeEl: the <code> element containing the content
      // idx: unique index for generating IDs
      // Transform codeEl.textContent and replace the parent <pre>
    },

    init: function() {
      document.querySelectorAll("pre code.yourplugin").forEach((el, idx) => {
        this.render(el, idx);
      });
    }
  };

  document.addEventListener("DOMContentLoaded", function() {
    window.MarkdownPlugins.yourplugin.init();
  });
})();
```

## Rendering Modes

- **client**: Content is passed through by Lua filter and rendered in browser
- **server**: Custom Lua filter processes content at build time (e.g., tikz)

## Available Plugins

| Plugin | Description | Rendering |
|--------|-------------|-----------|
| abcjs  | ABC music notation with audio playback | client |
