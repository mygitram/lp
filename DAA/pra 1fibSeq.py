#Recursive fibonacci
def fib(num):
    if num<=1:
        return num
    else:
        return(fib(num-1)+fib(num-2))

for i in range(5):
    print(fib(i))

num1 = 0
num2= 1
count = 0
while count<5:
    print(num1)
    num = num1+num2
    num1 = num2
    num2 = num
    count+=1