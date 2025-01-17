import random as r
no_of_runs = int(input("Number of iterations for loop to run: "))
min_num = int(input("Enter the minmium number: "))
max_num = int(input("Enter the maxium number: "))
modulo_value = int(input("Enter a modulo value: "))

while True:    
    if min_num < modulo_value and max_num > modulo_value:
        break
    else:
        modulo_value = int(input("Enter a modulo value: "))


list1 = []
x = 1
modulo_multiples = modulo_value
while True:
        x += 1
        if x % modulo_value == 0 and min_num < modulo_multiples and max_num > modulo_multiples:
            modulo_multiples = modulo_value * x
            list1.append(modulo_multiples)
            print(list1)
            print(x)
        elif min_num > modulo_multiples or max_num < modulo_multiples:
            break


    
    
    
    
    
    
        

        
    

