print("welcome to ABC Bank\n\nInsert your card")
password=1234
balance=10000
choice=0
pin=int(input("Enter your four digit pin\n"))
if pin==password:

    while choice!=4:
        print("pin correct")
        print("\n\n***Menu***")
        print("1==balance")
        print("2==deposit")
        print("3==withdraw")
        print("4==cancel\n")

        choice=int(input("\nEnter your option:\n"))
        if choice==1:
            print("balance=R",balance)

        elif choice==2:
            dep=int(input("Enter your deposit:R"))
            balance+=dep
            print("\ndeposit amount:R",dep)
            print("balance=R",balance)

        elif choice==3:
            wit=int(input("Enter your withdraw:R"))
            balance-=wit
            print("\nwithdraw amount:R",wit)
            print("balance=R",balance)

        elif choice==4:
            print("\nSession Ended!!! Goodbye...")

        else:
            print("\nInvalid Entry!!")


else:
    print("pin incorrect!! Try again")
