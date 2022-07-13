category=["Infants","Toddlers","Childern"]
infant=["Ping Ping Panda, 32Cm","Happyland Ride on Bus","Soft Caterpillar     ","Soft Fighter Panda     ","Bear Ball Pit           "]
infant_price=[2199,2999,1499,899,2799]
toddler=["Super buddy Rabbito","Xylophone             ","Splash Light Up Turtle","Tricycle               ","Learning blocks     "]
toddler_price=[4000,1299,600,6000,2000]
child=["Jumbo Teddy            ","Stunt Car             ","Penguin Soft Toys        ","Musicjam Playmat        ","Musical Bee Catcher Game"]
child_price=[3999,2000,2799,3499,1000]
crt=[]
amt=[]
tamt=[]
name=input(("Please enter your name: "))
p_no=int(input("Please enter your phone number: "))
def infants():
    print("Welcome to Infants section")
    for i in range(len(infant)):
        print((i+1),".",infant[i],"\t\t",infant_price[i])
    print("0 . Main Menu")
    c=int(input("Choose a product: "))
    a=int(input("Enter the number of items: "))
    if c>0 and c<=5 :
        crt.append(infant[c-1])
        amt.append(a)
        total=infant_price[c-1]*a
        tamt.append(total)
    if(c==0):
        menu()
    menu()
def toddlers():
    print("Welcome to toddlers section")
    for i in range(len(toddler)):
        print((i+1),".",toddler[i],"\t\t",toddler_price[i])
    print("0 . Main Menu")
    c=int(input("Choose a product: "))
    a=int(input("Enter the number of items: "))
    if c>0 and c<=5 :
        crt.append(toddler[c-1])
        amt.append(a)
        total=infant_price[c-1]*a
        tamt.append(total)
    if(c==0):
        menu()
    menu()
def children():
    print("Welcome to children section")
    for i in range(len(child)):
        print((i+1),".",child[i],"\t\t",child_price[i])
    print("0 . Main Menu")
    c=int(input("Choose a product: "))
    a=int(input("Enter the number of items: "))
    if c>0 and c<=5 :
        crt.append(child[c-1])
        amt.append(a)
        total=child_price[c-1]*a
        tamt.append(total)
    if(c==0):
        menu()
    menu()
def cart():
    sum=0
    print("Sr no.\tProduct\t\t\t Quantity  \t\t Payable Amount")
    for i in range(len(crt)):
        print((i+1),".",crt[i],"\t",amt[i],"\t\t\t",tamt[i])
        sum=sum+tamt[i]
    print("The payable Amount is ",sum)
    print("1 . Buy")
    print("2 . Remove item")
    print("3 . Continue Shopping")
    print("4 . Exit")
    c=int(input("Enter Your choice: "))
    if(c==1):
        print("                             Bill")
        print("Name: ",name,"              Phone number: ",p_no)
        print("________________________________________________________________________")
        print("\tProduct\t\t\t Quantity  \t\t Payable Amount")
        print("________________________________________________________________________")
        for i in range(len(crt)):
            print((i+1),".",crt[i],"\t",amt[i],"\t\t\t",tamt[i])
        print("________________________________________________________________________")
        print("The Amount Payed is ",sum)
        print("Thanks For Shopping with us")
    elif(c==2):
        n=int(input("Which product do you want to delete: "))
        for i in range((n-1),(len(crt)-1)):
            crt[i]=crt[i+1]
            amt[i]=amt[i+1]
        crt.pop()
        amt.pop()
        cart()
    elif(c==3):
        menu()
    elif(c==4):
        print("Thanks for Shopping with Us.")
    else:
        print("Please Enter a valid Choice")
        cart()
def menu():
    print("Welcome to TOY STORE")
    for i in range(len(category)):
        print((i+1),".",category[i])
    print("9 . Cart")
    print("0 . Exit")
    c=int(input("Choose a category: "))
    if c==1 :
        infants()
    elif c==2 :
        toddlers()
    elif c==3 :
        children()
    elif c==9 :
        cart()
    elif c==0 :
        print("Thanks for Shopping with Us.")
    else:
        print("Enter a valid choice")
        menu()
menu()
