import random, sys, time

def gen_password():
    
    def create(word_list):
        word_list = (''.join(random.choice(word_list) for m in range(lenght)))
        return word_list

    lenght = int(input("\n       Insert password lenght: "))
                                                                                        
    choice = input('''

                   Select the password type:

                1)Only letters (upper and lower)
                2)Only numbers
                3)Alphanumeric (upper/lower + numbers)
                4)Alphanumeric with symbols (upper/lower + numbers + symbols(,.:;?!'"&*#@))
                

                choice: ''')

    if choice == '1':
        word_list = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        password_return = create(word_list)

    elif  choice == '2':
        word_list = ("0123456789")
        password_return = create(word_list)

    elif  choice == '3':
        word_list = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678901234567890123456789")
        password_return = create(word_list)

    elif  choice == '4':
        word_list = ('''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678901234567890123456789,.:;?!'"&*#@,.:;?!'"&*#@,.:;?!'"&*#@,.:;?!'"&*#@''')
        password_return = create(word_list)

    else:
        print("No password created")
        time.sleep(4)
        sys.exit(0)

    return password_return
