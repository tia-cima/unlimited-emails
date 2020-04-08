import smtplib
import os
import sys
import time
sys.path.insert(4, 'functions/')
from random_mail import random_mail, random_password, login_random
from password import gen_password
from gen_file import gen_file
from mail import send_mail
from ascii_art import ascii_art 


if __name__ == "__main__":

    while(True):
        choice = input(f'''
                                            
                                            
                                            
                                            
                                                        {ascii_art()}

                            1)CREATE A GMAIL ACCOUNT WITH RANDOM EMAIL & PASSWORD
                            2)GENERATE A RANDOM PASSWORD CHOOSING LENGHT AND TYPE
                            3)SEND UNLIMITED EMAILS WITH A GMAIL ACCOUNT


                            Your choice:    ''')

    
        if choice == '1':        
            print (f'''
                        RANDOM EMAIL: {random_mail()}
                        
                        RANDOM PASSWORD: {random_password()}

                        LOADING GMAIL LOGIN PAGE...''')
            time.sleep(2)
            login_random()

        elif choice == '2':
            print(f"\n\n        RANDOM PASSWORD:      {gen_password()}\n\n")     
        
        elif choice == '3':    
            n, object0, content = send_mail()    
            gen_file(n, object0, content)        
            
    
        choice = input('''                                                                       
                                                                            
        █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
        ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                                            
                Do you want to affect other options? Y/n: ''') 
        if choice == 'y' or choice == 'Y':
            continue
        else:
            break
        