# sort function that sorts a numerical list
def sort_list(l: list):

    n = len(l)  # length of l
    # two counter variables used for the nested while loop below
    i = 0   
    

    # nested while loops that traverse through entire array, swapping the current element with the next element if the next element is smaller
    while i < n:
        j = 0
        while j < (n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            j+=1
        i+=1

    # returns sorted list
    return l

# testing sort_list()
input1 = [1, 3, 2, 7]
print("Printing input1")    
print(*sort_list(input1))   # should print '1 2 3 7'
input2 = [3, 2, 4, 89]
print("Printing input2")
print(*sort_list(input2))   # should print '2 3 4 89'
input3 = 1
print("Printing input3")
print(*sort_list(input3))   # "NOT A LIST"
input4 = "Happy New Year"
print("Printing input4")
print(*sort_list(input4))   # "NOT A LIST"





     

