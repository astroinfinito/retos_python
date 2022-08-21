###
# 
# Dado un listado de números, encuentra el valor más alto y el segundo más grande.
#
####

numbers = [55, 4, 92, 1, 104, 64, 73, 99, 67]

max_value = None

for num in numbers:
    
    if (max_value is None or num > max_value):
        max_value = num
        
         
print('Valor más alto:', max_value)

numbers.sort(reverse=True)

print('Segundo valor más alto: ',numbers[1])


    