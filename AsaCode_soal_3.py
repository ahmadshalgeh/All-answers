#من به طور کامل متوجه منظور سوال نشدم 
# منظورتون همین برنامست که نوشتم ؟؟ 

numbers = '2,4,6,8'
numbers= numbers.split(',')
new_numbers = ''
for number in numbers:
    number = pow(int(number),  2)
    new_numbers += ',' + str(number) 

print(new_numbers.strip(','))