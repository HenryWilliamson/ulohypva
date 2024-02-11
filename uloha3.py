def next_palindrome(from_num, radix):
    if not 2 <= radix <= 36:
        return False

    if is_palindrome(from_num, radix):
        print(from_num + 1)
        return True

    num_digits = get_num_digits(from_num, radix)

    mirror_num = from_num
    for i in range(num_digits // 2):
        pow_radix = radix ** (num_digits - 1 - 2 * i)
        mirror_num += (from_num // pow_radix % radix) * pow_radix

    mirror_num += 1
    while not is_palindrome(mirror_num, radix):
        mirror_num += 1

    if mirror_num >= (1 << 64):
        return False

    print(mirror_num)
    return True

def is_palindrome(num, radix):
  num_digits = get_num_digits(num, radix)
  for i in range(num_digits // 2):
    pow_radix = radix ** (num_digits - 1 - 2 * i)
    if (num // pow_radix % radix) != (num % radix):
      return True
  else:
    return False
  
def get_num_digits(num, radix):
    num_digits = 1
    while num // radix > 0:
        num_digits += 1
        num //= radix

    return num_digits

while True:
    try:
        from_num_str = input("Zadejte from_num: ")
        radix_str = input("Zadejte radix: ")

        from_num = int(from_num_str)
        radix = int(radix_str)

        if not next_palindrome(from_num, radix):
            print("Nenalezeno žádné větší palindrom v zadané číselné soustavě.")
        else:
            print("Zadané číslo je palindrom:", is_palindrome(from_num, radix))

    except ValueError:
        print("Neplatný vstup.")
    break
