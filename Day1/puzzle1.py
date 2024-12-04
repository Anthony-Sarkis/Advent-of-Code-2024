#Part 1

# Data File Path
file_path = 'Day1\\data.txt'

# Initialize variables
left_list = []
right_list = []
total_distance = 0

# Read the file and separate the data into left and right lists
with open(file_path, 'r') as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()

# Compute the total distance between paired numbers
for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

print(f"Distance Total: {total_distance}")

####################################################################

#Part 2

# Compute similarity score
similarity_score = 0

# Iterate through each element in the left list
for element_l in left_list:
    # Count occurrences of element_l in the right list
    copy_counter = right_list.count(element_l)
    
    # Calculate the contribution to the similarity score
    temp_calculation = element_l * copy_counter
    
    # Add the contribution to the total similarity score
    similarity_score += temp_calculation

print(f"Similarity Score: {similarity_score}")
