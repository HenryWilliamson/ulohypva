def main():
  regaly = nacteni_regalu()

  seznamy = nacteni_seznamu(regaly)

  for seznam in seznamy:
    optimalizovany_seznam = optimalizuj_seznam(seznam, regaly)
    vypis_seznamu(optimalizovany_seznam)

def nacteni_regalu():
  regaly = []
  radek = input() 

  while radek:
    if radek.isdigit():
      cislo_regalu = int(radek)
      regaly.append([])
    else:
      print("Chybný formát regálu:", radek)
      exit(1)

    radek = input() 

    while radek:
      regaly[cislo_regalu].append(radek.strip())
      radek = input()

    cislo_regalu += 1

  # Kontrola sekvence čísel regálů
  if cislo_regalu != len(regaly) + 1:
    print("Nesprávná sekvence čísel regálů")
    exit(1)

  return regaly

def nacteni_seznamu(regaly):
  seznamy = []
  radek = input()

  while radek:
    seznam = []
    while radek:
      seznam.append(radek.strip().lower())
      radek = input()

    seznamy.append(seznam)

    radek = input()

  return seznamy

def optimalizuj_seznam(seznam, regaly):
  optimalizovany_seznam = []
  pozice_v_regalu = 0

  for polozka in seznam:
    nalezeno = False
    for cislo_regalu in range(pozice_v_regalu, len(regaly)):
      if polozka in regaly[cislo_regalu]:
        optimalizovany_seznam.append((polozka, cislo_regalu + 1, najdi_produkt(polozka, regaly[cislo_regalu])))
        pozice_v_regalu = cislo_regalu + 1
        nalezeno = True
        break

    if not nalezeno:
      optimalizovany_seznam.append((polozka, -1, "nenalezeno"))

  return optimalizovany_seznam

def najdi_produkt(nazev, produkty):
  for produkt in produkty:
    if nazev in produkt.lower():
      return produkt
  return produkty[0]

def vypis_seznamu(seznam):
  for polozka, cislo_regalu, produkt in seznam:
    if cislo_regalu > 0:
      print(f"{cislo_regalu}. {produkt} ({polozka})")
    else:
      print(f"** {polozka} (nenalezeno)")

if __name__ == "__main__":
  main()