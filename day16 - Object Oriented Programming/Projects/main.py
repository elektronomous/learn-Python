from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import coffee_logo

def main():
    menu = Menu();
    coffee_maker = CoffeeMaker();
    money_machine = MoneyMachine();
    
    is_machine_on = True;
    
    # We create a logo first so customer know what it could buy
    print(coffee_logo);
    
    # The default state the machine is on
    while is_machine_on:
        # take the customer order
        ordered = input(f"What would you like? ({menu.get_items()}): ").lower();
        
        if ordered == "report":
            # ask the machine to report how many water, coffee and milk
            coffee_maker.report();
            money_machine.report();
            continue;

        if ordered == "off" or ordered not in menu.get_items().split('/'):
            break;
        
        # get the coffee object that the customer ordered
        get_coffee = menu.find_drink(ordered);
        
        if get_coffee:
            # check the resource of the machine
            if coffee_maker.is_resource_sufficient(get_coffee):
                # enough, then report the profit
                money_machine.report();
                # then ask the money
                if money_machine.make_payment(get_coffee.cost):
                    # payment accepted, then make the coffee
                    coffee_maker.make_coffee(get_coffee);

if __name__ == "__main__":
    main();