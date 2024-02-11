import math

def main(a):

  if a <= 0:
    print("Velikost místnosti musí být kladná.")
    return

  try:
    x1, y1, z1 = map(float, input("Zadejte souřadnice prvního bodu (x, y, z): ").split())
    x2, y2, z2 = map(float, input("Zadejte souřadnice druhého bodu (x, y, z): ").split())
  except ValueError:
    print("Některé ze zadaných souřadnic nejsou čísla.")
    return

  if not (0 <= x1 <= a and 0 <= y1 <= a and 0 <= z1 <= a):
    print("První bod neleží v žádné stěně/stropu/podlaze.")
    return
  if not (0 <= x2 <= a and 0 <= y2 <= a and 0 <= z2 <= a):
    print("Druhý bod neleží v žádné stěně/stropu/podlaze.")
    return
 

  d1 = abs(x1 - x2)
  d2 = abs(y1 - y2)
  d3 = abs(z1 - z2)
  delka_trubiek = d1 + d2 + d3

  delka_hadice = math.sqrt((d1**2 + d2**2 + d3**2))

  print("Délka trubek:", delka_trubiek)
  print("Délka hadice:", delka_hadice)


if __name__ == "__main__":
  a = int(input("Zadejte velikost místnosti (a): "))
  main(a)