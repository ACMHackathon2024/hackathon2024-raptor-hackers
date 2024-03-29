import re
import string
import secrets
import random

score = 3

def validate(password):
    global score
    while True:
        if len(password) < 8 or len(password) > 15:
            print("Make sure your password is at lest 8 letters")
            score -=1
            return False
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
            score -=1
            return False
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
            score -=1
            return False
        else:
            print("Your password seems fine")
            return True



# Main method
def main():
    '''Username and password input'''
    password = input("Enter Your Password : ")
    if (validate(password)):
        return(validate)
    else:
        print("Generating random password")
        gen = ""
        length = random.randint(8, 15)
        for i in range(0, length):
            gen += chr(random.randint(33, 126))
        if score < 3:
            print(gen)

        if score > 3:
            score = 3

        print(["Weak", "Medium", "Strong", "Excellent"][score])
         
# Driver Code        
if __name__ == '__main__':
    main()



