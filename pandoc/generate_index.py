#!/usr/bin/env python3
"""
Generate docs/index.html by indexing all post folders in docs/posts/.
"""

import os
import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"
POSTS_DIR = DOCS_DIR / "posts"
OUTPUT_FILE = DOCS_DIR / "index.html"

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Posts</title>
<style>
body {{
    font-family: sans-serif;
    max-width: 800px;
    margin: 2em auto;
    padding: 0 1em;
}}
h1 {{
    border-bottom: 1px solid #ccc;
    padding-bottom: 0.5em;
}}
ul {{
    list-style: none;
    padding: 0;
}}
li {{
    margin: 0.5em 0;
}}
a {{
    color: #0066cc;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
</style>
</head>
<body>
<h1>Posts</h1>
<ul>
{post_links}
</ul>
</body>
</html>
"""


def extract_title(md_path):
    """Extract title from YAML front matter of a markdown file."""
    if not md_path.exists():
        return None
    content = md_path.read_text()
    # Match YAML front matter between --- delimiters
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    front_matter = match.group(1)
    # Extract title from front matter
    title_match = re.search(r'^title:\s*(.+)$', front_matter, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    return None


def get_post_folders():
    """Return sorted list of (folder_name, title) tuples for posts in docs/posts/."""
    if not POSTS_DIR.exists():
        return []
    posts = []
    for d in POSTS_DIR.iterdir():
        if d.is_dir() and (d / "index.html").exists():
            title = extract_title(d / "index.md")
            posts.append((d.name, title))
    return sorted(posts, key=lambda x: x[0], reverse=True)


def generate_index():
    """Generate the docs/index.html file."""
    posts = get_post_folders()

    if not posts:
        post_links = "<li>No posts yet.</li>"
    else:
        links = []
        for folder, title in posts:
            if title:
                links.append(f'<li><a href="posts/{folder}/">{folder} - {title}</a></li>')
            else:
                links.append(f'<li><a href="posts/{folder}/">{folder}</a></li>')
        post_links = "\n".join(links)

    html = HTML_TEMPLATE.format(post_links=post_links)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html)
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_index()
