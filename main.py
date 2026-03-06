#parodyti TIC TAC TOE Logo
from urllib.parse import splitquery

from pyfiglet import figlet_format


print(figlet_format("TIK TAC TOE"))

grid = {
    (0, 2): " ", (1, 2): " ", (2, 2): " ",  # VIRŠUTINĖ EILUTĖ
    (0, 1): " ", (1, 1): " ", (2, 1): " ",  # VIDURINĖ EILUTĖ
    (0, 0): " ", (1, 0): " ", (2, 0): " ",  # APATINĖ EILUTĖ
}

print(f"{grid[(0,0)]} | {grid[(1,0)]} | {grid[(2,0)]}  2")
print("---------")
print(f"{grid[(0,1)]} | {grid[(1,1)]} | {grid[(2,1)]}  1")
print("---------")
print(f"{grid[(0,2)]} | {grid[(1,2)]} | {grid[(2,2)]}  0")
print("")
print(" 0  1  2 ")


# isiminti simbolio kordinate


# prasyti user 2 ivesti kordinates
# isiminti simbolio kordinate
# parodyti gride priskirta simoboli ir pries tai buvusius simbolius

# patikrinti ar neatsirado laimetojas

grid = {
    (0, 2): " ", (1, 2): " ", (2, 2): " ",  # VIRŠUTINĖ EILUTĖ
    (0, 1): " ", (1, 1): " ", (2, 1): " ",  # VIDURINĖ EILUTĖ
    (0, 0): " ", (1, 0): " ", (2, 0): " ",  # APATINĖ EILUTĖ
}

ejimasX_x = input("Įveskite kordinates x (0-2): ")
ejimasX_y = input("Įveskite kordinates y (0-2): ")
x_skaicius = int(ejimasX_x)
y_skaicius = int(ejimasX_y)

koordinate = (x_skaicius, y_skaicius)

grid[koordinate] = "X"

print(f"{grid[(0,2)]} | {grid[(1,2)]} | {grid[(2,2)]}")
print("---------")
print(f"{grid[(0,1)]} | {grid[(1,1)]} | {grid[(2,1)]}")
print("---------")
print(f"{grid[(0,0)]} | {grid[(1,0)]} | {grid[(2,0)]}")





# if grid["0,"] == thisdict["b1"]:
#     print("True")
# else:
#     print("False")

# kartoti kol neatsiranda laimetojas

# paskelbti nugaletoja
# paskbelti nugaletoju list pagal best taskus ever
# prideti mano reklama