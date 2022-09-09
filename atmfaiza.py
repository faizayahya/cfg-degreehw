#key infomation
password = 4444
keeping_count = 0
balance = 100
withdrawal_amount = 0

#user ID infomation
def integer(prompt):
    ID_input = -1
    while ID_input <= 0:
        try:
            ID_input = int(input(prompt))
        except ValueError:
            print("Please enter an integer.")
            continue
    return ID_input


#account details (pin,balance)
while keeping_count < 3:
    print("*FAIZA'S ATM MACHINE*")
    print("--WELCOME--")
    ID_pass = integer("Please enter your pin: \n")
    if ID_pass == password:
        keeping_count = 0
        print("Pin accepted!")
        print('Your current balance is: £{}'.format(balance))
        withdrawal_amount = integer("Please enter an amount to withdraw: ")

        if withdrawal_amount  <= balance:
            print('You have made a withdrawal of : £{}'.format(withrawal_amount))
            print('Your new balance is: £{}'.format(balance))

            user_options = input('Would you like another service? yes/no:\n')

            if user_options == 'yes':

                print('One Moment Please')

            else:

                print('Thank you for using this service.')

                keeping_count = 3

        else:

            print('Sorry insufficient funds, your available balance is £{}.'.format(balance))

    else:

        keeping_count += 1
        print(

            "Your password is incorrect. You have {} attempts left!".format(3 - keeping_count))


