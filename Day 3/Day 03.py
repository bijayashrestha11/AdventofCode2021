with open('F:\Study Material\Extra\Advent of Code\Day 3\input.txt') as f:
    lines = f.readlines()
 
#Part 1 of the DAY 3 OF THE Advent of Coding   
nums = [ str(line.strip()) for line in lines ]
leng = len(nums[0])
c0 = c1 = 0
gamma = ' '
alpha = ' '
for k in range(leng):
    for i in range(len(nums)):
        if nums[i][k] == '0':
            c0 += 1
        else:
            c1 += 1 
    
    print(c0, c1)
    if c0<=c1:
        alpha += '0'
        gamma += '1'
    else:
        alpha += '1' 
        gamma += '0' 
    c0 = c1 = 0
print(gamma, alpha)      
gamma =int(gamma,2)
alpha = int(alpha,2)
print("The power consumption is ", alpha * gamma)

