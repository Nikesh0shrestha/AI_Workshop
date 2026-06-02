name = "Nikesh Shrestha"
faculty = "Computer Science"
dob = "03/07/2004"
age = 22

print(f"Hello this is {name}. I am {age} years old.")

#data types 

print(f"Type of name:{type(name)}")
print(f"Type of name:{type(faculty)}")
print(f"Type of age:{type(age)}")


# swap variables 

x, y = 10,20
print("Before swap x = ",x, "y = ", y)
x,y = y,x 
print("After Swap: x = ",x, "y=",y)

# list can hold multiple data types 
student_info = ["Charlie",21,88.00]
name, age, score, = student_info

print("Unpacked ", name, age, score)

name, *age =  student_info
print("Name:", name , "age and score : ", age)

# creating  list

student_name = ["Alice", "Bob", "Charlie","Arbin"]

print("First student:",student_name[0])
print("Last Student:",student_name[-1])
print("First 3 student:",[0,3])
print("Every seconnd student:",student_name[::2])

# List Operations

student_name.append("Eva")
print("After addin Eva:", student_name)

student_name.insert(1,"Rohan")
print("After inserting Rohan",student_name)

student_name.remove("Eva")
print("After removing Eva:",student_name)

# list comprehension(poserul  feature)
student_score = [85,67,95,50]
passing_score = [score for score in student_score if score >=80]
print("/Passing scores (>=80):", passing_score)




