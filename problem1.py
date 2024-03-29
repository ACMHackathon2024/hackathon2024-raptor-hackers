import re

def length(pwd, count):
    if len(pwd) <= 8:
        print("Not Long Enough!")
    else:
        return count + 1

def mixed_case(pwd, count):
    if pwd.isupper():
        print("Not strong enough, needs to be mixed cases")
    elif pwd.islower():
        print("Not strong enough, needs mixed cases")
    else:
        return count + 1
    
def special_chars(pwd, count):
    x = re.findall("[~`!@#$%^&*()_-+={[}]|\:;""'<,>.?/]", pwd)
    if x:
        print("No symbols")
    else:
        return count + 1

def main():
    count = 0
    i = 0
    password = input("Password: ", )
    while i == 0:
        print(password)
        length(password, count)
        mixed_case(password, count)
        special_chars(password, count)
    return 1


if __name__ == "__main__":
    main()

#i = 0
#while i == 0:

        
