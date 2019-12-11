#puzzle input : 193651-649729 ( range of possible password )


def validNumber(value):
    valueStr = str(value)
    valueList = list(valueStr)
    # valid = False
    doubleValue = {}
    for z in range (5):
        if (valueList[z] > valueList[z+1]):
            return False
        if (valueList.count(valueList[z]) >= 2):
            #valid = True
            doubleValue[valueList[z]] = (valueList.count(valueList[z]))

    largestValue = 0 
    print (doubleValue)
    if (len(doubleValue) != 0 ):
        for keys in doubleValue:
            if ( doubleValue[keys] == 2):
                return True    
    return False 

counter = 0

for i in range ( 193651, 649730 ):
    if (validNumber(i)):
        print (i)
        counter += 1 
print ( counter )

# print (validNumber(234566))

