/**
 * Plugin Loader
 * Imports and initializes all active plugins
 */

import abcjs from './abcjs/abcjs.js';

const plugins = [
  abcjs,
  // Add new plugins here:
  // import mermaid from './mermaid/mermaid.js';
];

// Initialize all plugins on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  plugins.forEach(plugin => {
    plugin.init();
  });
});
