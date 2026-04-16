import re

COMPACT_FOOTER = '''    <footer class="bg-emerald-900 text-white pt-10 pb-6 border-t-4 border-gold-500">
        <div class="container mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4 mb-4">
                <div class="flex flex-wrap items-center gap-4 text-sm text-emerald-100">
                    <span><i class="fas fa-map-marker-alt text-gold-500 mr-1"></i> Ақтөбе қ., Жастар ш.а., 3-ш.а., 13А ст.</span>
                    <span><i class="fas fa-phone text-gold-500 mr-1"></i> 8 (7132) 46-11-77</span>
                    <span><i class="fas fa-envelope text-gold-500 mr-1"></i> ksatbaevoml@yandex.kz</span>
                </div>
                <a href="https://www.instagram.com/satbayev_lyceum" target="_blank" class="hover:text-gold-500 transition"><i class="fab fa-instagram text-xl"></i></a>
            </div>
            <div class="border-t border-emerald-800 pt-4 text-center text-sm text-emerald-400 flex flex-col md:flex-row justify-between items-center">
                <p>&copy; 2025 Қ.Сәтбаев атындағы мектеп-лицей. Барлық құқықтар қорғалған.</p>
                <p class="mt-2 md:mt-0 text-xs">Осы мектеп түлегі Елдосұлы Сүлеймен жасады</p>
            </div>
        </div>
    </footer>'''

files = [
    "c:/Users/PC/Desktop/STBV/admin.html",
    "c:/Users/PC/Desktop/STBV/achievements.html",
    "c:/Users/PC/Desktop/STBV/upbringing.html",
    "c:/Users/PC/Desktop/STBV/education.html",
    "c:/Users/PC/Desktop/STBV/billim.html",
    "c:/Users/PC/Desktop/STBV/community.html",
    "c:/Users/PC/Desktop/STBV/services.html",
    "c:/Users/PC/Desktop/STBV/alumni.html",
]

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()

    new_content = re.sub(
        r'    <footer class="[^"]*">.*?</footer>',
        COMPACT_FOOTER,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(new_content)
        print(f"Updated: {f}")
    else:
        print(f"No change: {f}")

print("Done")
