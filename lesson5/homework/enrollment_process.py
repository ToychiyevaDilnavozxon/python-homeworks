universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(uni_list):
    students = []
    tuition_fee = []
    
    for university in uni_list:
        students.append(university[1])  # Add the number of enrolled students
        tuition_fee.append(university[2])  # Add the tuition fee
    
    return students, tuition_fee

# Function to calculate the mean
def mean(lst):
    return sum(lst) / len(lst)

# Function to calculate the median
def median(lst):
    return statistics.median(lst)

# Get student enrollment and tuition fee lists
students, tuition_fee = enrollment_stats(universities)

# Calculate the total number of students and total tuition
total_students = sum(students)
total_tuition = sum(tuition_fee)

# Calculate the mean and median of students and tuition
mean_students = mean(students)
median_students = median(students)
mean_tuition = mean(tuition_fee)
median_tuition = median(tuition_fee)

# Print the results in the desired format
print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}")
print()
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("******************************")