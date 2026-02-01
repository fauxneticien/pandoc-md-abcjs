-- Passthrough filter for client-rendered plugins
-- Code blocks with these classes are passed through unchanged for browser rendering

local plugins = {
  "abcjs",
  -- Add new plugins here:
  -- "mermaid",
  -- "katex",
}

-- Build lookup table for O(1) checks
local plugin_set = {}
for _, name in ipairs(plugins) do
  plugin_set[name] = true
end

function CodeBlock(cb)
  for _, class in ipairs(cb.classes) do
    if plugin_set[class] then
      return pandoc.RawBlock("html",
        '<pre><code class="' .. class .. '">' .. cb.text .. '</code></pre>'
      )
    end
  end
end
