for mk in range(1,6):
    mark = int(input(f"Enter mark of subject {mk} :- "))
    ttl = mark + mark + mark + mark + mark
    
print(f"Total marks of all subject :- {ttl} ")
avg = ttl/5

if avg >= 70:
    print("Distinction")
elif (avg >=60 and avg < 70):
    print("First class")
elif (avg >=50 and avg < 60):
    print("Second class")
elif (avg >=40 and avg < 50):
    print("Distinction")
elif (avg >=33 and avg < 40):
    print("pass class")
else:
    print("Beter lick! next time")
    
        