orbits = {}

with open ("D6_input.txt", 'r') as file: 
    for line in file: 
        line = line.rstrip("\n")
        value = line.split(')')
        planet = value[0]
        orbit = value[1]
        if (planet in orbits.keys()):
            orbits[planet].append(orbit)
        else:
            orbits[planet] = [orbit]

print (orbits)

#part 1
# #count orbitals
# counter = 0
# for i in (orbits.values()):
#     for z in range (len(i)):
#         value = i[z]
#         while (value != 'COM'):
#             for k in orbits.keys():
#                 if (value in orbits[k]):
#                     value = k
#                     counter += 1 
# print (counter)

#PART 2 
value = 'YOU'
pathToYou = []
#find path to 'YOU'
while (value != 'COM'):
    for k in orbits.keys():
        if (value in orbits[k]):
            value = k
            pathToYou.append(value)
pathToYou = pathToYou[::-1] + []

value = 'SAN'
pathToSan =  []
#find path to 'YOU'
while (value != 'COM'):
    for k in orbits.keys():
        if (value in orbits[k]):
            value = k
            pathToSan.append(value)
pathToSan = pathToSan[::-1] + []

print (pathToYou)
print (pathToSan)
if (len(pathToSan) > len(pathToYou)):
    for i in range(len(pathToSan)):
        if (pathToSan[i] != pathToYou[i]):
            split = i
            break
    distance = len(pathToYou) + len(pathToSan) - (split*2)
else: 
    for i in range(len(pathToYou)):
        if (pathToSan[i] != pathToYou[i]):
            split = i
            break
    distance = len(pathToYou) + len(pathToSan) - (split*2)
print (split)
print ("distance" , end = '')
print (distance)