# soal 1
def sortirList(listToCheck):
    newList = []
    for element in listToCheck:
        if (element % 2 == 0):
            newList.append(element)   # kesalahan di 'newList += element'
    print(newList)

sortirList([1,2,3,4,5,6,7,8,9])


# soal 2 (benar)
def flipLetters(stringToFlip):
    flippedStringLetters = []
    for letter in stringToFlip[::-1]:
        flippedStringLetters.append(letter)
    return flippedStringLetters

a = flipLetters("halo")
print(a)


# soal 3
def multiplyNum(numToMultiply):         # kesalahan: kurang 'numToMultiply'
    listOfNums = [int(num) for num in str(numToMultiply)]
    multipliedNum = 1
    for i in range(len(listOfNums)):    # kesalahan: 'listOfNums' harusnya 'len(listOfNums)'
        multipliedNum *= int(listOfNums[i])
    return multipliedNum

b = multiplyNum(234)
print(b)