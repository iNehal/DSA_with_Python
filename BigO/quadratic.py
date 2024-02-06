def pint_list(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
            
pint_list(5)

#this is a nested for loop that's why we will not add we will multiply the time complexity
#for i loop is O(n) and for j loop is O(n) it means O(n) * O(n) = O(n^2) i.e., BigO of n square
#it can be O(n^2), O(n^3), O(n^4) etc but we will always call O(n^2) or quadratic runtime complexity
#this is a worst time complexity
#actually we are doing one task multiple time