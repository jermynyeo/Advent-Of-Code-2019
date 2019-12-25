#1. create the layers
#2. fit the pixels in the layers 
imageX = 25
imageY = 6
with open ('D8_input.txt', 'r') as file: 
    for lines in file: 
        lines = lines.rstrip('\n')
        xCounter = 0
        yCounter = 0
        image = []
        layer = []
        pixels = []
        for num in lines:
            if ( yCounter < imageY ):
                if ( xCounter < imageX ): 
                    pixels.append(num)
                    xCounter += 1
                else : 
                    layer.append(pixels)
                    pixels = [num]
                    yCounter += 1 
                    xCounter = 1

            else : 
                image.append(layer)
                layer = []
                pixels.append(num)
                yCounter = 0
                xCounter += 1
        layer.append(pixels)
        image.append(layer)

#part 1
# noZeros = 99999999999999999999999999999999999999999999999999999999999999999
# zeroCount = 0
# for i in image:
#     for z in i: 
#         zeroCount += z.count('0')
#     if ( zeroCount < noZeros ):
#         noZeros = zeroCount
#         fewestZero = i
#     zeroCount = 0
# oneCount = 0
# twoCount = 0 
# for j in fewestZero:
#     oneCount += j.count('1')
#     twoCount += j.count('2')
# print (oneCount * twoCount)

#part 2 
# initalizing the output image
outputImage = image[0] + []
print (outputImage)

# print (outputImage)
# print (len(outputImage))
for i in range(len(outputImage)):
    for z in range(len(outputImage[i])):
        if ( outputImage[i][z] == '2'): 
            for j in range(1, len(image)):
                if (outputImage[i][z] == '2' and image[j][i][z] != '2'):
                    outputImage[i][z] = image[j][i][z]
print (outputImage)

#USE AN IMAGE CONVERTER https://www.dcode.fr/binary-image TO FIND THE PASSWORD