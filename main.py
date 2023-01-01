import random

uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special_characters="!@#$%^&*()"

upper=True
lower=True
nums=True
spec_char=True

string=""

if upper:
    string+=uppercase
if lower:
    string+=lowercase
if nums:
    string+=numbers
if spec_char:
    string+=special_characters

length=10
count=5

for i in range(count):
    password="".join(random.sample(string,length))
    print("Your Password is:",password)
   


    

