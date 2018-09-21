def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

n = int(input())
    
string = str(factorial(n))
sum = 0 
for i in range(0,len(string)):
  sum += int(string[i])
print(sum)