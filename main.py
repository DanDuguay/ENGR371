def extract_height_data(inputFile, outputFile, column_name):
    i = 0
    j = 0
    usefulRowNumber = 0
    inputFileVar = open(inputFile, "r")
    outputFileVar = open(outputFile, "w")

    for line in inputFileVar:
        lineWordArray = line.split(",")

        if i == 0:
            for word in lineWordArray:
                if word.strip() == column_name:
                    usefulRowNumber = j
                j += 1

        if len(lineWordArray) > 1 and lineWordArray[usefulRowNumber] != "" and i != 0:
            outputFileVar.write(lineWordArray[usefulRowNumber] + "\n")

        i += 1

    inputFileVar.close()
    outputFileVar.close()

####################################################################################################################


extract_height_data("NHANESstats.txt", "NHANESheightCMfile.txt", "BMXHT")
extract_height_data("NBAstats.txt", "NBAheightFTfile.txt", "HEIGHT")
extract_height_data("WNBAstats.txt", "WNBAheightFTfile.txt", "HEIGHT")
