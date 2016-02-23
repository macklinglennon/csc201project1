#project1 - half pyramid
#ask user how many levels they would like the half pyramid to have

height = int(input("How many levels would you like the half pyramid to have"))

begin = 0
step = +1
end = height+1

for k in range(begin, end, step):
    print("*" * k)


#project2 - full pyramid
#ask user how many levels they would like the full pyramid to have

height = int(input("How many levels would you like the full pyramid to have"))

begin = 0
step = +1
end = height+1

for k in range(begin, end, step):
    print(" " * (height-k) + "*" * k + "*" * (k-1))

#project3 - corrections
#both of my pyramids still works with two digit numbers so I am n/a
#for project 3


#project4 - rotated parabola
#ask the user for the range of x values to be used

width = int(input("Enter range of x values to be used in the form of [a, b]:"))




