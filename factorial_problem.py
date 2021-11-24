
# by using normal function
def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result


j= factorial(5)
print(j)
# by using recursive function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

j = factorial(5)
print(j)



