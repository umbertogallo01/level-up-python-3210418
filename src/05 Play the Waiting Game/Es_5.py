import random
import time

def waiting_game():
  target = random.randint(2,4)
  print(f"Il tempo target è {target : .3f} secondi")

  input("Premer Enter per far partire il cronometro")
  start=time.perf_counter()

  input("Ripremere Enter per bloccare il cronometro")
  diff = time.perf_counter()-start

  if diff == target:
    print("Hai vinto!")
  elif diff<target:
    print(f"Sei stato {diff : .3f} secondi più veloce!")
  else:
    print(f"Sei stato {diff : .3f} secondi più lento!")

waiting_game()
