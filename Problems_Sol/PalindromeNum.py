#checking wherther a number is palindrome or not

def rev_num(num):
    rev = 0
    while(num>0):
        i = num % 10
        rev = rev*10 + i
        num = num // 10
    return rev

n = int(input())
r = rev_num(n)
if (n==r):
    print('Number is Palindrome.')
else:
    print('Sorry buddy, it is not')

