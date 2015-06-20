import time
import webbrowser

class Vending_machine(object):


    def __init__(self, soda=1.50, chips=1.10, candy=0.75, giftcard=5.00): #gives item selection and prices belonging to each
        self.selection_02 = soda                                                 #class starts with $5.00 in giftcard balance
        self.selection_01 = chips
        self.selection_03 = candy
        self.giftcard = giftcard


    def check_balance(self):        #checks to see giftcard balance
        self.amount = self.giftcard
        if self.amount >= 0.75:
            print "Your balance is {}".format(self.amount)
            return self.amount
        else:
            print "Balance too low"

    def item_purchase(self):
        amount = self.check_balance()
        if amount > self.selection_01:
            amount -= self.selection_01
            print "Your balance is now {}".format(amount)
            return amount
        elif amount > self.selection_02:
            amount -= self.selection_02
            print "Your balance is now {}".format(amount)
            return amount
        elif amount > self.selection_03:
            amount -= self.selection_03
            print "Your balance is now {}".format(amount)
            return amount

vending_machine = Vending_machine()
balance = vending_machine.check_balance()
choice_00 = vending_machine.item_purchase()

def vending_visit():
    print "Hello, welcome to your friendly nieghborhood vending machine! Take a gander at what we have to offer!"
    time.sleep(0.5)
    choice = raw_input("Would you like to see your gift card balance? Press Yes or No\n"
                    "(Otherwise pick from our many choices! Input your selection accurately, or else!!!)\n"
                    "If you would like a silly bag of chips, please press one!\n"
                    "If you would like a akward tasting soda, please press two!\n"
                    "If you would like a half eaten candy bar, please press three!\n")


    if choice == 'y':
        vending_machine.check_balance()
        return vending_visit()
    elif choice == 'n':
        pass
    elif choice == '1':
        choice_01
        return vending_visit()
    elif choice == '2':
        Vending_machine.item_purchase.self.selection_02
        return vending_visit()
    elif choice == '3':
        Vending_machine.item_purchase.self.selection_03
        return vending_visit()
    else:
        KeyError
        print "Since you can't follow directions, take some lessons from this guy!"
        webbrowser.open_new("https://www.youtube.com/watch?v=BROWqjuTM0g")

vending_visit()