import matplotlib.pyplot as plt

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

# general population sample does not differentiate between male and female, so we will combine NBA and WNBA to match.
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

# mean = 1/n * [sum of values from 1 to n]
def calculate_mean (inputFile):
    inputFileVar = open(inputFile, "r")
    sum = 0
    lineCount = 0

    for line in inputFileVar:
        if line.strip() != "":
            sum += float(line)
            lineCount += 1

    print(sum)
    print(lineCount)
    print("\n")

    return sum / lineCount

def create_graph (inputFile, xAxis_name, yAxis_name, plotTitle):
    inputFileVar = open(inputFile, "r")
    y = [float(line.strip()) for line in inputFileVar]
    x = [float(i) for i in range(1, len(y)+1)]

    plt.plot(x,y)
    plt.xlabel(xAxis_name)
    plt.ylabel(yAxis_name)
    plt.title(plotTitle)
    plt.show()

    inputFileVar.close()

def sort_file (inputFile, outputFile):
    inputFileVar = open(inputFile, "r")
    outputFileVar = open(outputFile, "w")

    lines = [line for line in inputFileVar]
    lines.sort(key=float)

    for line in lines:
        outputFileVar.write(str(line))

    inputFileVar.close()
    outputFileVar.close()



####################################################################################################################


extract_height_data("NHANESstats.txt", "NHANESheightCMfile.txt", "BMXHT")
extract_height_data("NBAstats.txt", "NBAheightFTfile.txt", "HEIGHT")
extract_height_data("WNBAstats.txt", "WNBAheightFTfile.txt", "HEIGHT")

convert_FT_to_CM("NBAheightFTfile.txt", "NBAheightCMfile.txt")
convert_FT_to_CM("WNBAheightFTfile.txt", "WNBAheightCMfile.txt")

combine_WNBA_NBA("WNBAheightCMfile.txt", "NBAheightCMfile.txt", "NBAcombinedCMfile.txt")

NBAmean = round(calculate_mean("NBAheightCMfile.txt"), 1)
WNBAmean = round(calculate_mean("WNBAheightCMfile.txt"), 1)
combinedMean = round(calculate_mean("NBAcombinedCMfile.txt"), 1)
NHANESmean = round(calculate_mean("NHANESheightCMfile.txt"), 1)

print("NBA mean: " + str(NBAmean) + "\n")
print("WNBA mean: " + str(WNBAmean) + "\n")
print("Combined NBA/WNBA mean: " + str(combinedMean) + "\n")
print("NHANES mean: " + str(NHANESmean) + " (NOTE: Sample age range is 0 to 150 years old)\n")

sort_file("NBAheightCMfile.txt", "sortedNBAcmFile.txt")
sort_file("WNBAheightCMfile.txt", "sortedWNBAcmFile.txt")
sort_file("NBAcombinedCMfile.txt", "sortedNBAcombinedFile.txt")
sort_file("NHANESheightCMfile.txt", "sortedNHANEScmFile.txt")

create_graph("sortedNBAcmFile.txt", "Number of People", "Height", "NBA Height In cm")
