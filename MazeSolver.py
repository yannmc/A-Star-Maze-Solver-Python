#!/usr/local/bin/python3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# by Yann Morin Charbonneau - Github : @yannmc
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Initialisation of a dictionary to store the file's informations
file_infos = {"map": [], "startPos": {"x": "", "y": ""}, "endPos": {"x": "", "y": ""}, "Fx": [], "ManX": [], "aGx": [], "amountSteps": "", "reverseWinningPath": []}

#Function that takes the file'S content inside the "map" proprety of file_infos
def readFiles(num):
    tempStr = []
    tempInt = []
    #Read the file's content
    tempMap = open("./exercise" + num + ".txt", "r").readlines()

    #Loop through all the lines of the file's content
    for line in range(0, len(tempMap)):
        tempMap[line] = tempMap[line].replace("\n", "")
        tempStr.append(list(tempMap[line]))

    #Loop through all the numbers in each line of the file's content
    for line in range(0, len(tempStr)):
        for case in range(0, len(tempStr[line])):
            tempStr[line][case] = float(tempStr[line][case])

    #Store the information inside the "map" proprety of file_infos
    file_infos["map"] = tempStr

#Function to locate both START and END positions from the "map"
def locateStartEnd():

    #Loop through all the lines of the "map"
    for line in range(0, len(file_infos["map"])):

        #Loop through all the numbers of each line of the "map"
        for case in range(0, len(file_infos["map"][line])):

            #If the current case is the START position
            if file_infos["map"][line][case] == 2:

                #Save the X and Y coordinates of the START position
                file_infos["startPos"]["x"] = case
                file_infos["startPos"]["y"] = line

            #If the current case of the END position
            if file_infos["map"][line][case] == 3:

                #Save the X and Y coordinates of the END position
                file_infos["endPos"]["x"] = case
                file_infos["endPos"]["y"] = line

#Function that initializes the Manhattan map
def createManX():
    manhat = []

    #Loop through all the lines of the "map"
    for line in range(0, len(file_infos["map"])):
        row = []

        #Loop through all the numbers of each line of the "map"
        for case in range(0, len(file_infos["map"][line])):

            #Fill each case with |X1 - X2| + |Y1 - Y2|
            row.append((abs(case - file_infos["endPos"]["x"]) + abs(line - file_infos["endPos"]["y"])))
        manhat.append(row)

    #Store the Manhattan map in the "ManX" proprety of file_infos
    file_infos["ManX"] = manhat

#Function that initializes the Fx map
def createFx():
    Fx = []

    #Loop through all the lines of the "map"
    for line in range(0, len(file_infos["map"])):
        row = []

        #Loop through all the numbers of each line of the "map"
        for case in range(0, len(file_infos["map"][line])):

            #Insert -1 at the starting position coordinates in "Fx"
            if case == file_infos["startPos"]["x"] and line == file_infos["startPos"]["y"]:
                row.append(-1.0)

            #Insert FALSE everywhere else
            else: row.append(False)
        Fx.append(row)

    #Store the Fx map in the "Fx" proprety of the file_infos
    file_infos["Fx"] = Fx

#Function that initializes the aGx map
def createaGx(a):
    aGx = []

    #Loop through all the lines of the "map"
    for line in range(0, len(file_infos["map"])):
        row = []

        #Loop through all the numbers of each line of the "map"
        for case in range(0, len(file_infos["map"][line])):

            #Insert "alpha" * the value of "Fx" at the starting position in "aGx"
            if case == file_infos["startPos"]["x"] and line == file_infos["startPos"]["y"]:
                row.append(a * file_infos["ManX"][line][case])

            #Insert FALSE everywhere else
            else: row.append(False)
        aGx.append(row)

    #Store the aGx map in the "aGx" proprety of file_infos
    file_infos["aGx"] = aGx

