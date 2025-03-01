# Exercsie 34 SD: Convert while loop to function

# i = 0      moved
numbers = []
def numbers_list(x, y):    # defined a function and added a new variable y --> i += y
    i = 0
    while i < x:   # replaced i < 6
        #print(f"At the top i is {i}")
        print("At the top of i is %d" % i)
        numbers.append(i)
        
        # i = i + 1  modified
        i += y   # added, this is the same as i = i + 1 , the increment by
        
        print("Numbers now: ", numbers)
        #print(f"At the bottom i is {i}")
        print("At the bottom of i is %d" % i)
    return numbers

numbers_list(6, 1)
print("The Numbers: ")

for num in numbers:
    print(num)
    

