name1:str=input("what is your name?")
name2:str=input("what is your last name?")
month=input("when is your birth month?")
day=input("what day where you born?")
year=input("what year where you born?")
birthday=month+","+day+","+year
major=input("what is your major?")
course1=input("what courses have you take?")
course2=input("How many courses have you taken in college?")
left2=input("how many courses do you have left")
print("STUDENT INFORMATION")
print("your name is " +name1+","+name2)
print("your birthday is "+str(birthday))
x=str(int(course2)+int(left2))
print("you have "+course2+ " out of "+x+" completed")
print("your major is "+major)
y=str(float(course2)/float(x)*100)
print("you have "+y+"% completed")# Write your code here :-)
