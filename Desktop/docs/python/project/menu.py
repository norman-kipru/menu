print("Welcome to Vanilla Corp")
print("Choose option")
print("1. Read the population data")
print("2. Write more data")
print("3. Exit system")
file="vanilla.txt"
def writing():
    file=open(file,"w")
    file.write(input("Enter data to be input: "))
    file.close()

def reading():
    read=open(file,"r")
    print(file.read())
    file.closed()

choice=1
while choice==1:
    choice=int(input("Enter choice: "))
    if choice==1:
         print(reading)
    elif choice==2:
         print(writing)
    else:
         print("Thank you for visiting our site")

choice=int(input("Enter choice: "))
     
    

    

    

