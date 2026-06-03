#exercise lvl 1
lst = []
print(lst)
lst = [1,2,3,4,5,6,7]
print(lst)
print(len(lst))
print(lst[0])
print(lst[int(len(lst)/2)])
print(lst[len(lst)-1])

#exercise lvl 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print('min = ',ages[0],' max = ', ages[len(ages)-1])
if len(ages)%2==0:
    median = ages[int(len(ages)/2)-1] + ages[int(len(ages)/2)]
    median = int(median/2)
else:
    median = ages[int(len(ages)/2)]

print('Median = ',median)
print('Range = ', ages[len(ages)-1]-ages[0])
avg = int(sum(num for num in ages) / len(ages))
print('Average = ',avg)
print('Negative Deviation = ', abs(min(ages)-avg))
print('Positive Deviation = ', abs(max(ages)-avg))