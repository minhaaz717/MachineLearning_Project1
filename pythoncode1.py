import statistics
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))

#adding min and max age again to the list
ages.append(max(ages))
ages.append(min(ages))
print(ages)

#finding median of ages
median_of_ages=statistics.median(ages)
print(median_of_ages)

#finding average of ages
average_of_ages=sum(ages)/len(ages)
print(average_of_ages)

#finding range of ages
range_of_ages= max(ages)-min(ages)
print(range_of_ages)




