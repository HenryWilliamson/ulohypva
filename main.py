import math

def delka_usecky(x1, y1, x2, y2):
  """
  Vypočítá délku úsečky mezi dvěma body.

  Argumenty:
    x1, y1: Souřadnice prvního bodu (float)
    x2, y2: Souřadnice druhého bodu (float)

  Vrací:
    Délka úsečky (float)
  """
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def jsou_stejne(x1, y1, x2, y2):
  """
  Zjistí, zda se dva body shodují.

  Argumenty:
    x1, y1: Souřadnice prvního bodu (float)
    x2, y2: Souřadnice druhého bodu (float)

  Vrací:
    True, pokud se body shodují, False jinak (bool)
  """
  return abs(x1 - x2) < 1e-6 and abs(y1 - y2) < 1e-6

def lezi_na_primce(x1, y1, x2, y2, x3, y3):
  """
  Zjistí, zda bod leží na přímce dané prvními dvěma body.

  Argumenty:
    x1, y1: Souřadnice prvního bodu (float)
    x2, y2: Souřadnice druhého bodu (float)
    x3, y3: Souřadnice třetího bodu (float)

  Vrací:
    True, pokud bod leží na přímce, False jinak (bool)
  """
  return abs((x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)) < 1e-6

def main():
  """
  Hlavní funkce programu.
  """

  # Vstup souřadnic

  try:
    x1, y1 = map(float, input("Zadejte souřadnice bodu A (x, y): ").split())
    x2, y2 = map(float, input("Zadejte souřadnice bodu B (x, y): ").split())
    x3, y3 = map(float, input("Zadejte souřadnice bodu C (x, y): ").split())
  except ValueError:
    print("Některé ze zadaných souřadnic nejsou čísla.")
    return

  # Kontrola shody bodů

  if jsou_stejne(x1, y1, x2, y2) and jsou_stejne(x2, y2, x3, y3):
    print("Všechny body splývají.")
    return
  if jsou_stejne(x1, y1, x2, y2):
    print("První a druhý bod splývají.")
    return
  if jsou_stejne(x2, y2, x3, y3):
    print("Druhý a třetí bod splývají.")
    return
  if jsou_stejne(x1, y1, x3, y3):
    print("První a třetí bod splývají.")
    return

  # Kontrola, zda body leží na přímce

  if lezi_na_primce(x1, y1, x2, y2, x3, y3):
    print("Body leží na jedné přímce.")
    # Určení prostředního bodu
    if delka_usecky(x1, y1, x2, y2) > delka_usecky(x1, y1, x3, y3):
      print("Prostřední bod je:", x3, y3)
    elif delka_usecky(x2, y2, x3, y3) > delka_usecky(x1, y1, x3, y3):
      print("Prostřední bod je:", x1, y1)
    else:
      print("Prostřední bod je:", x2, y2)
  else:
    print("Body neleží na jedné přímce.")


if __name__ == "__main__":
  main()