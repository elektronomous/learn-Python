from logo import coffee_logo
from menu import MENU, resource
from coins import penny, nickel, dime, quarter
import os

def show_resource():
    """Show resource of the our coffee machine"""
    for ingredient, n_ingredient in resource.items():
        print(f"{ingredient}: {n_ingredient}{'ml' if ingredient != 'coffee' else 'g'}")

def resource_enough(ordered:dict):
    """Check the resource of our coffee machine. return true if enough"""
    status = True;

    for ingredient, n_ingredient in ordered['ingredients'].items():
        if n_ingredient > resource[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            status = False;
    return status;

def update_resource(ordered:dict):
    for ingredient, n_ingredient in ordered['ingredients'].items():
        resource[ingredient] -= n_ingredient;

def main():
    # print logo first
    print(coffee_logo);
    
    machine_on = True;
    
    while machine_on:
        customer_order = input("What would you like? (espresso/latte/cappucino): ").lower();
        if customer_order == "report":
            show_resource();
            continue;
        if customer_order == "off" or customer_order not in MENU.keys():
            break;
        
        # ordered as the MENU customer order
        ordered = MENU[customer_order];

        if resource_enough(ordered):
            n_penny = int(input("How many penny? "));
            n_nickel = int(input("How many nickel? "));
            n_dime = int(input("How many dime? "));
            n_quarter = int(input("How many quarter? "));

            # count the price and update the resource
            money = (n_penny * penny) + (n_nickel * nickel) + (n_dime * dime) + (n_quarter * quarter);
            if money >= ordered['cost']:
                # show resource first
                show_resource();
                # then update the resource
                update_resource(ordered);
                # then show them again
                show_resource();

                print("Money: %.2f" % money);

                money -= ordered['cost'];
                # machine offer a change (susuk/kembalian)
                if money:
                    print("Here is your %.2f dollars in change." % money);
                print(f"Here's your {customer_order}. Enjoy!");
                
            else:
                print("Sorry that's enough money. Money refunded.");


if __name__ == "__main__":
    main();