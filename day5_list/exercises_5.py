ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
sort_age_last_value = ages[-1]
print(sort_age_last_value)
ages.append(ages[0])
ages.append(sort_age_last_value)
ages.sort()

print(ages)
print(len(ages))
median_value = int(len(ages)/2) 
median = ages[median_value]
print(median)

average = sum(ages)/len(ages)
print(average)


