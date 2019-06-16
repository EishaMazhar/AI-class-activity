for i in range(5):
        for k in range(i):
                print('*', end=' ')
        print()
        

def greet():
        print("good morning") #indented part function ki body hai

greet()
greet()

a= int(input("Enter number 1 : "))
b= int(input("Enter number 2 : "))
def add(a, b):
        mySum=a+b
        print(mySum)

add (a,b)

def t(owner, pet, city = "Karachi"):
        print(owner,"is an owner of", pet , ". They are from",city, ".")

t(pet="cat",owner="Eisha",city="Khi")

def check(c):
        flag=-1
        if(c%2 == 0):
                flag=0
        else:
                flag=1
        return flag

c=int(input("Enter a number : "))
val=check(c)
if(val==0):
        print("Even")
else:
        print("Odd")
