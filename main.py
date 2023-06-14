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

        if len(lineWordArray) > 1 and lineWordArray[usefulRowNumber].strip() != "" and i != 0:
            outputFileVar.write(lineWordArray[usefulRowNumber].strip() + "\n")

        i += 1

    inputFileVar.close()
    outputFileVar.close()


def convert_FT_to_CM(inputFile, outputFile):
    inputFileVar = open(inputFile, "r")
    outputFileVar = open(outputFile, "w")

    for line in inputFileVar:
        lineWordArray = line.split(".")

        if len(lineWordArray) > 1:
            firstDigit = float(lineWordArray[0].strip())
            secondDigit = float(lineWordArray[1].strip())

            result = round(((firstDigit * 12 + secondDigit) * 2.54), 1)
            outputFileVar.write(str(result) + "\n")

    inputFileVar.close()
    outputFileVar.close()

def combine_WNBA_NBA (WNBAcmFile, NBAcmFile, outputFile):
    WNBAcmFileVar = open(WNBAcmFile, "r")
    NBAcmFileVar = open(NBAcmFile, "r")
    outputFileVar = open(outputFile, "w")

    for line in WNBAcmFileVar:
        if line.strip() != "":
            outputFileVar.write(line)

    for line in NBAcmFileVar:
        if line.strip() != "":
            outputFileVar.write(line)

    WNBAcmFileVar.close()
    NBAcmFileVar.close()
    outputFileVar.close()


####################################################################################################################


extract_height_data("NHANESstats.txt", "NHANESheightCMfile.txt", "BMXHT")
extract_height_data("NBAstats.txt", "NBAheightFTfile.txt", "HEIGHT")
extract_height_data("WNBAstats.txt", "WNBAheightFTfile.txt", "HEIGHT")

convert_FT_to_CM("NBAheightFTfile.txt", "NBAheightCMfile.txt")
convert_FT_to_CM("WNBAheightFTfile.txt", "WNBAheightCMfile.txt")

combine_WNBA_NBA("WNBAheightCMfile.txt", "NBAheightCMfile.txt", "NBAcombinedCMfile.txt")
