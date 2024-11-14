from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

choice = ""
while choice != "off":
    choice = input("What would you like? (espresso / latte / cappuccino /):").lower()
    menuItem = menu.find_drink(choice)
    print(f'Cost of {menuItem.name} = {menuItem.cost}')
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == 'off':
        print("Turning off machine ...")
        break
    elif choice == 'report': # 3. Print report
        coffeeMaker.report()
    elif menuItem is None:  # Check if choice is valid
        print("Not available")
    elif not coffeeMaker.is_resource_sufficient(menuItem): # Check resources sufficient?
        print("Not enough ingredients")
    elif moneyMachine.make_payment(menuItem.cost):  # 5. Process coins + 6. Check transaction successful?
        coffeeMaker.make_coffee(menuItem)  #7. Make Coffee.

