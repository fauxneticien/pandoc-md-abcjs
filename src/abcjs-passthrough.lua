function CodeBlock(cb)
  if cb.classes:includes("abcjs") then
    return pandoc.RawBlock("html",
      "<pre><code class=\"abcjs\">" .. cb.text .. "</code></pre>"
    )
  end
end
