working_days=int(input("How many working days do you have: "))
absent_days=int(input("How many days for absent: "))
attendance = ((working_days - absent_days)/working_days) * 100

if attendance < 75:
    print("Student cannot sit in exam")
else: 
    print("Student can sit in exam")

