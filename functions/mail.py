import smtplib
import os
import sys
import time

def send_mail():        
        def exitpgm():
            print("exit from the program...")
            time.sleep(2)
            sys.exit(0)

        
        email = smtplib.SMTP("smtp.gmail.com", 587) 
        email.ehlo()                                 
        email.starttls()                            
        
        
        quantity = int(input("\nInsert amount of emails to send -->" ))

        while (True):
            try:
                user = input("\nInsert email of your gmail account (it will be the sender): ")
                password = input("Insert password: ")
                email.login(user, password) 
                break      
            except:
                choice = input("\nWrong email or password. \nCheck the options at this link for the login with stranger apps: \nhttps://myaccount.google.com/u/6/lesssecureapps?pageId=none\n\nRetry? Y/n: ")
                if choice == 'Y' or choice == 'y':
                    continue
                else:
                    exitpgm()

        print(f"\nEmails will be sent with this address: {user}")
        sender = user
        
        while(True):
            recipient = input("\nInsert recipient: ")
            choice = input("Confirm? *make sure the address is valid*\nY/n: ")
            if choice == 'Y' or choice == 'y':
                break
            else:
                continue


        object_mail0 = input("\nInsert email object: ")          
        content = input("Insert a message to send: ")    
        print ('\n')

        for n in range(1, quantity + 1):
            object_mail = (f"Subject: {object_mail0} {n}\n\n")   
            message = object_mail + content

            email.sendmail(sender, recipient, message)
            print(f"emails sent = {n}")
            
            
       
        email.quit() 

        return n, object_mail0, content
