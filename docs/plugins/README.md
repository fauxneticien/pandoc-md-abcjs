# Plugins

This directory contains modular plugins for rendering domain-specific content in Markdown posts.

## Directory Structure

```
docs/plugins/
├── main.js              # Entry point - imports and initializes all plugins
├── README.md            # This file
└── <plugin-name>/
    ├── <plugin>.js      # ES module with default export
    ├── <plugin>.css     # Plugin-specific styles
    └── manifest.json    # Plugin metadata (optional)
```

## Creating a New Plugin

1. Create a new directory: `docs/plugins/<your-plugin>/`
2. Create `<plugin>.js` as an ES module with a default export
3. Create `<plugin>.css` for styles (optional)
4. Import and register in `main.js`

## Plugin Interface

Each plugin exports a default object with this interface:

```javascript
export default {
  name: 'yourplugin',
  selector: 'pre code.yourplugin',  // CSS selector for content blocks

  render(codeEl, idx) {
    // codeEl: the <code> element containing the content
    // idx: unique index for generating IDs
    // Transform codeEl.textContent and replace the parent <pre>
  },

  init() {
    document.querySelectorAll(this.selector).forEach((el, idx) => {
      this.render(el, idx);
    });
  }
};
```

## Registering a Plugin

In `main.js`, import and add to the plugins array:

```javascript
import abcjs from './abcjs/abcjs.js';
import mermaid from './mermaid/mermaid.js';

const plugins = [
  abcjs,
  mermaid,
];
```

## Rendering Modes

- **client**: Content is passed through by Lua filter and rendered in browser (most plugins)
- **server**: Custom Lua filter processes content at build time (e.g., tikz)

## Available Plugins

| Plugin | Description | Rendering |
|--------|-------------|-----------|
| abcjs  | ABC music notation with audio playback | client |
