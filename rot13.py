rot = input("Type Here: ")
writeToInput = input("Write or Read?")
writeTo = False
if writeToInput == "Write":
    writeTo = True

letList = []
rotList = []
finalString = ''

for x in range(len(rot)):
    letList.append(rot[x].lower())
for z in letList:
    if ord(z) < 97 or ord(z) >= 123:
        rotList.append(z)
        continue
    if ord(z) < 110:
        rotted = 13 + ord(z)
    if ord(z) >= 110:
        rotted = ord(z) - 13
    rotList.append(chr(rotted))
for x in rotList:
    finalString += x
if writeTo == True:
    rotText = open("rotted-text.txt", 'a')
    rotText.write("\n")
    rotText.write("***")
    rotText.write(finalString)
print(finalString)
