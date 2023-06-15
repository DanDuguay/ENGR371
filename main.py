import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

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

    return sum / lineCount

def create_plot_graph (inputFile, xAxis_name, yAxis_name, plotTitle, graphSize, xAxis_ticks):
    inputFileVar = open(inputFile, "r")

    y = [float(line.strip()) for line in inputFileVar]

    dictionary = {i:y.count(i) for i in y}
    x = [float(i) for i in range(1, len(y)+1)]

    plt.plot(dictionary.keys(), dictionary.values())

    plt.rc('axes', titlesize=30)
    plt.rc('axes', labelsize=30)
    plt.rcParams['figure.figsize'] = [graphSize, graphSize]
    plt.xlabel(xAxis_name)
    plt.ylabel(yAxis_name)
    plt.title(plotTitle)
    plt.xlim(list(dictionary)[0],list(dictionary)[-1])
    plt.ylim(0)
    plt.xticks(np.arange(list(dictionary)[0], list(dictionary)[-1]+1, xAxis_ticks))

    plt.show()
    inputFileVar.close()

def create_histogram (inputFile, xAxis_name, yAxis_name, plotTitle, graphSize, binAmount):
    inputFileVar = open(inputFile, "r")

    y = [float(line.strip()) for line in inputFileVar]

    dictionary = {i: y.count(i) for i in y}
    x = [float(i) for i in range(1, len(y) + 1)]

    plt.hist(y, bins=binAmount)
    plt.plot(dictionary.keys(), dictionary.values())

    plt.rc('axes', titlesize=30)
    plt.rc('axes', labelsize=30)
    plt.rcParams['figure.figsize'] = [graphSize, graphSize]
    plt.xlabel(xAxis_name)
    plt.ylabel(yAxis_name)
    plt.title(plotTitle)

    plt.show()
    inputFileVar.close()

def create_normal_distribution_graph (inputFile, xAxis_name, yAxis_name, plotTitle, graphSize, xAxis_ticks):
    inputFileVar = open(inputFile, "r")

    y = [float(line.strip()) for line in inputFileVar]

    dictionary = {i: y.count(i) for i in y}
    x = [float(i) for i in range(1, len(y) + 1)]

    mean = np.mean(y)
    print(inputFile + " mean: " + str(round(mean,1)))
    standardDeviation = np.std(y)
    print(inputFile + " standard deviation: " + str(round(standardDeviation,1)))
    variance = standardDeviation**2
    print(inputFile + " variance: " + str(round(variance,1)) + "\n")

    PDF = calculate_normal_distribution(y, mean, standardDeviation)
    plt.plot(y, PDF, color="red")
    #plt.plot(dictionary.keys(), dictionary.values())

    plt.rc('axes', titlesize=30)
    plt.rc('axes', labelsize=30)
    plt.rcParams['figure.figsize'] = [graphSize, graphSize]
    plt.xlabel(xAxis_name)
    plt.ylabel(yAxis_name)
    plt.title(plotTitle)
    plt.xticks(np.arange(list(dictionary)[0], list(dictionary)[-1] + 1, xAxis_ticks))

    plt.show()
    inputFileVar.close()

# normal distribution = (1/pi*sd)exp[
def calculate_normal_distribution (x, mean, standardDeviation):
    #probabilityDensity = ((np.pi * standardDeviation) * np.exp(-0.5 * ((x-mean)/standardDeviation)**2))
    probabilityDensity = (1 / (standardDeviation * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) / (2 * standardDeviation)) ** 2)
    return probabilityDensity

def calculate_Z_score (x, mean, standardDeviation):
    z_score = (x-mean)/standardDeviation
    return z_score

def sort_file (inputFile, outputFile):
    inputFileVar = open(inputFile, "r")
    outputFileVar = open(outputFile, "w")

    lines = [line for line in inputFileVar]
    lines.sort(key=float)

    for line in lines:
        outputFileVar.write(str(line))

    inputFileVar.close()
    outputFileVar.close()

def calculate_probability (x, mean, standardDeviation):
    z_score = calculate_Z_score(x, mean, standardDeviation)
    print("Probability of being less or equal to " + str(mean) + " cm tall is " + str(round(st.norm.cdf(z_score),1)))



####################################################################################################################


extract_height_data("NHANESstats.txt", "NHANESheightCMfile.txt", "BMXHT")
extract_height_data("NBAstats.txt", "NBAheightFTfile.txt", "HEIGHT")
extract_height_data("WNBAstats.txt", "WNBAheightFTfile.txt", "HEIGHT")

convert_FT_to_CM("NBAheightFTfile.txt", "NBAheightCMfile.txt")
convert_FT_to_CM("WNBAheightFTfile.txt", "WNBAheightCMfile.txt")

combine_WNBA_NBA("WNBAheightCMfile.txt", "NBAheightCMfile.txt", "NBAcombinedCMfile.txt")

sort_file("NBAheightCMfile.txt", "sortedNBAcmFile.txt")
sort_file("WNBAheightCMfile.txt", "sortedWNBAcmFile.txt")
sort_file("NBAcombinedCMfile.txt", "sortedNBAcombinedFile.txt")
sort_file("NHANESheightCMfile.txt", "sortedNHANEScmFile.txt")

create_plot_graph("sortedNBAcmFile.txt", "Height", "Occurrences", "Plot Graph - NBA Height", 15, 2)
create_plot_graph("sortedWNBAcmFile.txt", "Height", "Occurrences", "Plot Graph - WNBA Height", 15, 2)
create_plot_graph("sortedNBAcombinedFile.txt", "Height", "Occurrences", "Plot Graph - NBA Combined Height", 15, 2)
create_plot_graph("sortedNHANEScmFile.txt", "Height", "Occurrences", "Plot Graph - NHANES Height", 22, 3)

create_histogram("sortedNBAcmFile.txt", "Height", "Occurrences", " Histogram - NBA Height", 15, 18)
create_histogram("sortedWNBAcmFile.txt", "Height", "Occurrences", "Histogram - WNBA Height", 15, 18)
create_histogram("sortedNBAcombinedFile.txt", "Height", "Occurrences", "Histogram - NBA Combined Height", 15, 18)
create_histogram("sortedNHANEScmFile.txt", "Height", "Occurrences", "Histogram - NHANES Height", 22, 40)

create_normal_distribution_graph("sortedNBAcmFile.txt", "Data Points", "Probability Density", "Normal Distribution - NBA Height", 15, 2)
create_normal_distribution_graph("sortedWNBAcmFile.txt", "Data Points", "Probability Density", "Normal Distribution - WNBA Height", 15, 2)
create_normal_distribution_graph("sortedNBAcombinedFile.txt", "Data Points", "Probability Density", "Normal Distribution - NBA Combined Height", 15, 2)
create_normal_distribution_graph("sortedNHANEScmFile.txt", "Data Points", "Probability Density", "Normal Distribution - NHANES Height", 22, 3)

print("probability of being over 213.4 cm tall is " + str(1-calculate_probability(213.4, 200.5, 8.6)))