#Function to go from the starting point, move around following our heuristic
def moveAround(a):
    steps = 0
    minimum = {"x": "", "y": "", "value": ""}
    isNumber = False

    #Check if the case to the left is a valid case
    def getLeft():
        if file_infos["map"][minimum["y"]][minimum["x"] - 1] != 1.0 and file_infos["aGx"][minimum["y"]][minimum["x"] - 1] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"]][minimum["x"] - 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else: file_infos["Fx"][minimum["y"]][minimum["x"] - 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"]][minimum["x"] - 1] = (a * file_infos["ManX"][minimum["y"]][minimum["x"] - 1]) + (file_infos["Fx"][minimum["y"]][minimum["x"] - 1])

    #Check if the case to the right is a valid case
    def getRight():
        if file_infos["map"][minimum["y"]][minimum["x"] + 1] != 1.0 and file_infos["aGx"][minimum["y"]][minimum["x"] + 1] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"]][minimum["x"] + 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else: file_infos["Fx"][minimum["y"]][minimum["x"] + 1] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"]][minimum["x"] + 1] = (a * file_infos["ManX"][minimum["y"]][minimum["x"] + 1]) + (file_infos["Fx"][minimum["y"]][minimum["x"] + 1])

    #Check if the case on top is a valid case
    def getUp():
        if file_infos["map"][minimum["y"] - 1][minimum["x"]] != 1.0 and file_infos["aGx"][minimum["y"] - 1][minimum["x"]] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"] - 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else: file_infos["Fx"][minimum["y"] - 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"] - 1][minimum["x"]] = (a * file_infos["ManX"][minimum["y"] - 1][minimum["x"]]) + (file_infos["Fx"][minimum["y"] - 1][minimum["x"]])

    #Check if the case on the bottom is a valid case
    def getDown():
        if file_infos["map"][minimum["y"] + 1][minimum["x"]] != 1.0 and file_infos["aGx"][minimum["y"] + 1][minimum["x"]] == False:
            if file_infos["Fx"][minimum["y"]][minimum["x"]] == - 1:
                file_infos["Fx"][minimum["y"] + 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 2
            else: file_infos["Fx"][minimum["y"] + 1][minimum["x"]] = file_infos["Fx"][minimum["y"]][minimum["x"]] + 1
            file_infos["aGx"][minimum["y"] + 1][minimum["x"]] = (a * file_infos["ManX"][minimum["y"] + 1][minimum["x"]]) + (file_infos["Fx"][minimum["y"] + 1][minimum["x"]])

    #While we're not on the end position, keep going
    while not file_infos["aGx"][file_infos["endPos"]["y"]][file_infos["endPos"]["x"]]:

        minimum = {"x": "", "y": "", "value": ""}

        #Loop through all the lines of the "map"
        for line in range(0, len(file_infos["map"])):

            #Loop through all the numbers of each line of the "map"
            for case in range(0, len(file_infos["map"][line])):

                #Check if current case is a number
                if isinstance(file_infos["aGx"][line][case], float):

                    #If we don't already have a minimum value, take the first one we find
                    if minimum["value"] == "":
                        minimum.update({"x": case, "y": line, "value": file_infos["aGx"][line][case]})

                    #If we already have one, check if the value is smaller that our minimum
                    elif file_infos["aGx"][line][case] < minimum["value"]:

                        #If it is, make it our new minimum
                        minimum.update({"x": case, "y": line, "value": file_infos["aGx"][line][case]})

        #If we don't have a minimum, it means that we're stuck and the map is IMPOSSIBLE
        if minimum["value"] == "":
            file_infos["numberSteps"] = "IMPOSSIBLE"
            file_infos["reverseWinningPath"] = "IMPOSSIBLE"
            return
        steps += 1

        #If the current case is in the middle columns
        if 0 < minimum["x"] < len(file_infos["map"][0]) - 1:
            getLeft()
            getRight()

        #If the current case is in the first column
        elif minimum["x"] == 0:
            getRight()

        #Id the current case is on the last column
        else:
            getLeft()

        #If the current case is on the middle rows
        if 0 < minimum["y"] < len(file_infos["map"]) - 1:
            getUp()
            getDown()

        #If the current case is on the first row
        elif minimum["y"] == 0:
            getDown()

        #If the current case is on the last row
        else:
            getUp()

        #The case we were previously on, becomes TRUE
        file_infos["aGx"][minimum["y"]][minimum["x"]] = True

    #Store the amount of steps required to find the exit in the "numberSteps" proprety of file_infos
    file_infos["numberSteps"] = steps

#Function to go from the END to the START using the shortest path possible
def trackBack():
    currentPosition = {"x": file_infos["endPos"]["x"],"y": file_infos["endPos"]["y"],"value": file_infos["Fx"][file_infos["endPos"]["y"]][file_infos["endPos"]["x"]]}
    while True:

        #If current file is IMPOSSIBLE, stop here
        if currentPosition["value"] == - 1 or file_infos["numberSteps"] == "IMPOSSIBLE":
            break
        minimum = {"x": "", "y": "", "value": ""}

        #If current position is not on first row
        if currentPosition["y"] != 0 and file_infos["aGx"][currentPosition["y"] - 1][currentPosition["x"]]:

            #If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] - 1, "value": file_infos["Fx"][currentPosition["y"] - 1][currentPosition["x"]]})

            #If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"] - 1][currentPosition["x"]] < minimum["value"]:
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] - 1, "value": file_infos["Fx"][currentPosition["y"] - 1][currentPosition["x"]]})

        #If current position is not on the first column
        if currentPosition["x"] != 0 and file_infos["aGx"][currentPosition["y"]][currentPosition["x"] - 1]:

            #If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"] - 1, "y": currentPosition["y"], "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] - 1]})

            #If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"]][currentPosition["x"] - 1] < minimum["value"]:
                minimum.update({"x": currentPosition["x"] - 1, "y": currentPosition["y"], "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] - 1]})

        if currentPosition["x"] < (len(file_infos["map"][0]) - 1) and file_infos["aGx"][currentPosition["y"]][currentPosition["x"] + 1]:

            #If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"] + 1, "y": currentPosition["y"], "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] + 1]})

            #If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"]][currentPosition["x"] + 1] < minimum["value"]:
                minimum.update({"x": currentPosition["x"] + 1, "y": currentPosition["y"], "value": file_infos["Fx"][currentPosition["y"]][currentPosition["x"] + 1]})

        if currentPosition["y"] < (len(file_infos["map"]) - 1) and file_infos["aGx"][currentPosition["y"] + 1][currentPosition["x"]]:

            #If we don't already have a minimum value, take the first one we see
            if minimum["value"] == "":
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] + 1, "value": file_infos["Fx"][currentPosition["y"] + 1][currentPosition["x"]]})

            #If we already have one, check if the value is smaller that our minimum
            elif file_infos["Fx"][currentPosition["y"] + 1][currentPosition["x"]] < minimum["value"]:
                minimum.update({"x": currentPosition["x"], "y": currentPosition["y"] + 1, "value": file_infos["Fx"][currentPosition["y"] + 1][currentPosition["x"]]})

        #Add the opposite direction to the "reverseWinningPath" proprety of file_infos
        if currentPosition["x"] < minimum["x"]: file_infos["reverseWinningPath"].append("W")
        elif currentPosition["x"] > minimum["x"]: file_infos["reverseWinningPath"].append("E")
        elif currentPosition["y"] > minimum["y"]: file_infos["reverseWinningPath"].append("S")
        else: file_infos["reverseWinningPath"].append("N")
        currentPosition = minimum

