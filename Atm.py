class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balanceinquiry(self):
        print("YOUR BALANCE IS: $100")

    def cashwidthdrawal(self,amount):
        new_amount=100-amount
        print("YOU WITHDRAWED:" + str(amount) + "YOUR REMAINING BALANCE IS: " + str(new_amount))

def main():
         name=input("HELLO WHAT IS YOUR NAME?")
         print("HELLO ,  " +name)
         cardnumber=input("INSERT YOUR CARD NUMBER:  ")
         pin=input("ENTER YOUR PIN:  ")
         new_user=Atm(cardnumber,pin)

         print("CHOOSE YOUR ACTIVITY")
         print("1. BALANCE INQUIRY")
         print("2. CASH WITHDRAWAL")
         activity=int(input("ENTER ACTIVITY CHOICE: "))

         if(activity==1):
             new_user.balanceinquiry()
         elif(activity==2):
                amount=int(input("ENTER THE AMOUNT: "))
                new_user.cashwidthdrawal(amount)
         else:
             print("ENTER A VALID NUMBER")

if __name__=="__main__":
    main()
