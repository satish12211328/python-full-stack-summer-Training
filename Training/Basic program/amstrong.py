user_value = int(input('Enter a number'))
orin = user_value
sum = 0
while(user_value>0):
    rem = user_value%10
    sum = sum+rem**3
    user_value = user_value//10
if sum == orin:
    print('Armstrong')
else:
    print('Not Armstrong')