def main():
	wordListPath="top-1m.csv"

	# Prompt for where to write the data
	writePathForVowels = input("Write the vowels output where?\r\n")
	writePathForLengths = input("Write the lengths output where?\r\n")
	writePathForAlphas = input("Write the alphas output where?\r\n")
	writePathForCapitals = input("Write the capitals output where?\r\n")

	# Read the words, calc basic info, throw into lists
	try:
		with open(wordListPath,"r") as readFile:
			# Calc percents
			print("Calculating vowel percents...")
			vowelPercentsList = generateCharClassPercentsForFile("aeiouAEIOU",readFile)
			print("Calculating alpha percents...")
			alphaPercentsList = generateCharClassPercentsForFile("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",readFile)
			print("Calculating capitals percents...")
			capitalPercentsList = generateCharClassPercentsForFile("ABCDEFGHIJKLMNOPQRSTUVWXYZ",readFile)
			print("Calculating word lengths...")
			wordLengthsList = generateWordLengthsForFile(wordListPath)

			# Write to file
			print("Writing to file...\r")
			exportWordStatsToCSV(vowelPercentsList,writePathForVowels)
			exportWordStatsToCSV(alphaPercentsList,writePathForAlphas)
			exportWordStatsToCSV(capitalPercentsList,writePathForCapitals)
			exportWordStatsToCSV(wordLengthsList,writePathForLengths)
	except IOError:
		print("Error opening file for reading.")
#	vowelPercentsList = generateVowelPercentsForFile(wordListPath)
#	wordLengthsList = generateWordLengthsForFile(wordListPath)
	# REWRITE REWRITE NEED TO OPEN AND CLOSE FILE ONCE REWRITE REWRITE

#	print("Writing to file...\r")

	# Write lists to files
#	exportWordStatsToCSV(vowelPercentsList,writePathForVowels)
#	exportWordStatsToCSV(wordLengthsList,writePathForLengths)

	print("Done.\r")

# Returns the count of chars in a word that are vowels
def vowelCount(word):
    vowels=list("aeiouAEIOU")
    vowelCount = sum(word.count(vowel) for vowel in vowels)
    return vowelCount

# Returns the count of alpha chars in a word
def alphaCount(word):
    alphas=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphaCount = sum(word.count(alpha) for alpha in alphas)
    return alphaCount

# Returns the count of capital chars in a word
def capitalCount(word):
	capitals=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	capitalCount = sum(word.count(capital) for capital in capitals)
	return capitalCount

# Returns a list of the percents of capital chars in words in the given inFileName
def generateCapitalPercentsForFile(inFile):
	wordStats = []

	for line in inFile:
		capitalsInWord = capitalCount(line)
		wordLength = len(line.strip()) # Removing newline char
		capitalPercent = capitalsInWord / wordLength
		wordStats.append(capitalPercent)

	return wordStats

# Returns a list of the percents of alpha chars in words in the given inFileName
def generateAlphaPercentsForFile(inFile):
	wordStats = []

	for line in inFile:
		alphasInWord = alphaCount(line)
		wordLength = len(line.strip()) # Removing newline char
		alphaPercent = alphasInWord / wordLength
		wordStats.append(alphaPercent)

	return wordStats

# Calculates the percent of vowels in a word, appends to list, returns list
def generateVowelPercentsForFile(inFileName):
	wordStats = []

	try:
		with open(inFileName,"r") as inputFile:
			for line in inputFile:
				vowelsInWord = vowelCount(line)
				wordLength = len(line.strip()) # Removing newline char
				vowelPercent = vowelsInWord / wordLength
				wordStats.append(vowelPercent)
	except IOError:
		print("Error opening the provided file {}".format(inFileName))

	return wordStats

# Finds length for words in given inFileName, appends to list, returns list
def generateWordLengthsForFile(inFileName):
	wordStats=[]

	try:
		with open(inFileName,"r") as inputFile:
			for line in inputFile:
				wordLength = len(line.strip())
				wordStats.append(wordLength)
	except IOError:
		print("Error opening the provided file {}".format(inFileName))

	return wordStats

# Counts the occurrences of any char in string "charClass" in the given "word"
def countCharClassInWord(charClass,word):
	charClassList=list(charClass)
	charClassCount = sum(word.count(char) for char in charClassList)
	return charClassCount

# For each word in inFile, calculate the percent of chars that are of charClass.
# Percents are put into a list, and returned.
def generateCharClassPercentsForFile(charClass,inFile):
	wordStats = []

	for line in inFile:
		line = line.strip() # Remove newline char
		charsInWord = countCharClassInWord(charClass,line)
		wordLength = len(line)
		charClassPercent = charsInWord / wordLength
		wordStats.append(charClassPercent)

	inFile.seek(0)
	return wordStats

# Exports a given list as a csv to the given path
def exportWordStatsToCSV(inStats,outFile):
	try:
		with open(outFile,"w") as outputFile:
			for stat in inStats:
				outputFile.write(str(stat)+"\n")
	except IOError:
		print("Error opening the provided file {}".format(outputFile))

if __name__ == '__main__':
    main()