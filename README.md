# ❌ Tic-Tac-Toe (Kryžiukai-Nuliukai) ⭕

Tai mano pirmasis Python programavimo projektas – klasikinio žaidimo terminalinė versija. Žaidimas sukurtas mokantis Python pagrindų, duomenų struktūrų ir loginio srauto valdymo.

## 🚀 Funkcijos

* **Interaktyvi lenta:** Žaidimas vyksta 3x3 tinklelyje naudojant koordinačių sistemą.
* **Laimėjimo patikra:** Programa tikrina 16 galimų laimėjimo kombinacijų (eilutės, stulpeliai, įstrižainės).
* **Sesijos taškai:** Žaidimas skaičiuoja, kiek kartų laimėjo „X“ ir kiek „O“ per visą sesiją.
* **Klaidų valdymas:** Integruota `try-except` logika apsaugo nuo programos lūžimo įvedus neteisingus duomenis.
* **Revanšo galimybė:** Po kiekvienos partijos žaidėjai gali pasirinkti žaisti iš naujo arba išeiti.
* **ASCII Menas:** Naudojama `pyfiglet` biblioteka stilingiems laimėjimo pranešimams.

## 🛠️ Technologijos

* **Kalba:** Python 3
* **Bibliotekos:** `pyfiglet`, `os`
* **Duomenų struktūros:** `Dictionary` (tinkleliui), `List` (kombinacijoms), `Tuple` (koordinatėms).

## 🎮 Kaip paleisti

1. Įsitikinkite, kad turite įdiegtą Python ir `pyfiglet` biblioteką:
   ```bash
   pip install pyfiglet
   
2. Paleiskite žaidimą:

Bash
python main.py

📈 Ateities planai (Roadmap)
Šis projektas bus evoliucionuojamas:

[ ] Sukurti grafinę sąsają (GUI) naudojant Django.

[ ] Integruoti SQL duomenų bazę rezultatų saugojimui.

[ ] Pridėti galimybę žaisti prieš kompiuterį (AI).

Sukūrė: [Justas osipovas]