
''' Program header
program name: assignment.py
author: @Nguyen Anh Bao 
        @Noah Urbano
        @Allyson Licerio 
date: March `2026
description: Assignment: Programming Strategies
Description: The program allows user selects a beverage and chooses optional extras (sugar, cream, or syrup),
            calculates the subtotal, applies a discount if the subtotal exceeds $5.00, and adds tax,
            and displays the order summary and a final receipt with the total cost and number of drinks ordered.
'''

#Constant for assignment
from typing import Final
COFFEE_COST: Final = 3.00
TEA_COST: Final = 2.50
HOT_CHOCOLATE_COST: Final = 3.75
SUGAR_COST: Final = 0.10
SYRUP_COST: Final = 0.75
CREAM_COST: Final = 0.50
TAX: Final = 0.05
DISCOUNT: Final = 0.1
PRICE_FOR_DISCOUNT:Final = 5.00

#Constant Dictionary for extras and drinks
drink_dictionary = {1:"Coffee",2:"Tea",3:"Hot Chocolate"}
extra_dictionary = {1:"Sugar",2:"Cream",3:"Syrup"}
drink_cost_dictionary = {"Coffee":3.00,"Tea":2.50,"Hot Chocolate":3.75}
extras_cost_dictionary = {"Sugar":0.10,"Cream":0.50,"Syrup":0.75}

number_of_drinks = 0
order_number = 1
user_continue_choice = "Y"
total = 0
#Keep displaying the cafe section and extra selection section until user's continue choice is N
while(user_continue_choice == "Y" or user_continue_choice == "y"):
    extra_status = {"Sugar":"","Cream":"","Syrup":""}
    user_drink_selection = -1
    subtotal = 0
    ''' 
        Cafe section:
        Display cafe menu and allow user to choose drink
        Keep displaying the menu until user's choice is valid
    '''
    while(user_drink_selection < 1 or user_drink_selection > 3):
        print("=" * 38)
        print(f'{"WELCOME TO Python CAFE":^38}')
        print("=" * 38)
        print("")

        print(f'Order #{order_number}')
        order_number += 1
        print("-" * 8)
        print("")

        print("=" * 38)
        print(f'{"Beverage Menu:":^38}')
        print("=" * 38)
        print(f'{"1.":<3}{"Coffee":<16}{"$3.00"}')
        print(f'{"2.":<3}{"Tea":<16}{"$2.50"}')
        print(f'{"3.":<3}{"Hot chocolate":<16}{"$3.75"}')
        print("=" * 38)

        user_drink_selection = int(input("Your selection (1-3): "))
        print("")
        if 1 <= user_drink_selection <= 3:
            drink_product = drink_dictionary[user_drink_selection]
            drink_cost = drink_cost_dictionary[drink_product]
            subtotal += drink_cost_dictionary[drink_product]
        else:
            print("Please enter a number between 1 and 3.")
        print("")

    """
        Extra selection section:
        Display extra selection menu
        Keep display the extra selection menu until user's choice is 0
    """
    user_extra_selection = -1
    while user_extra_selection != 0:
        print("=" * 38)
        print(f'{"Add Extras":^38}')
        print("=" * 38)
        print(f'{"1.":<3}{"Sugar":<16}{"$0.10":<6}{extra_status["Sugar"]}')
        print(f'{"2.":<3}{"Cream":<16}{"$0.50":<6}{extra_status["Cream"]}')
        print(f'{"3.":<3}{"Syrup":<16}{"$0.75":<6}{extra_status["Syrup"]}')
        print(f'{"0.":<3}{"Finish order"}')

        user_extra_selection = int(input("Select extra (0-3): "))
    
        if 1 <= user_extra_selection <= 3:
            user_extra_choice = extra_dictionary[user_extra_selection]
            if extra_status[user_extra_choice] == "✓":
                 print(f'{user_extra_choice} is already added.')
            else:
                 extra_status[user_extra_choice] = "✓" 
                 print(f'{user_extra_choice} added (+${extras_cost_dictionary[user_extra_choice]})')
                 subtotal += extras_cost_dictionary[user_extra_choice]
        else:
                print("Please enter a number between 0 and 3.")
    
#Print Order Summary
    print("")
    print("=" * 38)
    print(f'{"ORDER SUMMARY":^38}')
    print("=" * 38)
    print(f'{"Beverage: "}{drink_product:<21}${drink_cost:<6.2f}')
    
    extra_contain = False
    for status in extra_status.values():
        if status == "✓":
            break
            
    if extra_contain == True:
        for extra, status in extra_status.items():
            if status == "✓":
                print(f'{" • Sugar":<31}{"$0.10":<7}')
                subtotal += extras_cost_dictionary[extra]
    
    if subtotal > PRICE_FOR_DISCOUNT:
        print(f'{"Discount:":<30}-${subtotal*DISCOUNT:<5.2f}')
        print(f'{"After discount:":<31}${subtotal*(1-DISCOUNT):<5.2f}')
        print(f'{"Subtotal:":<31}${subtotal*(1-DISCOUNT):<6.2f}') 
        total += subtotal*(1-DISCOUNT)
    else:  
        total += subtotal
        print(f'{"Subtotal:":<31}${subtotal:<6.2f}')  
    user_continue_choice = input("Would you like to order another drink? (Y/N): ")
    if user_continue_choice == "" :
        user_continue_choice = "N"

#Print recipt summary
print("=" * 38)
print(f'{"RECEIPT SUMMARY":^38}')
print("=" * 38)
print("")

print(f'{"Number of drinks":<32}{number_of_drinks:<6}')
print(f'{"Subtotal":<32}${total:<5.2f}')
print(f'{"Tax (5%)":<32}${total*TAX:<5.2f}')
print(f'{"Grand total":<32}${total*(1+TAX):<5.2f}')
print("=" * 38)
print("Thank you for visiting Python Cafe! ")
print("We hope to see you again soon! ")
        
   





