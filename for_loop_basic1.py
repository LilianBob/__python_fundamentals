# Basic - Print all integers from 0 to 150.
for int in range (1, 151, 1):
    print (int)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range (5,1001, 5):
    print (i)

# outlier = 1
# print(outlier)
# for i in range (5, 101, 5):
#     print(i)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for int in range (1, 101, 1):
    if int%5==0:
        print("Coding")
    if int%5==0:
        print ("Coding " + "Dojo")
    print (int)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for int in range (1, 500000, 1):
    if int%2==1:
        sum += int 
print (sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for count in range (2018, -1, -4):
    print(count)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
multi = 3
for counter in range (lowNum, highNum+1, 1):
    if counter%multi==0:
        print(counter)