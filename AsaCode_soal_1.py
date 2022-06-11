# by python3
number = input()
number_list = []

while number_list == sorted(number_list):
    for i in number:
        number_list.append(int(i))

    if number_list == sorted(number_list):
        print(number)
        break

    else:
        number = int(number) - 1
        number = str(number)
        number_list = []
        
        
