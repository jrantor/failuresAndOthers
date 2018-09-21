primeF = int(input())

if primeF > 1:
  for i in range(2,primeF):
    if primeF % i == 0:
      print( primeF, " is not a prime dude!")
      print(i, ' times ',primeF//i,' is ', primeF)
      break
  else:
    print("Yes, its prime!")

elif primeF==1:
  print(primeF, " is not a prime dude!")