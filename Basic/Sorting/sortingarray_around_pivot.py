def DistributedArray(array,pivot):
    # sort the array using sort() function if pivot in this array so simply use sort
    #if not in array then first append it in and then sort it which sort the array around thw pivot
    if pivot in array:
        array.sort()
    else:
        array.append(pivot)
        array.sort()
    return array
#Take input of array length, array and pivot
n=int(input("Enter length of array:"))
array=[]
for i in range(0,n,1):
    a=int(input("Enter integers for array:"))
    array.append(a)
pivot=int(input("Enter pivot number:"))
print("The input array is :",array)
sort_array=DistributedArray(array,pivot)
print("\nThe sorted array is :",array)