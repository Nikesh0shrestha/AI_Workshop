# Tuples cannnot be changed after the creation

student_records = ("Alice",20,8505,"computer science")
print("Student Records Tuples:", student_records)


# Accessing Tuples Elements

print("Name:",student_records[0])
print("Age:",student_records[1])

#Tuples unpacking
name, age, score, department, = student_records
print("\nUnpackedd:", name, "is", age, "years old , scored", score, "in", department)



# Sets automatically remove duplicates
course_A = {"Alice","Bob","Charlie","Diana"}
course_B = {"Charlie","Diana","Eye","Frank"}

print("Couurse_A Student",course_A)
print("Couurse_B Student",course_B)

# set operations (great for finding overlaps)
print("\nStudents in both course:",course_A & course_B)
print("Student in either course:",course_A | course_B)
print("Only in course_A",course_A - course_B)
print("Only in one course",course_A ^ course_B)

# Remove Duplicates form list using set  
scores_with_duplicates = {85,92,85,78,92,95,85}
unique_scores = list(set(scores_with_duplicates))
print("\nOriginal scores:",scores_with_duplicates)
print("Unique scores:",unique_scores)
