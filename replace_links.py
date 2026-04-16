import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
prefix = "https://pub-39a28f27a0f9433d82dd113973c76079.r2.dev/"

for file_name in html_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace local relative paths with the Cloudflare prefix
    content = content.replace('="doc/', f'="{prefix}doc/')
    content = content.replace('="assets/', f'="{prefix}assets/')
    content = content.replace('="assetss/', f'="{prefix}assetss/')

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file_name}")
