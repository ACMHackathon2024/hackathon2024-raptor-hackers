# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re
import random

score = 0

error = ""

password = input("Please Enter Password: ")
print("Password: " + password)

#if len(password) == 0:
    #throw
    
if len(password) <= 8:
    error += "Length < 8"
    score -= 1
    
if(re.search(r'[0-9]+', password)):
    #print('number')
    score += 1
else:
    error += "Number"
    
if(re.search(r'[a-z]+', password)):
    #print('lower')
    score += 1
    
if(re.search(r'[A-Z]+', password)):
    #print('upper')
    score += 1
    
if(re.search(r'[!-/]+', password)):
    #print('synbol')
    score += 1

gen = ""

for i in range(0, 10):
    gen += chr(random.randint(33, 126))
    
if score < 3:
    print(gen)

if score > 3:
    score = 3

print(["Weak", "Medium", "Strong", "Excellent"][score])
