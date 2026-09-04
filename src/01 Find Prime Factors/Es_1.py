def get_prime_factor(n):
  prime_factors=[]
  for i in range(2,n+1):
    while n%i==0:
      prime_factors.append(i)
      n=n//i
  return prime_factors

n=int(input("Inserire un numero n: "))
print("I suoi fattori primi sono: ", get_prime_factor(n)) 