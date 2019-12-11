#get the information in an array
lines = []
with open('D3_input.txt', 'r') as file:
    for line in  file:
        line.rstrip('\n')
        line_arr = line.split(',')
        lines.append(line_arr)
line1 = lines[0]
line2 = lines[1]

#get the max size of board requireds
#[up,down,left,right]
coord = [0,0,0,0]
def findWidthHeight(lineArray, coordArray):
    direction_list = []
    x_movement = 0
    y_movement = 0
    for values in lineArray:
        direction = values[0]
        direction_list.append(direction)
        number_of_moves = int(values[1:])
        if (direction == 'R'):
            x_movement += number_of_moves
            coordArray[3] = max(x_movement,0, coordArray[3])
        elif (direction == 'L'): 
            x_movement = x_movement - number_of_moves
            coordArray[2] = min ( 0, x_movement, coordArray[2])
        elif (direction == 'U'): 
            y_movement = y_movement + number_of_moves
            coordArray[0] = max ( 0, y_movement,coordArray[0])
        elif (direction == 'D'): 
            y_movement = y_movement - number_of_moves
            coordArray[1] = min ( 0, y_movement, coordArray[1])
    return coordArray

findWidthHeight(line1, coord)
findWidthHeight(line2, coord)
width = coord[3] - coord[2]  
height = coord[0] - coord[1] 

#store coordinates
lineOneCoord = []

#starting coord
x = -coord[2]
y = -coord[1]
start = [x,y]
current_point = start + []

#draw line1
for movement in line1:
    direction = movement[0]
    number_of_moves = int(movement[1:])
    if (direction == 'U'): 
        for noMoves in range (number_of_moves):
            current_point[1] = current_point[1] + 1
            append_point = current_point + []
            lineOneCoord.append(append_point)
    elif (direction == 'D'): 
        for noMoves in range (number_of_moves):
            current_point[1] = current_point[1] - 1
            append_point = current_point + []
            lineOneCoord.append(append_point)
    elif (direction == 'L'): 
        for noMoves in range (number_of_moves):
            current_point[0] = current_point[0] - 1
            append_point = current_point + []
            lineOneCoord.append(append_point)
    elif (direction == 'R'): 
        for noMoves in range (number_of_moves):
            current_point[0] = current_point[0] + 1
            append_point = current_point + []
            lineOneCoord.append(append_point)

#draw line 2
lineTwoCoord = []
current_point = start
for movements in line2:
    direction = movements[0]
    number_of_moves = int(movements[1:])
    if (direction == 'U'): 
        for noMoves in range (number_of_moves):
            current_point[1] = current_point[1] + 1
            append_point = current_point + []
            lineTwoCoord.append(append_point)
    elif (direction == 'D'): 
        for noMoves in range (number_of_moves):
            current_point[1] = current_point[1] - 1
            append_point = current_point + []
            lineTwoCoord.append(append_point)
    elif (direction == 'L'): 
        for noMoves in range (number_of_moves):
            current_point[0] = current_point[0] - 1
            append_point = current_point + []
            lineTwoCoord.append(append_point)
    elif (direction == 'R'): 
        for noMoves in range (number_of_moves):
            current_point[0] = current_point[0] + 1
            append_point = current_point + []
            lineTwoCoord.append(append_point)
        
#find clashes
clash_points = []

#print ( lineTwoCoord )
#print ( lineOneCoord ) 
lineTwoLen = len(lineTwoCoord)
lineOneLen = len(lineOneCoord)
if (lineTwoLen > lineOneLen):
    for point in lineTwoCoord:
        if (point in lineOneCoord):
            clash_points.append(point)
else:
    for point in lineOneCoord:
        if (point in lineTwoCoord):
            clash_points.append(point)

#find distance for clashes
# manhattandistance = width+height

# for points in clash_points:
#     if (points[1] < y):
#         y_dist = y-points[1]
#     else:
#         y_dist = points[1] - y
#     if (points[0] < x):
#         x_dist = x - points[0]
#     else :
#         x_dist = points[0] - x
#     manhattandistance = min ( manhattandistance, x_dist + y_dist)

# print (manhattandistance)

#part 2 

#find the first interesection point 
minSteps = lineOneLen + lineTwoLen
for points in clash_points:
    numberOfStepsLineOne = lineOneCoord.index(points) + 1 
    numberOfStepsLineTwo = lineTwoCoord.index(points) + 1 
    minSteps = min(minSteps, numberOfStepsLineOne + numberOfStepsLineTwo) 


# firstIntersection = clash_points[0]
# numberOfStepsLineOne = lineOneCoord.index(firstIntersection) + 1 
# numberOfStepsLineTwo = lineTwoCoord.index(firstIntersection) + 1 
print (minSteps)