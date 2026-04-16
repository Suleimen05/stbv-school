import glob

FULL_NAME = "Қаныш Сәтбаев атындағы орта мектеп-лицей"
FULL_NAME_UPPER = "ҚАНЫШ СӘТБАЕВ АТЫНДАҒЫ ОРТА МЕКТЕП-ЛИЦЕЙ"

replacements = [
    # Title tags
    ("Тәрбие үдерісі - Мектеп-Лицей", f"Тәрбие үдерісі - {FULL_NAME}"),
    ("Инфрақұрылым - Мектеп-Лицей", f"Инфрақұрылым - {FULL_NAME}"),
    ("Мектеп-Лицей - Басты бет", f"{FULL_NAME} - Басты бет"),
    ("Жетістіктер галереясы - Мектеп-Лицей", f"Жетістіктер галереясы - {FULL_NAME}"),
    ("Әкімшілік бөлім - Мектеп-Лицей", f"Әкімшілік бөлім - {FULL_NAME}"),
    ("Түлектер тақтасы - Мектеп-Лицей", f"Түлектер тақтасы - {FULL_NAME}"),
    ("Қоғамдастық және Серіктестік - Мектеп-Лицей", f"Қоғамдастық және Серіктестік - {FULL_NAME}"),
    ("Білімді жаңарту - Мектеп-Лицей", f"Білімді жаңарту - {FULL_NAME}"),
    ("Білім беру - Мектеп-Лицей", f"Білім беру - {FULL_NAME}"),

    # Navbar headers (uppercase in span)
    ('>МЕКТЕП-ЛИЦЕЙ<', f'>{FULL_NAME_UPPER}<'),

    # index.html navbar (two-line version)
    ('>Қ.Сәтбаев атындағы<', f'>Қаныш Сәтбаев атындағы<'),
    ('>Мектеп-лицей<', '>орта мектеп-лицей<'),

    # index.html footer logo
    ('Қ.Сәтбаев атындағы<br>мектеп-лицей', 'Қаныш Сәтбаев атындағы<br>орта мектеп-лицей'),

    # Footer copyright (all pages)
    ('Қ.Сәтбаев атындағы мектеп-лицей', FULL_NAME),

    # index.html timeline text
    ('"Мектеп-Лицей" мәртебесіне', '"Орта мектеп-лицей" мәртебесіне'),
]

for f in glob.glob("c:/Users/PC/Desktop/STBV/*.html"):
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()

    original = content
    for old, new in replacements:
        content = content.replace(old, new)

    if content != original:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Updated: {f}")

print("Done")
