# -------------------------------
# break Statement : it is used to terminate the loop
print("Break Statement : ")
for i in range(1,11):
    if i == 5:
        break;
    print(i)

# -------------------------------
# continue statement : it prints the all the values except that perticular condition
print("Continue Statement : ")
for i in range(1,11):
    if i==6:
        continue
    print(i)

# -------------------------------
# pass statement : it is filler means we have to implement function but we dont know the logic so if we implement it directly so it will throw error so when we use pass statement it doesnt throw the error
print("Pass Statement : ")
for i in range(1,11):
    pass