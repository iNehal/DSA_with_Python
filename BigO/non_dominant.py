def print_list(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
              
    for k in range(n):
        print(k)
        
print_list(5)

#fo i and for j loop is O(n^2) and for k loop is O(n) so, we can say that O(n^2) + O(n) = O(n^2 + n)
#dominant term is n^2(n square) and non-dominant term is n
#we can remove/drop non dominant term. so, the answer will be O(n^2)
#we have to drop it because we have to make BigO notation simple.