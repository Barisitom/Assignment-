options = ['1. Add item', '2. View cart', '3. Remove item', '4. Compute total', '5. Quit']
cart = []
price =[]
total=0


print('Welcome to the Shopping Cart Program!')
while True :
    print('\nPlease select one of the following:')
    for i in options:
        print(f'{i} ')
    action = int(input('Please enter an action: '))

    if  action == 1:
        actionb = input('What item would you like to add? ')
        cart.append(actionb)
        actionc = float(input(f"What is the price of {actionb}? "))
        price.append(actionc)
        print(f"'{actionb}' has been added to the Cart.")
        
    elif action == 2:
        print('The content of the shopping cart are: ')
        count = 0
        for item in cart:
            print(F"{item} - ${price[count]}")
            count +=1

    elif action == 3:
        cart_length = len(cart)
        delete = int(input('Which item would you like to remove? '))
        if action <= cart_length :
            delete-=1
            del cart[delete]
            del price[delete]
        else:
            print('sorry, that is not a valid item number')

    elif action == 4:
        total = 0
        for i in price:
            total += i
        print(f'The total price of the items in the shoping cart is {total}')

    elif action == 5:
        break


print('Thank you. Goodbye.')