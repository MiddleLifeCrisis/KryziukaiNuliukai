from urllib.parse import splitquery

from pyfiglet import figlet_format


print(figlet_format("TIK TAC TOE"))

grid = {
    (0, 2): " ", (1, 2): " ", (2, 2): " ",  # VIRŠUTINĖ EILUTĖ
    (0, 1): " ", (1, 1): " ", (2, 1): " ",  # VIDURINĖ EILUTĖ
    (0, 0): " ", (1, 0): " ", (2, 0): " ",  # APATINĖ EILUTĖ
}

print(f"{grid[(0, 2)]} | {grid[(1, 2)]} | {grid[(2, 2)]} 2")
print("---------")
print(f"{grid[(0, 1)]} | {grid[(1, 1)]} | {grid[(2, 1)]} 1")
print("---------")
print(f"{grid[(0, 0)]} | {grid[(1, 0)]} | {grid[(2, 0)]} 0")
print("")
print(" 0  1  2 ")
print("")

zaidejas = "X"

while True:

    ejimasX_x = input(f"žaidėjas {zaidejas} įveskite kordinates x (0-2): ")
    ejimasX_y = input(f"žaidėjas {zaidejas} Įveskite kordinates y (0-2): ")
    x_skaicius = int(ejimasX_x)
    y_skaicius = int(ejimasX_y)

    koordinate = (x_skaicius, y_skaicius)

    if grid[koordinate] == " ":
        grid[koordinate] = zaidejas
    else:
        print("Langelis užimtas, parašykite kordinates iš naujo")

    print(f"{grid[(0,2)]} | {grid[(1,2)]} | {grid[(2,2)]} 2")
    print("---------")
    print(f"{grid[(0,1)]} | {grid[(1,1)]} | {grid[(2,1)]} 1")
    print("---------")
    print(f"{grid[(0,0)]} | {grid[(1,0)]} | {grid[(2,0)]} 0")
    print("")
    print(" 0  1  2 ")
    print("")

    if zaidejas == "X":
        zaidejas = "O"
    else:
        zaidejas = "X"

