NHANESfile = open("NHANESstats.txt", "r")
NBAfile = open("NBAstats.txt", "r")
WNBAfile = open("WNBAstats.txt", "r")
NHANESheightCMfile = open("NHANESheightCMfile.txt", "w")
NBAheightFTfile = open("NBAheightFTfile.txt", "w")
WNBAheightFTfile = open("NBAheightFTfile.txt", "w")

def extract_height_data(file, column_name):
    i = 0
    j = 0
    usefulRowNumber = 0

    for line in file:
        lineWordArray = line.split(",")


i = 0
j = 0
usefulRowNumber = 0
# Extracting the BMXHT column from the NHANES survey data, and saving it in a separate file.
for line in NHANESfile:
    lineWordArray = line.split(",")

    if i == 0:
        for word in lineWordArray:
            if word.strip() == "BMXHT":
                usefulRowNumber = j
            j += 1

    if len(lineWordArray) > 2 and lineWordArray[usefulRowNumber] != "":
        NHANESheightCMfile.write(lineWordArray[usefulRowNumber] + "\n")

    i += 1

i = 0
j = 0
# Extracting the HEIGHT column from the NBA data, saving it to a separate file.
for line in NBAfile:
    lineWordArray = line.split(",")

    if i == 0:
        for word in lineWordArray:
            if word.strip() == "HEIGHT":
                usefulRowNumber = j
            j += 1
    if len(lineWordArray) > 2 and lineWordArray[usefulRowNumber] != "":
        NBAheightFTfile.write(lineWordArray[usefulRowNumber] + "\n")

    i += 1

i = 0
j = 0

# Extracting the HEIGHT column from the NBA data, saving it to a separate file.
for line in NBAfile:
    lineWordArray = line.split(",")

    if i == 0:
        for word in lineWordArray:
            if word.strip() == "HEIGHT":
                usefulRowNumber = j
            j += 1
    if len(lineWordArray) > 2 and lineWordArray[usefulRowNumber] != "":
        NBAheightFTfile.write(lineWordArray[usefulRowNumber] + "\n")




NBAheightFTfile.close()
WNBAheightFTfile.close()
NHANESheightCMfile.close()
NHANESfile.close()
NBAfile.close()
WNBAfile.close()

