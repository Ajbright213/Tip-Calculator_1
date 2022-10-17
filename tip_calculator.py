# create a function that collects user input
def tip_user_input():
    print('Welcome to the Tip Calculator')

    try:
        bill = float(input('What is your bill? '))
        num_of_peo = int(input('How many people are at your table? '))
        tip = float(input('How much % would you like to leave for a tip? 0% 5%, 10%, 15%, 20%, 25% '))
    except ValueError:
        print('Invalid input. Be sure to enter valid numbers.')

    return calculate_total_bill(num_of_peo, bill, tip)

    

# Calculate and produce user's bill, inlcuding tax and tip
def calculate_total_bill(num_of_peo, bill, tip):
    bill_tax = float(bill * .1)
    bill_tip = float(bill * (tip/100))
    total_bill = round(bill + bill_tax + bill_tip,2)
    split_bill = round(total_bill/num_of_peo, 2)
    new_bill = str(total_bill)
    print(f"Each person's total is ${split_bill}")
    print(f'The total bill with tip and tax is {new_bill}')
    # return additional_tip(new_bill)

    new_calc_tip = input('Would you like to calculate a different tip? yes or no ')

    while new_calc_tip == 'yes':
        tip_user_input()
    else:
        print('Thanks! Have a great day!')
    
#Running the user input for the first time
tip_user_input()