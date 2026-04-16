import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_name in html_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Attempt to reverse the CP1251 to UTF-8 mojibake
    try:
        # Strip BOM if present
        if content.startswith('\ufeff'):
            content = content[1:]
            
        # The content has characters like 'РњРµРє'. These are actual unicode characters in the string.
        # We need to get the raw bytes by encoding to cp1251, then decode as utf-8
        restored_content = content.encode('cp1251').decode('utf-8')
        
        # Add the BOM back if the original had it (optional, but let's just use regular utf-8)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(restored_content)
        print(f"Successfully restored {file_name}")
    except Exception as e:
        print(f"Failed to restore {file_name}: {e}")
