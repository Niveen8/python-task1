
#variable
name = input("Enter your name: ")
age = input("Enter your age: ")
city =input("Enter your city: ")
with open("file.txt","w") as f:
 f.write("Name: " + name + "\n")
 f.write("Age: " + age + "\n")
 f.write("city: " + city + "\n")
with open("file.txt", "r") as f:
print(f.read())





