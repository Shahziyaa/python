arra = [{'id' :1,'name':'rajesh'},
        {'id':2,'name':'rahul'},
        {'id':3,'name':'sruthi'}]

std_id = int(input("enter id"))

found = False
for student in arra:
    if student['id'] == std_id:
        print(f"Name: {student['name']}")
        found = True
        break
if not found:
    print("Student not found")