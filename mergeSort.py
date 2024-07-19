def mergeSort(array):
 if len(array) > 1:
   middle = len(array) // 2
   greater_than = array[:middle]
   less_than = array[middle:]
   mergeSort(greater_than)
   mergeSort(less_than)
   i = j = k = 0
   while i < len(greater_than) and j < len(less_than):
     if greater_than[i] < less_than[j]:
       array[k] = greater_than[i]
       i += 1
     else:
       array[k] = less_than[j]
       j += 1
     k += 1
   while i < len(greater_than):
     array[k] = greater_than[i]
     i += 1
     k += 1
   while j < len(less_than):
     array[k] = less_than[j]
     j += 1
     k += 1
array = [8,3,2,9,7,1,5,4]
mergeSort(array)
print("Sorted array is: ",array)

