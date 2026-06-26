#this is the menu plan for the resturant
Menu={'chai':10,
      "water":20,
      "soft_drinks":40,
      "burger":35,
      "pizza":90,
      "pasta":60
    }
bill=0
menu=('chai:10\nwater:20\nsoft_drinks:40\nburger:35\npizza:90\npasta:60')
#greetings
y=0
print("Hello customer,Whom I'm speaking with ?\nPlease enlighten me.\nMr.\nMrs.")
reply=input(":")
if (reply =='sir'):
    print("Hello Sir.\nWhat do you like to order today ?")
    print(menu)
    order_1=input(": ")
    if(order_1 in Menu):
        bill+=Menu[order_1]
        print("Your Order is added")
        print("Anything else like to order Sir,")
        yes=input(':')
        if(yes=="yes"):
                print('And that would be ?')
                print(menu)
                order_2=input(":")
                if (order_2=="pasta"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="burger"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="pizza"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="water"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="soft_drinks"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                print("Your Order is added")
                print("Anything else like to order Sir,")
                yes=input(':')
        while(yes=="yes"):
            
                print('And that would be ?')
                print(menu)
                order_2=input(":")
                if (order_2=="pasta"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="burger"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="pizza"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="water"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                elif (order_2=="soft_drinks"):
                    bill+=Menu[order_2]
                    print("Ok Sir, On my way.")
                print("Your Order is added")
                print("Anything else like to order Sir,")
                yes=input(':')
                y+=1
                if(yes=="no"):
                    break;
    print("Your bill would be :",bill)
    print("Thank You Sir, \nFor Having Us\nHave a Nice Day")

elif(reply=="mrs" ):
    print("hello Madam.\nWhat do you like to order today ?")
    print(menu)
    order_1=input(": ")
    if(order_1 in Menu):
        bill+=Menu[order_1]
        print("Your Order is added")
        print("Anything else like to order Madam,")
        yes=input(':')
        if(yes=="yes"):
                print('And that would be ?')
                print(menu)
                order_2=input(":")
                if (order_2=="pasta"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="burger"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="pizza"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="water"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="soft_drinks"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                print("Your Order is added")
                print("Anything else like to order MAdam,")
                yes=input(';')
        while(yes=="yes"):
            
                print('And that would be ?')
                print(menu)
                order_2=input(":")
                if (order_2=="pasta"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="burger"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="pizza"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="water"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                elif (order_2=="soft_drinks"):
                    bill+=Menu[order_2]
                    print("Ok MAdam, On my way.")
                print("Your Order is added")
                print("Anything else like to order MAdam,")
                yes=input(':')
                y+=1
                if(yes=="no"):
                    break;
    print("Your bill would be :",bill)
    print("Thank You MAdam, \nFor Having Us\nHave a Nice Day")
