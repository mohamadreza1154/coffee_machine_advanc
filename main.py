from menu import MenuItem,Menu
from money_machine import MoneyMachine
from coffee_macker import CoffeeMaker
menu =Menu()
menu_item = MoneyMachine()
money_m = MoneyMachine()
coffee_m = CoffeeMaker()
turn_on  = True
while turn_on:
    coffee_m.report()
    question = input("what do you like(espresso,latte , cappuccino)")
    drink=menu.find_drink(question)
    turn_on= coffee_m.is_resource_sufficient(drink)
    turn_on= money_m.make_payment(drink.cost)
    coffee_m.make_coffee(drink)
    money_m.report()



