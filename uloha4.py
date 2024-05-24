def analyzuj_posloupnost(cisla):
  if not cisla:
    raise ValueError("Vstupní posloupnost je prázdná.")
  if len(cisla) > 2000:
    raise ValueError("Vstupní posloupnost je příliš dlouhá (více než 2000 čísel).")
  for cislo in cisla:
    if not isinstance(cislo, int):
      raise ValueError("Neplatná hodnota v posloupnosti: {}.".format(cislo))

  soucty_intervalu = {}
  pocet_intervalu = 0  
  for levy in range(len(cisla)):
    for pravy in range(levy + 1, len(cisla)):
      soucet = sum(cisla[levy:pravy + 1])
      if soucet not in soucty_intervalu:
        soucty_intervalu[soucet] = []
      soucty_intervalu[soucet].append((levy, pravy))
      pocet_intervalu += 1

  pocet_stejnych_souctu = 0
  for soucet, intervaly in soucty_intervalu.items():
    if len(intervaly) > 1:
      for i in range(len(intervaly) - 1):
        for j in range(i + 1, len(intervaly)):
          pocet_stejnych_souctu += 1

  print("Počet nalezených intervalů:", pocet_intervalu)

  print("Počet dvojic intervalů se stejným součtem:", pocet_stejnych_souctu)

  return pocet_stejnych_souctu

cisla = [1, 5, 2, 4, 2, 2, 2]
analyzuj_posloupnost(cisla)