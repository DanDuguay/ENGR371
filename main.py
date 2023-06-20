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

def trim_data (inputFile, outputFile, trimValue):
    inputFileVar = open(inputFile, "r")
    outputFileVar= open(outputFile, "w")

    for line in inputFileVar:
        if float(line.strip()) > trimValue:
            outputFileVar.write(line)

    inputFileVar.close()
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

    plt.rc('axes', titlesize=30)
    plt.rc('axes', labelsize=30)
    plt.rcParams['figure.figsize'] = [graphSize, graphSize]

    plt.plot(dictionary.keys(), dictionary.values())

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

    plt.rc('axes', titlesize=30)
    plt.rc('axes', labelsize=30)
    plt.rcParams['figure.figsize'] = [graphSize, graphSize]

    plt.hist(y, bins=binAmount)
    plt.plot(dictionary.keys(), dictionary.values())

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
    print(inputFile + " variance: " + str(round(variance,1)))
    print("calculated Standard Deviation: " + str(calculate_standard_deviation(y, mean)) + "\n")

    PDF = calculate_normal_distribution(y, mean, standardDeviation)
    #plt.plot(dictionary.keys(), dictionary.values())

    plt.rc('axes', titlesize=30)
    plt.rc('axes', labelsize=30)
    plt.rcParams['figure.figsize'] = [graphSize, graphSize]

    plt.plot(y, PDF, color="red")

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

def find_median (inputFile):
    inputFileVar = open(inputFile, "r")
    lines = []
    count = 0

    for line in inputFileVar:
        if line.strip() != "":
            lines.append(line)

    if len(lines)%2 == 0:
        return float(lines[int(len(lines)/2)])
    else:
        return (float(lines[int(np.ceil(len(lines)/2))]) + float(lines[int(np.floor(len(lines)/2))]))/2


def calculate_probability (x, mean, standardDeviation):
    z_score = calculate_Z_score(x, mean, standardDeviation)
    #print("Probability of being less or equal to " + str(mean) + " cm tall is " + str(st.norm.cdf(z_score)))
    return st.norm.cdf(z_score)

def calculate_standard_deviation (x, mean):
    result = sum(((np.abs(x-mean))**2))
    standardDeviation = np.sqrt(result/len(x))
    return standardDeviation

def calculate_standard_deviation (inputFile):
    inputFileVar = open(inputFile, "r")
    x = [float(line.strip()) for line in inputFileVar]
    mean = np.mean(x)

    result = sum(((np.abs(x-mean))**2))
    standardDeviation = np.sqrt(result/len(x))

    inputFileVar.close()
    return standardDeviation

def count_players_in_height_range (inputFile, lowerLimit, upperLimit):
    inputFileVar = open(inputFile, "r")
    count = 0

    for line in inputFileVar:
        if float(line.strip()) > lowerLimit and float(line.strip()) <= upperLimit:
            count += 1

    inputFileVar.close()
    return count


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

trim_data("sortedNHANEScmFile.txt", "adjustedNHANEScmFile.txt", 146)


create_plot_graph("sortedNBAcmFile.txt", "Height", "Occurrences", "Plot Graph - NBA Height", 15, 2)
create_plot_graph("sortedNBAcmFile.txt", "Height", "Occurrences", "Plot Graph - NBA Height", 15, 2)
create_plot_graph("sortedWNBAcmFile.txt", "Height", "Occurrences", "Plot Graph - WNBA Height", 15, 2)
create_plot_graph("sortedNBAcombinedFile.txt", "Height", "Occurrences", "Plot Graph - NBA Combined Height", 15, 2)
create_plot_graph("sortedNHANEScmFile.txt", "Height", "Occurrences", "Plot Graph - NHANES Height", 22, 3)

