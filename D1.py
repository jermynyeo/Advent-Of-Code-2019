#part 1
# with open ("D1_input.txt", 'r') as file: 
#     sum = 0
#     for line in file: 
#         value = line.rstrip('\n')
#         value = int(value)  
#         value = (value//3 - 2)
#         sum += value
#     print (sum)

#part 2 
with open ("D1_input.txt", 'r') as file: 
    sum = 0
    for line in file: 
        value = line.rstrip('\n')
        value = int(value)  
        valueSum = 0
        fuel = value
        while fuel > 5:
            fuel = fuel // 3 - 2
            valueSum += fuel
        sum += valueSum
    print (sum)
