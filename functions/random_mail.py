import random
import string
import webbrowser


def random_mail():
    domain = "gmail.com"
    lenght = int(12)
    letters = string.ascii_letters[:12]
    
    email = (''.join(random.choice(letters) for i in range(lenght))) + '@' + domain
    return email


def random_password():
    lenght = int(12)
    alfanumeric_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    password = (''.join(random.choice(alfanumeric_letters) for i in range(lenght)))
    return password


def login_random():
    webbrowser.open("https://accounts.google.com/signup/v2/webcreateaccount?hl=en-GB&flowName=GlifWebSignIn&flowEntry=SignUp")


