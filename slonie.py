ile_sloni = int(input("Ile ma byc sloni: "))
waga = list(map(int, input("Podaj wagi sloni po spacji (pierwsza podana to waga 1 slonia): ").split()[:ile_sloni]))
waga1 = waga[:]
jak_stoja = list(map(int, input("Podaj poczatkowe ustawienie sloni po spacji: ").split()[:ile_sloni]))
jak_maja = list(map(int, input("Podaj docelowe ustawienie sloni po spacji: ").split()[:ile_sloni]))

potrzebna_sila = 0
x = min(waga)
min_index = waga.index(x)
min_index += 1
run = True
while run:
    for i in range(len(jak_stoja)):
        if jak_stoja[i] == min_index:
            if jak_stoja[i] != jak_maja[i]:
                p = jak_stoja[i]
                for j in range(len(jak_stoja)):
                    if jak_stoja[j] == jak_maja[i]:

                        jak_stoja[i] = jak_maja[i]
                        potrzebna_sila += waga[min_index - 1]
                        jak_stoja[j] = p
                        potrzebna_sila += waga[jak_stoja[i] - 1]
                        break
            else:
                waga1.remove(x)
                x = min(waga1)
                min_index = waga.index(x)
                min_index += 1

    if jak_stoja == jak_maja:
        run = False

print(potrzebna_sila)
