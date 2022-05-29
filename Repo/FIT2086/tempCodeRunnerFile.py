three = [7, 8, 9, 10] 
sum = 0
for _ in range(3):
    for item in one:
        sum += item/24
    for item2 in two:
        sum += item2*2/24

    for item3 in three:
        sum += item3*3/24

print(sum)