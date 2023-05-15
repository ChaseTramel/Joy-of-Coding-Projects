# A program that reads a CSV file and outputs statistical information about the data
# Chase Tramel aka Kasey Chase Littlepaws - https://github.com/ChaseLittlepaws

# Import libraries
import csv 
import statistics

# Assign an easier name to the file
csv = "Module One/Data Project Practice/sample_grades.csv"

# Set up arrays for each semester
spring = []
fall = []

# Read the file
file = open(csv)
for line in file:
    # print(line.rstrip())
    
    
file.close()