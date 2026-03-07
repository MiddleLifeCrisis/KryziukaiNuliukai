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

    ejimasX_x = input(f"žaidėjas '{zaidejas}' įveskite simbolio x ašies koordinates 0/1/2: ")
    ejimasX_y = input(f"žaidėjas {zaidejas} įveskite simbolio y ašies koordinates 0/1/2: ")
    x_skaicius = int(ejimasX_x)
    y_skaicius = int(ejimasX_y)

    koordinate = (x_skaicius, y_skaicius)

    if grid[koordinate] == " ":
        grid[koordinate] = zaidejas
        if zaidejas == "X":
            zaidejas = "O"
        else:
            zaidejas = "X"
    else:
        print("Langelis užimtas, parašykite koordinates iš naujo!")

    print(f"{grid[(0,2)]} | {grid[(1,2)]} | {grid[(2,2)]} 2")
    print("---------")
    print(f"{grid[(0,1)]} | {grid[(1,1)]} | {grid[(2,1)]} 1")
    print("---------")
    print(f"{grid[(0,0)]} | {grid[(1,0)]} | {grid[(2,0)]} 0")
    print("")
    print(" 0  1  2 ")
    print("")

#virustines eilutes tikrinimas
    if grid[(0,2)] == "X" and grid[(1,2)] == "X" and grid[(2,2)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(0,2)] == "O" and grid[(1,2)] == "O" and grid[(2,2)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
#vidurines eilutes tikrinimas
    if grid[(0,1)] == "X" and grid[(1,1)] == "X" and grid[(2,1)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(0,1)] == "O" and grid[(1,1)] == "O" and grid[(2,1)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
#vapatines eilutes tikrinimas
    if grid[(0,0)] == "X" and grid[(1,0)] == "X" and grid[(2,0)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(0,1)] == "O" and grid[(1,0)] == "O" and grid[(2,0)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
#pirmo stulpelio tikrinimas
    if grid[(0,2)] == "X" and grid[(0,1)] == "X" and grid[(0,0)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(0,2)] == "O" and grid[(1,2)] == "O" and grid[(2,2)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
#antro stulpelio tikrinimas
    if grid[(1,2)] == "X" and grid[(1,1)] == "X" and grid[(1,0)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(1,2)] == "O" and grid[(1,1)] == "O" and grid[(1,0)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
#trecio stulpelio tikrinimas
    if grid[(2,2)] == "X" and grid[(2,1)] == "X" and grid[(2,0)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(2,2)] == "O" and grid[(2,1)] == "O" and grid[(2,0)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
#pirmos istrizaines tikrinimas
    if grid[(0,2)] == "X" and grid[(1,1)] == "X" and grid[(2,0)] == "X":
        print("Laimėjo žaidėjas 'X'")
        break
    if grid[(0,2)] == "O" and grid[(1,1)] == "O" and grid[(2,0)] == "O":
        print("Laimėjo žaidėjas 'O'")
        break
    else:
        print("Lygiosios")