import time
import random
import copy

# ls = [4,1,2,3,5,5,6]

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

# print(bubble_sort(ls))
# ##bubble_sort last_swapped index. better than swapped boolean variable 

array = [4,1,7,2,1,9,0,0,1,2]

# my merge_sort, recursive
def merge_sort_mine(ls):
    size = len(ls)
    if size == 1:
        return ls

    else:
        size = size//2
        array1, array2 = ls[:size], ls[size:]
        return merge(merge_sort_mine(array1), merge_sort_mine(array2))

def merge(array_1, array_2):
    sorted_array = []
    size_1 = len(array_1)
    size_2 = len(array_2)
    i_1 = 0
    i_2 = 0
    while i_1 != size_1 and i_2 != size_2:
        if array_1[i_1] > array_2[i_2]:
            sorted_array.append(array_2[i_2])
            i_2 += 1
        else:
            sorted_array.append(array_1[i_1])
            i_1 += 1

    # if i_1 != size_1:
    #     sorted_array += array_1[i_1:]
    # else:
    #     sorted_array += array_2[i_2:]
    while i_1 != size_1:
        sorted_array.append(array_1[i_1])
        i_1 += 1

    while i_2 != size_2:
        sorted_array.append(array_2[i_2])
        i_2 += 1

    return sorted_array

def merge_sort_mine_1(ls):
    size = len(ls)
    if size == 1:
        return ls

    else:
        size = size//2
        array1, array2 = ls[:size], ls[size:]
        return merge_1(merge_sort_mine(array1), merge_sort_mine(array2))

def merge_1(array_1, array_2):
    sorted_array = []
    size_1 = len(array_1)
    size_2 = len(array_2)
    i_1 = 0
    i_2 = 0
    while i_1 != size_1 and i_2 != size_2:
        if array_1[i_1] > array_2[i_2]:
            sorted_array.append(array_2[i_2])
            i_2 += 1
        else:
            sorted_array.append(array_1[i_1])
            i_1 += 1

    if i_1 != size_1:
        sorted_array += array_1[i_1:]
    else:
        sorted_array += array_2[i_2:]

    return sorted_array


#iterative
def merge_sort(array):
    if len(array) > 1:
        midpt = len(array)//2
        L_pos = R_pos = main_pos = 0
        L = array[:midpt]
        R = array[midpt:]
        merge_sort(L)
        merge_sort(R)
        while L_pos < len(L) and R_pos < len(R):
            if L[L_pos] > R[R_pos]:
                array[main_pos] = R[R_pos]
                R_pos += 1
            else:
                array[main_pos] = L[L_pos]
                L_pos += 1
            main_pos += 1

        while L_pos < len(L):
            array[main_pos] = L[L_pos]
            L_pos += 1
            main_pos +=1

        while R_pos < len(R):
            array[main_pos] = R[R_pos]
            R_pos += 1
            main_pos +=1

def run_function(f, x):
    start = time.time()
    f(x)
    end = time.time()
    return end-start

def gen_random_int(number, seed):
    ls = [i for i in range(number)]
    random.shuffle(ls, random.seed(seed))
    return ls

 
time_builtin = []
time_builtin_2 = []
# set the maximum power for 10^power number of inputs
maxpower = 6
for n in range(1, maxpower + 1):
    # create array for 10^1, 10^2, etc 
    # use seed 100
    array = gen_random_int(10**n, 100)
    array_2 = copy.deepcopy(array)
    
    # call run_function with sorted() and array as arguments
    # result = run_function(None, None) 
    result = run_function(merge_sort_mine_1, array)
    result_2 = run_function(merge_sort_mine, array)
    ###
    ### YOUR CODE HERE
    ###
    time_builtin_2.append(result_2)
    time_builtin.append(result)


print('if', time_builtin, 'while', time_builtin_2)

# print(time_builtin)
