# A program that reads a CSV file and outputs statistical information about the data
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws
import csv 
import statistics

data = {'Fall': [], 'Spring': []}

# grab the data from the file
def getData(file):
    #Set up a list with empty lists
    # Read the file
    reader = csv.reader(file)
    for row in reader:
        name, semester, grade = row
        semester = findSemester(semester)
        data[semester].append(float(grade))    
    file.close()

# find the semester from the semester data
# this only works if the years are the same
def findSemester(semester):
    semester = semester.strip().lower()
    if "fall" in semester:
        return "Fall"
    elif "spring" in semester:
        return "Spring"
    else:
        raise ValueError("Something is wrong with the semester")

# calculate and print the statistics
def calculateStats(data):
    print("Mean: " + str(round(statistics.mean(data),2)))
    print("Median: " + str(round(statistics.median(data),2)))
    print("Standard Deviation: " + str(round(statistics.stdev(data),2)))
    

# Assign an easier name to the file
filename = "Module One/Data Project Practice/sample_grades.csv"

# open the file and get the data
with open(filename, 'r') as file:
    getData(file)

# print the statistics with labels
print("Statistics for Fall:")
calculateStats(data["Fall"])
print("\n")
print("Statistics for Spring:")
calculateStats(data["Spring"])