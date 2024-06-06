# PARTIE 1
def part_1(tableau):
    if len(tableau) < 10 and len(tableau[0]) < 10:
        for line in range(len(tableau)):
            txt = ""
            for column in range(len(tableau[line])):
                if tableau[line][column] < 10:
                    txt += f"{tableau[line][column]}   "
                else:
                    txt += f"{tableau[line][column]}  "

            print(txt)
    else:
        print("Tableau trop grand")

tableau_1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

# part_1(tableau_1)

# PARTIE 2
def part_2(num_lines, num_columns):
    n = num_lines * num_columns

    tableau_2 = []
    compteur = 1

    for i in range(num_lines):
        line = []
        for ii in range(num_columns):
            line.append(compteur)
            compteur += 1

        tableau_2.append(line)

    return tableau_2

num_tab = part_2(5, 6) #générer le tableau2
# part_1(num_tab) #afficher le tableau2 avec la fonction 1

# PARTIE 3
def part_3(num_lines, num_columns):
    tableau_3 = []
    compteur = 1

    inverse = False

    for i in range(num_lines):
        line = []
        for ii in range(num_columns):
            if inverse:
                line.insert(0, compteur)
            else:
                line.append(compteur)
            compteur += 1
        tableau_3.append(line)

        inverse = not inverse #inverse les lignes

    return tableau_3

num_tab = part_3(4, 4) #générer le tableau3
# part_1(num_tab) #afficher le tableau3 avec la fonction 1

# Avec modulo
def part_3(num_lines, num_columns):
    tableau_3 = []
    compteur = 1


    for i in range(num_lines):
        line = []
        for ii in range(num_columns):
            if i % 2 == 1:
                line.insert(0, compteur)
            else:
                line.append(compteur)
            compteur += 1
        tableau_3.append(line)


    return tableau_3

num_tab = part_3(4, 4) #générer le tableau3
# part_1(num_tab) #afficher le tableau3 avec la fonction 1

# PARTIE 4
def part_4(num_lines, num_columns):
    tableau_4 = []

    for i in range(num_lines):
        line = []
        for i in range(num_columns):
            line.append(0)
        tableau_4.append(line)

    compteur = 1
    start_line = 0
    end_line = num_lines - 1
    start_column = 0
    end_column = num_columns - 1

    while compteur <= num_lines * num_columns:

        for c in range(start_column, end_column + 1):
            tableau_4[start_line][c] = compteur
            compteur += 1

        if compteur > num_lines * num_columns:
            break

        for l in range(start_line + 1, end_line + 1):
            tableau_4[l][end_column] = compteur
            compteur += 1

        if compteur > num_lines * num_columns:
            break

        for c in range(end_column - 1, start_column - 1, -1):
            tableau_4[end_line][c] = compteur
            compteur += 1

        if compteur > num_lines * num_columns:
            break

        for l in range(end_line - 1, start_line , -1):
            tableau_4[l][start_column] = compteur
            compteur += 1

        if compteur > num_lines * num_columns:
            break

        start_line += 1
        start_column += 1
        end_line -= 1
        end_column -= 1

    return tableau_4

num_tab = part_4(6, 9) #générer le tableau4
# part_1(num_tab) #afficher le tableau4 avec la fonction 1

# PARTIE 5
ask_line = int(input("Nombre de lignes: "))
ask_column = int(input("Nombre de colonnes: "))

type_tableau = input("Quel type de tableau (N, S, E) ? ")

while type_tableau != "N" and type_tableau != "S" and type_tableau != "E":
    type_tableau = input("Quel type de tableau (N, S, E) ? ")

if type_tableau == "N":
    num_tab = part_2(ask_line, ask_column)
elif type_tableau == "S":
    num_tab = part_3(ask_line, ask_column)
elif type_tableau == "E":
    num_tab = part_4(ask_line, ask_column)

part_1(num_tab)