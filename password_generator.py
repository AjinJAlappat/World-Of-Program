import random

#length = int(input("Enter the length of the password?\n"))
letters = int(input("How many letters , Do u like in the password?\n"))
symbols = int(input("How many Symbols , Do u like in the password?\n"))
numbers = int(input("How many numbers , you need in the password?\n"))
s = ['!','@','#','$','%','^','&','*','~']
let = ['a','b','c','d','q','w']
n = ['1'',2','3','4','5','6','7','8','9','0']
#length = letters+symbols+numbers
password = []


for i in range(1,letters+1):
    char = random.choice(let)
    password+=char
for i in range(1,symbols+1):
    char = random.choice(s)
    password+=char
for i in range(1,numbers+1):
    char = random.choice(n)
    password+=char
random.shuffle(password)
new_password=""

for i in password:
    new_password+=i
print(new_password)

