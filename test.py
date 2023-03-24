s = input("Introduceți un șir: ")

# Calculează lungimea șirului
l = len(s)

# Verificați dacă lungimea șirului este impară
if l % 2 == 0:
    # Dacă lungimea șirului este impară, accesați caracterul din mijloc prin indexare
    m = s[l // 2]
    print("Caracterul din mijloc este:", m)
else:
    print("Lungimea șirului trebuie să fie impară.")