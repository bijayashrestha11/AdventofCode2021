with open ('input1.txt') as f:
    lines = f.readlines()

nums = [ int(line.strip()) for line in lines ]
#print(nums)

#Part 1 of the Advent of Coding Day 1
count = 0
for i in range (1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1;
print("Value of count of Part 1 is = ", count)


#Part 2 of the Advent of Code Day 1
sum =0
arr = []
a = 3
for i in range(len(nums)-2):
    sum = 0
    for j in range(i, a):
        sum += nums[j]
    arr.append(sum)
    a += 1

count = 0
for i in range(len(arr)):
    if arr[i] > arr[i-1]:
        count += 1
print("Value of count of Part 2 is =", count)
        