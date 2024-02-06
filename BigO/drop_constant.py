def print_list(n):
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j)
        
print_list(5)

#for i loop is O(n) and for j loop is O(n) it means O(n) + O(n) = O(2n) so, we can drop constant(2) i.e, O(n).