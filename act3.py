def add(num1,num2):
    return (num1+num2)

def sub(num1,num2):
    return (num1-num2)

def mul(num1,num2):
    return (num1*num2)

def divide(num1,num2):
    return (num1/num2)

print("please select which operation to perform- ")
print("A. add")
print("B. subtract")
print("C. multiply")
print("D. divide")
choice=input("please enter choice- ")
num1=int(input("please enter the first number- "))
num2=int(input("please enter the second number- "))

if choice=="A" :
    print("the answer is ",add(num1,num2))
elif choice=="B" :
    print("the answer is ",sub(num1,num2))
elif choice=="C" :
    print("the answer is ",mul(num1,num2))
elif choice=="D" :
    print("the answer is ",divide(num1,num2))
else :
    print("there was an error")