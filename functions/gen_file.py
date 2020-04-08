import os, time, sys
#CREAZIONE FILE DI TESTO PER VEDERE QUANTE MAIL SONO STATE INVIATE
def gen_file(n, object_mail0, content):    
    
    def exitpgm():
            print("exit from pgm...")
            time.sleep(2)
            sys.exit(0)
    
    path_file = os.getcwd()
    choice = input("\n\nDo you want to create a text file where the amount of emails sent, the object and the message are saved? Y/n: ")
    while(True):
        if choice == 'Y' or choice == 'y':
            try:
                file_name = input("\nInsert text file name: ")
                file1 = open(f"{file_name}.txt", "a")
                file1.write(f"\nAmount of emails sent:{str(n)}\nobject: {object_mail0}\nmessagge: {content}\n\n")
                file1.close
                print(f"\n\"{file_name}.txt\" successfully opened and overwritten at path <{path_file}>\n")
                os.system("pause")
                break
            except: 
                choice = input("Something went wrong, retry? Y/n: ")
                if choice == 'Y' or choice == 'y':
                    continue
                else:
                    exitpgm()
        else:
            print("\nEmails sent successfully but no files created.\n")
            exitpgm()
