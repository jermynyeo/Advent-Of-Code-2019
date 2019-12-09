# part1
# with open ("D2_input.txt", 'r') as file: 
#     for line in file: 
#         line = line.rstrip("\n")
#         numbers = line.split(',')
#         for i in range(len(numbers)):
#             if (i%4 == 0 and ((i+3) < len(numbers))):
#                 numbers[i] = int(numbers[i])
#                 positionOne = int(numbers[i+1])
#                 positionTwo = int(numbers[i+2])
#                 outputPosition = int(numbers[i+3])
#                 if (numbers[i] == 99):
#                     print (numbers[0])
#                 elif (numbers[i] == 1):
#                     numbers[outputPosition] = int(numbers[positionOne]) + int(numbers[positionTwo])
#                 elif (numbers[i] == 2):
#                     numbers[outputPosition] = int(numbers[positionOne]) * int(numbers[positionTwo])

#part 2        
with open ("D2_P2_input.txt", 'r') as file: 
    for line in file: 
        line = line.rstrip("\n")
        original_number_list = line.split(',')

for z in range (1,100):
    for j in range (1,100):
        new_number_list = original_number_list + []
        new_number_list[1] = z
        new_number_list[2] = j 
        for i in range(len(new_number_list)):
            if (i%4 == 0 and ((i+3) < len(new_number_list))):
                new_number_list[i] = int(new_number_list[i])
                positionOne = int(new_number_list[i+1])
                positionTwo = int(new_number_list[i+2])
                outputPosition = int(new_number_list[i+3])
                if (new_number_list[i] == 99):
                    if (new_number_list[0] == 19690720):
                        print ( (z * 100 ) + j)
                elif (new_number_list[i] == 1):
                    new_number_list[outputPosition] = int(new_number_list[positionOne]) + int(new_number_list[positionTwo])
                elif (new_number_list[i] == 2):
                    new_number_list[outputPosition] = int(new_number_list[positionOne]) * int(new_number_list[positionTwo])
