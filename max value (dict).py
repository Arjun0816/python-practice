marks = {"maths": 87, "physics": 98,"chemistry": 95}
max_val = list(marks.values())[0]
for value in marks.values():
    if value > max_val:
       max_val = value
print("maximum value is : ",max_val)

