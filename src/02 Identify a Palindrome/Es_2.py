import re

def is_plindrome(s):
  prompt = ''.join(re.findall(r'[a-z]+', s.lower()))
  if prompt==prompt[::-1]:
    return True
  else:
    return False

s=input("Inserire una stringa: ")
if is_plindrome(s):
  print("La stringa è palindroma!")
else:
  print("La stringa non è palindroma!")