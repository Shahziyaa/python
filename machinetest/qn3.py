details = [{'id' :1,'name':'rajesh'},
        {'id':2,'name':'rahul'},
        {'id':3,'name':'sruthi'}]

std_id = int(input("enter id :"))

for x in details:
    if x['id'] == std_id:
        print(f"id: {x['id']}, Name: {x['name']}")
        break
else:
    print("Student not found")
