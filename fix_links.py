import glob, re

R2 = "https://pub-39a28f27a0f9433d82dd113973c76079.r2.dev/"

for f in glob.glob("c:/Users/PC/Desktop/STBV/*.html"):
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()

    original = content

    def fix_match(m):
        attr = m.group(1)
        path = m.group(2)
        path = path.replace("\\", "/")
        return attr + '="' + R2 + path

    content = re.sub(r'(href|src)="((doc|assets)\\[^"]+)', fix_match, content)

    if content != original:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        changes = original != content
        print(f"Fixed: {f}")

print("Done")
