ls = [4,1,2,3,5,5,6]

def bubble_sort(ls):
    #keeping track of outer_iterations
    o_i = 0
    #keeping track of inner_iterations
    ls_i_i = []
    swapped = True
    last_swapped = len(ls) - 1 
    while swapped:
        swapped = False
        o_i += 1
        i_i = 0
        for i in range(last_swapped):
            i_i += 1
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                last_swapped = i
                swapped = True
        ls_i_i.append(i_i)
    
    return ls, o_i, ls_i_i

print(bubble_sort(ls))
##bubble_sort last_swapped index. better than swapped boolean variable 

array = [2,8,5,3,9,4,1,7]
def merge_sort(ls):
    pass