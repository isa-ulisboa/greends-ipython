# ASSIGNMENT # 5 - Handling an ASCII file

# Open the file
file = open("GreenDSfile1.csv", 'r')
file.close

# read lines into list
listLines = file.readlines()

# Count the number of lines in the file (or list)
nLines = len(listLines)
file.close

# Print the number of lines
print("number of Lines:", nLines)

# Create a new file named GreenDSfile1_sample500k.csv to store the first 500 000 lines
fsample500k = open("GreenDSfile1_sample500k.csv", 'w')
for i in range(500000):
    fsample500k.writelines(listLines[i])
fsample500k.close()

# Create a new file named GreenDSfile1_samplelast100.csv to store the last 100 lines
fsample100 = open("GreenDSfile1_samplelast100.csv", 'w')
for i in range(100):
    fsample100.writelines(listLines[-i-1])
fsample100.close()