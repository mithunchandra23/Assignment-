marks = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78,
    "Diana" : 90,
    "Ethan" : 88
}
name = input("Enter the student's name: ")

if name in marks:
    print(name, "'s marks: ", marks[name])
    
else:
    print("Student not found")
 