#Function to write the file containing the answer
def writeFile(num):
    textFile = open("./Result" + num + ".txt",'w')

    #If the file is IMPOSSIBLE to solve
    if file_infos["numberSteps"] == "IMPOSSIBLE":

        #Write "IMPOSSIBLE" in the file
        textFile.write(str(file_infos["reverseWinningPath"]))

    #If the file is solvable
    else:

        #Take the reverse of our "reverseWinningPath"
        file_infos["reverseWinningPath"].reverse()

        #Write it to the file
        textFile.write(str(''.join(file_infos["reverseWinningPath"])))
        textFile.write(str("\n"))

        #Write the amount of steps to the file
        textFile.write(str(file_infos["numberSteps"]))
    textFile.close()

#Our main from which we call all of our functions
def main():

    #Repeat for all 9 files
    for each_file in range(1,2):
        global file_infos
        file_infos = {"map": [], "startPos": {"x": "", "y": ""}, "endPos": {"x": "", "y": ""}, "Fx": [], "ManX": [], "aGx": [], "amountSteps": "", "reverseWinningPath": []}

        #Assign the correct "alpha" based on the exercise
        if 1 <= each_file <=  6: a = 1.0
        elif 7 <= each_file <= 8: a = 0.5
        else: a = 5.0

        #Call each functions in the correct order
        readFiles(str(each_file))
        locateStartEnd()
        createManX()
        createFx()
        createaGx(a)
        moveAround(a)
        trackBack()
        writeFile(str(each_file))

if __name__ == "__main__":
    main()
