#Bubble Sort := Sorts the  given numbers in an list
# Concepts used in bubble sort are following
# 1. Comparing 
# 2. Swapping
# 
# use 2 loops :- one for performing comparision
# other loop for performing the travesal through the list
#   
#

list_to_be_sorted_var = [5,4,3,2,1]
#function to perform swapping of 2 numbers
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

#function to perform sorting
def bubble_sort(list_var):
    for i in range(len(list_var)-1,0,-1):
        for j in range(i):
            if list_var[j] > list_var[j+1] :#sign here will decide asending or desending order. (>) means asending
                list_var[j],list_var[j+1] = swap( list_var[j],list_var[j+1] )
    return list_var

#main 

print("unsorted List",list_to_be_sorted_var)
list_sorted_var = bubble_sort(list_to_be_sorted_var)
print("Sorted list in inreasing order(aesending)",list_sorted_var)


#function to perform sorting desending order
def bubble_sort_2(list_var):
    for i in range(len(list_var)-1,0,-1):
        for j in range(i):
            if list_var[j] < list_var[j+1] :#sign here will decide asending or desending order. (<) means desending
                list_var[j],list_var[j+1] = swap( list_var[j],list_var[j+1] )
    return list_var

#main 
list_to_be_sorted_var = [1,2,3,4,5]
print()
print("unsorted List",list_to_be_sorted_var)
list_sorted_var = bubble_sort_2(list_to_be_sorted_var)
print("Sorted list in deacrsing order(desending)",list_sorted_var)


#############  Or whole process can be replaced by using sort() funcion that python provides########################
print()
print("Sorting by using Sort() Function")
sample_list_var = [2,3,4,1,3,5]
print("unsorted",sample_list_var)
sample_list_var.sort()
print("sorted",sample_list_var)

