from pyfiglet import figlet_format
print(figlet_format("TIK TAC TOE"))

grid = {
    (0, 2): " ", (1, 2): " ", (2, 2): " ",  # VIRŠUTINĖ EILUTĖ
    (0, 1): " ", (1, 1): " ", (2, 1): " ",  # VIDURINĖ EILUTĖ
    (0, 0): " ", (1, 0): " ", (2, 0): " ",  # APATINĖ EILUTĖ
}

zaidejas = "X"
ejimai = 0

laimejimo_kombinacijos = [
    # Eilutės
    [(0, 2), (1, 2), (2, 2)], [(0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0)],
    # Stulpeliai
    [(0, 2), (0, 1), (0, 0)], [(1, 2), (1, 1), (1, 0)], [(2, 2), (2, 1), (2, 0)],
    # Įstrižainės
    [(0, 2), (1, 1), (2, 0)], [(0, 0), (1, 1), (2, 2)]
]

x_laimejimai = 0
o_laimejimai = 0

while True:

    print(f"{grid[(0, 2)]} | {grid[(1, 2)]} | {grid[(2, 2)]} 2")
    print("---------")
    print(f"{grid[(0, 1)]} | {grid[(1, 1)]} | {grid[(2, 1)]} 1")
    print("---------")
    print(f"{grid[(0, 0)]} | {grid[(1, 0)]} | {grid[(2, 0)]} 0")
    print("")
    print(" 0  1  2 ")
    print("")

    try:
        ejimas_x = input(f"žaidėjas '{zaidejas}' įveskite simbolio x ašies koordinates 0/1/2: ")
        ejimas_y = input(f"žaidėjas {zaidejas} įveskite simbolio y ašies koordinates 0/1/2: ")
        x_skaicius = int(ejimas_x)
        y_skaicius = int(ejimas_y)
        if x_skaicius not in [0,1,2] or y_skaicius not in [0,1,2]:
            print("Įvesta bloga reikšmė. Tinka tik 0, 1 arba 2")
            continue
        koordinate = (x_skaicius, y_skaicius)
    except ValueError:
        print("Įvesta bloga reikšmė. Tinka tik 0, 1 arba 2")
        continue
    if grid[koordinate] == " ":
        grid[koordinate] = zaidejas
        ejimai += 1
        if zaidejas == "X":
            zaidejas = "O"
        else:
            zaidejas = "X"
    else:
        print("Langelis užimtas, parašykite koordinates iš naujo!")

#virustines eilutes tikrinimas
    if grid[(0,2)] == "X" and grid[(1,2)] == "X" and grid[(2,2)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        print(f"Rezultatas: X - {x_laimejimai} | O - {o_laimejimai}")
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(0,2)] == "O" and grid[(1,2)] == "O" and grid[(2,2)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
#vidurines eilutes tikrinimas
    if grid[(0,1)] == "X" and grid[(1,1)] == "X" and grid[(2,1)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(0,1)] == "O" and grid[(1,1)] == "O" and grid[(2,1)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
#vapatines eilutes tikrinimas
    if grid[(0,0)] == "X" and grid[(1,0)] == "X" and grid[(2,0)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(0,0)] == "O" and grid[(1,0)] == "O" and grid[(2,0)] == "O":
        print(figlet_format("LAIMĖJO O"))
        break
#pirmo stulpelio tikrinimas
    if grid[(0,2)] == "X" and grid[(0,1)] == "X" and grid[(0,0)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(0,2)] == "O" and grid[(0,1)] == "O" and grid[(0,0)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
#antro stulpelio tikrinimas
    if grid[(1,2)] == "X" and grid[(1,1)] == "X" and grid[(1,0)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(1,2)] == "O" and grid[(1,1)] == "O" and grid[(1,0)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
#trecio stulpelio tikrinimas
    if grid[(2,2)] == "X" and grid[(2,1)] == "X" and grid[(2,0)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(2,2)] == "O" and grid[(2,1)] == "O" and grid[(2,0)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
#pirmos istrizaines tikrinimas
    if grid[(0,2)] == "X" and grid[(1,1)] == "X" and grid[(2,0)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(0,2)] == "O" and grid[(1,1)] == "O" and grid[(2,0)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
#antros istrizaines tikrinimas
    if grid[(0,0)] == "X" and grid[(1,1)] == "X" and grid[(2,2)] == "X":
        print(figlet_format("LAIMĖJO X"))
        x_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą
    if grid[(0,0)] == "O" and grid[(1,1)] == "O" and grid[(2,2)] == "O":
        print(figlet_format("LAIMĖJO O"))
        o_laimejimai += 1
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą

        break
    if ejimai == 9:
        print(figlet_format("LYGIOSIOS"))
        testi = input("Ar žaisite dar kartą? (t/n): ")
        if testi.lower() == 't':
            # Nunuliname viską naujam žaidimui
            grid = {(x, y): " " for x in range(3) for y in range(3)}
            ejimai = 0
            continue  # Grįžtame į ciklo pradžią
        else:
            break  # Išjungiame žaidimą