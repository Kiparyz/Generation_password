import random

s = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

len_pass = int(input("Укажите длину пароля"))

password = ''

for x in range(len_pass):
    password += random.choice('abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    
    print(password)