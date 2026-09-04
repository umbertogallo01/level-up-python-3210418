def sort_words(s):
  l = s.split()
  l = sorted(l, key=str.lower)
  return " ".join(l)

s = input("Inserire una stringa: ")
print(sort_words(s))