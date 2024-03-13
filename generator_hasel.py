import random

characters = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''
ask = int(input('Z ilu znaków powinno składać się hasło? '))

for i in range(ask):
    random_char = random.randint(0,71)
    symbol = characters[random_char]
    password += symbol
print('Twoje hasło: ', password)
