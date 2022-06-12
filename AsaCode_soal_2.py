#sharayet mokhtalef vorood :
#number = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9] hameh bazikonan hozoor darand vali be tartib vared nashodand
#number = [1, 2, 3, 4, 5, 6, 7, 8, 10] hame bazikonan vared nashodand
#number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] hame be tartib vared shodand va amadeh final hastand
number = [1, 2, 3, 4, 9, 8] #hame bazikonan vared nashodand va tartib ham nadarand
absent_numbers = ''
numbers_shifted = []

for i in range(1, 11):
    if i not in number:
        absent_numbers += ',' + str(i)


for i in range(1, len(number)):
    if number[i] < number[i - 1]:
        numbers_shifted.append(number[i])
        numbers_shifted.append(number[i - 1])
        

# <if> ha baraye sharayet mokhtalef (vorood va hazer boodan) bazikonan ast     
if len(absent_numbers) > 0 and len(numbers_shifted) > 0:
    print('bazikonane shomareh %s hozoor nadarand va hamchnin bazikon shomareh %i nabayad dir tar az bazikon shomareh %i biyayad' %(absent_numbers.strip(','), numbers_shifted[0], numbers_shifted[1]))
elif len(numbers_shifted) == 0 and len(absent_numbers) > 0:
    print('bazikonane shomareh %s hozoor nadarand' %(absent_numbers.strip(',')))
elif len(absent_numbers) == 0 and len(numbers_shifted) > 1:
    print('hame bazikonan hazerand vali bazikone shomareh  %i bad az bazikon shomareh %i amade ast' %(numbers_shifted[0], numbers_shifted[1]))
else:
    print('hameh be bazikonan be tartib hazerand va mitavan dar final sherkat kard')