create_histogram("sortedNBAcmFile.txt", "Height", "Occurrences", " Histogram - NBA Height", 15, 18)
create_histogram("sortedWNBAcmFile.txt", "Height", "Occurrences", "Histogram - WNBA Height", 15, 18)
create_histogram("sortedNBAcombinedFile.txt", "Height", "Occurrences", "Histogram - NBA Combined Height", 15, 18)
create_histogram("sortedNHANEScmFile.txt", "Height", "Occurrences", "Histogram - NHANES Height", 22, 40)

create_normal_distribution_graph("sortedNBAcmFile.txt", "Data Points", "Probability", "Probability Density - NBA Height", 15, 2)
create_normal_distribution_graph("sortedWNBAcmFile.txt", "Data Points", "Probability", "Probability Density - WNBA Height", 15, 2)
create_normal_distribution_graph("sortedNBAcombinedFile.txt", "Data Points", "Probability", "Probability Density - NBA Combined Height", 18, 2)
create_normal_distribution_graph("sortedNHANEScmFile.txt", "Data Points", "Probability", "Probability Density - NHANES Height", 25, 3)
create_plot_graph("adjustedNHANEScmFile.txt", "Height", "Occurrences", "Plot Graph - Adjusted NHANES Height", 22, 3)
create_histogram("adjustedNHANEScmFile.txt", "Height", "Occurrences", "Histogram - Adjusted NHANES Height", 22, 40)
create_normal_distribution_graph("AdjustedNHANEScmFile.txt", "Data Points", "Probability", "Probability Density - Adjusted NHANES Height", 25, 3)


print("NHANES mean: " + str(calculate_mean("sortedNHANEScmFile.txt")))
print("NHANES median: " + str(find_median("sortedNHANEScmFile.txt")))
print("NHANES standard deviation: " + str(calculate_standard_deviation("sortedNHANEScmFile.txt")))
print("NHANES variance: " + str(calculate_standard_deviation("sortedNHANEScmFile.txt")**2) + "\n")

print("Adjusted NHANES mean: " + str(calculate_mean("adjustedNHANEScmFile.txt")))
print("Adjusted NHANES median: " + str(find_median("adjustedNHANEScmFile.txt")))
print("Adjusted NHANES standard deviation: " + str(calculate_standard_deviation("adjustedNHANEScmFile.txt")))
print("Adjusted NHANES variance: " + str(calculate_standard_deviation("adjustedNHANEScmFile.txt")**2) + "\n")

print("NBA mean: " + str(calculate_mean("sortedNBAcmFile.txt")))
print("NBA median: " + str(find_median("sortedNBAcmFile.txt")))
print("NBA standard deviation: " + str(calculate_standard_deviation("sortedNBAcmFile.txt")))
print("NBA variance: " + str(calculate_standard_deviation("sortedNBAcmFile.txt")**2) + "\n")

print("WNBA mean: " + str(calculate_mean("sortedWNBAcmFile.txt")))
print("WNBA median: " + str(find_median("sortedWNBAcmFile.txt")))
print("WNBA standard deviation: " + str(calculate_standard_deviation("sortedWNBAcmFile.txt")))
print("WNBA variance: " + str(calculate_standard_deviation("sortedWNBAcmFile.txt")**2) + "\n")

print("WNBA/NBA combined mean: " + str(calculate_mean("sortedNBAcombinedFile.txt")))
print("WNBA/NBA combined median: " + str(find_median("sortedNBAcombinedFile.txt")))
print("WNBA/NBA combined standard deviation: " + str(calculate_standard_deviation("sortedNBAcombinedFile.txt")))
print("WNBA/NBA combined variance: " + str(calculate_standard_deviation("sortedNBAcombinedFile.txt")**2) + "\n")

