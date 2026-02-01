#!/usr/bin/env python3
"""
Generate docs/index.html by indexing all post folders in docs/posts/.
"""

import os
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


def get_post_folders():
    """Return sorted list of post folder names in docs/posts/."""
    if not POSTS_DIR.exists():
        return []
    folders = [
        d.name for d in POSTS_DIR.iterdir()
        if d.is_dir() and (d / "index.html").exists()
    ]
    return sorted(folders, reverse=True)


def generate_index():
    """Generate the docs/index.html file."""
    folders = get_post_folders()

    if not folders:
        post_links = "<li>No posts yet.</li>"
    else:
        post_links = "\n".join(
            f'<li><a href="posts/{folder}/">{folder}</a></li>'
            for folder in folders
        )

    html = HTML_TEMPLATE.format(post_links=post_links)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(html)
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_index()
