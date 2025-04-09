import random
moznosti = ["rohlík", "párek", "koloběžka", "šunka", "perník"]
for _ in range(10):
    osoba1_volba = random.choice(moznosti)
    osoba2_volba = random.choice(moznosti)
    print(f"- Kupme {osoba1_volba}.")
    if osoba1_volba == osoba2_volba:
        jina_volba = random.choice([item for item in moznosti if item != osoba1_volba])
        print(f"- Ne, kupme jiný {jina_volba}.")
    else:
        print(f"- Ne, kupme {osoba2_volba}.")