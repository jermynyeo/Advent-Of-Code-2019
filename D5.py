# # part1


# def valueToAdd (mode, position):
#     value = int(position) 
#     if (mode == str(0) or mode == 0):
#         value = int(numbers[position])
#     return value


# with open ("D5_input.txt", 'r') as file: 
#     for line in file: 
#         line = line.rstrip("\n")
#         numbers = line.split(',')
#         edit = False
#         for i in range(len(numbers)):
#             z = i
#             if ( edit ) :
#                 z = i - 2
#             if (z%4 == 0 and ((z+3) < len(numbers))):
#                 positionOne = int(numbers[i+1])
#                 positionTwo = int(numbers[i+2])
#                 outputPosition = int(numbers[i+3])
#                 numbers[i] = str(numbers[i])
#                 if ( len(numbers[i]) <= 2 ):
#                     opcode = int(numbers[i])
#                     positionOneMode = 0
#                     positionTwoMode = 0
#                     outputPositionMode = 0
#                 elif (len(numbers[i]) == 3):
#                     opcode = int(numbers[i][1:] )
#                     positionOneMode = numbers[i][0]
#                     positionTwoMode = 0
#                     outputPositionMode = 0
#                 elif (len(numbers[i]) == 4):
#                     opcode = int(numbers[i][2:] )
#                     positionOneMode = numbers[i][1]
#                     positionTwoMode = numbers[i][0]
#                     outputPositionMode = 0
#                 else : 
#                     opcode = int( numbers[i][3:] )
#                     positionOneMode = numbers[i][2]
#                     positionTwoMode = numbers[i][1]
#                     outputPositionMode = numbers[i][0]
#                 if (opcode == 99):
#                     print (numbers[0])
#                     quit()
#                 elif (opcode == 1):
#                     if (outputPositionMode == 1):
#                         outputPosition = numbers[outputPosition]
#                     numbers[outputPosition] = valueToAdd (positionOneMode, positionOne) + valueToAdd (positionTwoMode, positionTwo)
#                 elif (opcode == 2):
#                     if (outputPositionMode == 1):
#                         outputPosition = numbers[outputPosition]
#                     numbers[outputPosition]= valueToAdd (positionOneMode, positionOne) * valueToAdd (positionTwoMode, positionTwo)
#                 elif (opcode == 3):
#                     numbers[positionOne] = int(input("Please input value: "))
#                     edit = not edit
#                 elif (opcode == 4):
#                     numbers[positionOne] = int (numbers[positionOne])
#                     print (numbers[positionOne])
#                     edit = not edit

#part 2    

def valueToAdd (mode, position):
    value = int(position) 
    if (mode == str(0) or mode == 0):
        value = int(numbers[position])
    return value


with open ("D5_P2_input.txt", 'r') as file: 
    for line in file: 
        line = line.rstrip("\n")
        numbers = line.split(',')
        edit = False
        pointer = (False,0)
        for i in range(len(numbers)):
            z = i
            # print (pointer)
            if (pointer[0]):
                if (i != pointer[1]):
                    continue
            if ( edit ) :
                z = i - 2
            if (z%4 == 0 and ((z+3) < len(numbers))):
                positionOne = int(numbers[i+1])
                positionTwo = int(numbers[i+2])
                outputPosition = int(numbers[i+3])
                numbers[i] = str(numbers[i])
                if ( len(numbers[i]) <= 2 ):
                    opcode = int(numbers[i])
                    positionOneMode = 0
                    positionTwoMode = 0
                    outputPositionMode = 0
                elif (len(numbers[i]) == 3):
                    opcode = int(numbers[i][1:] )
                    positionOneMode = numbers[i][0]
                    positionTwoMode = 0
                    outputPositionMode = 0
                elif (len(numbers[i]) == 4):
                    opcode = int(numbers[i][2:] )
                    positionOneMode = numbers[i][1]
                    positionTwoMode = numbers[i][0]
                    outputPositionMode = 0
                else : 
                    opcode = int( numbers[i][3:] )
                    positionOneMode = numbers[i][2]
                    positionTwoMode = numbers[i][1]
                    outputPositionMode = numbers[i][0]
                
                print ('opcode: ', end ='')
                print (opcode)

                if (opcode == 99):
                    print (i)
                    print (numbers[0])
                    quit()
                elif (opcode == 1):
                    if (outputPositionMode == 1):
                        outputPosition = numbers[outputPosition]
                    numbers[outputPosition] = valueToAdd (positionOneMode, positionOne) + valueToAdd (positionTwoMode, positionTwo)

                elif (opcode == 2):
                    if (outputPositionMode == 1):
                        outputPosition = numbers[outputPosition]
                    numbers[outputPosition]= valueToAdd (positionOneMode, positionOne) * valueToAdd (positionTwoMode, positionTwo)
                    
                elif (opcode == 3):
                    numbers[positionOne] = int(input("Please input value: "))
                    edit = not edit
                    
                elif (opcode == 4):
                    numbers[positionOne] = int (numbers[positionOne])
                    print (numbers[positionOne])
                    edit = not edit
                    

                elif (opcode == 5):
                    if ( valueToAdd (positionOneMode, positionOne) != 0 ):
                        pointer = (True, valueToAdd (positionTwoMode, positionTwo) + i)

                elif (opcode == 6):
                    if ( valueToAdd (positionOneMode, positionOne) == 0 ):
                        pointer = (True, valueToAdd (positionTwoMode, positionTwo) + i )

                elif (opcode == 7):
                    if (outputPositionMode == 1):
                        outputPosition = numbers[outputPosition]
                    numbers[outputPosition] = 0
                    if (valueToAdd (positionOneMode, positionOne) < valueToAdd (positionTwoMode, positionTwo) ):
                        numbers[outputPosition] = 1

                elif (opcode == 8):
                    if (outputPositionMode == 1):
                        outputPosition = numbers[outputPosition]
                    numbers[outputPosition] = 0
                    if (valueToAdd (positionOneMode, positionOne) == valueToAdd (positionTwoMode, positionTwo) ):
                        numbers[outputPosition] = 1
                        
                    