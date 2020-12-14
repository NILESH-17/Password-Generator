import random
bigletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallletters='abcdefghijklmnopqrstuvwxyz'
symbol='_-,:'
numbers='123456789'
all=bigletters+smallletters+symbol+numbers
length=16
password =''.join(random.sample(all,length))
print(password)
