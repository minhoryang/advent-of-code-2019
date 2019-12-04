r = (245318, 765747)

results = []
for num in range(r[0]+1, r[1]):
    strnum = str(num)
    is_increasing = True
    found_same_number = False
    for i in range(5):
        # Check1
        if is_increasing and strnum[i] <= strnum[i+1]:
            pass
        else:
            is_increasing = False
        # Check2
        if not found_same_number and strnum[i] == strnum[i+1]:
            found_same_number = True
    if is_increasing and found_same_number:
        results.append(num)

print(len(results))

###############################
