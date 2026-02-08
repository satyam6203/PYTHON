# recurtion is the funtion that call itself again and again 
#problem 1:
def facto(n):
    if(n==0 or n==1):
        return 1
    return n * facto(n-1)
n=int(input("Enter the number: "))
print(facto(n))