print("With a mean/SD of 156.6/22.3, probability of being under 152.4 cm is " + str((calculate_probability(152.4, 156.6, 22.3))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being under 167.6 cm is " + str((calculate_probability(167.6, 156.6, 22.3))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being under 182.9 cm is " + str((calculate_probability(182.9, 156.6, 22.3))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being under 198.1 cm is " + str((calculate_probability(198.12, 156.6, 22.3))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being under 213.4 cm is " + str((calculate_probability(213.4, 156.6, 22.3))*100) + "%")

print("With a mean/SD of 156.6/22.3, probability of being over 152.4 cm but under 167.6 cm is " +
      str(((calculate_probability(167.6, 156.6, 22.3)) - (calculate_probability(152.4, 156.6, 22.3)))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being over 167.6 cm but under 182.9 cm is " +
      str(((calculate_probability(182.9, 156.6, 22.3)) - (calculate_probability(167.6, 156.6, 22.3)))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being over 182.9 cm but under 198.1 cm is " +
      str(((calculate_probability(198.1, 156.6, 22.3)) - (calculate_probability(182.9, 156.6, 22.3)))*100) + "%")
print("With a mean/SD of 156.6/22.3, probability of being over 198.1 cm but under 213.4 cm is " +
      str(((calculate_probability(213.4, 156.6, 22.3)) - (calculate_probability(198.1, 156.6, 22.3)))*100) + "%")

print("With a mean/SD of 156.6/22.3, probability of being over 213.4 cm is " + str((1-calculate_probability(213.4, 156.6, 22.3))*100) + "%\n")

print("With a mean/SD of 165.9/10.0, probability of being 152.4 cm or under is " + str((calculate_probability(152.4, 165.9, 10.0))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being under 167.6 cm is " + str((calculate_probability(167.6, 165.9, 10.0))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being under 182.9 cm is " + str((calculate_probability(182.9, 165.9, 10.0))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being under 198.1 cm is " + str((calculate_probability(198.12, 165.9, 10.0))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being under 213.4 cm is " + str((calculate_probability(213.4, 165.9, 10.0))*100) + "%")

print("With a mean/SD of 165.9/10.0, probability of being over 152.4 cm but under or equal to 167.6 cm is " +
      str(((calculate_probability(167.6, 165.9, 10.0)) - (calculate_probability(152.5, 165.9, 10.0)))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being over 167.6 cm but under or equal to 182.9 cm is " +
      str(((calculate_probability(182.9, 165.9, 10.0)) - (calculate_probability(167.7, 165.9, 10.0)))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being over 182.9 cm but under or equal to 198.1 cm is " +
      str(((calculate_probability(198.1, 165.9, 10.0)) - (calculate_probability(183.0, 165.9, 10.0)))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being over 198.1 cm but under or equal to 213.4 cm is " +
      str(((calculate_probability(213.4, 165.9, 10.0)) - (calculate_probability(198.2, 165.9, 10.0)))*100) + "%")
print("With a mean/SD of 165.9/10.0, probability of being over 213.4 cm but under or equal to 220.9 cm is " +
      str(((calculate_probability(220.9, 165.9, 10.0)) - (calculate_probability(213.4, 165.9, 10.0)))*100) + "%")

print("With a mean/SD of 165.9/10.0, probability of being over or equal to 221.0 cm is " + str((1-calculate_probability(221.0, 165.9, 10.0))*100) + "%\n")

print("Amount of NBA/WNBA players under 152.4 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 0, 152.4)))
print("Amount of NBA/WNBA players between 152.4 cm and 167.6 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 152.4, 167.6)))
print("Amount of NBA/WNBA players between 167.6 cm and 182.9 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 167.6, 182.9)))
print("Amount of NBA/WNBA players between 182.9 cm and 198.1 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 182.9, 198.1)))
print("Amount of NBA/WNBA players between 198.1 cm and 213.4 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 198.1, 213.4)))
print("Amount of NBA/WNBA players between 213.4 cm and 221.0 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 213.4, 220.9)))
print("Amount of NBA/WNBA players over 220.9 cm is " + str(count_players_in_height_range("sortedNBAcombinedFile.txt", 220.9, 99999)))