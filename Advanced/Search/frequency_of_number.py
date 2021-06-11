def frequency_count(array,l):
    #initialize the dictionary
    dict={}
    #Now it take elements and count how many time it occur and then add it in dictionary
    for i in range (0,l,1):
        count=array.count(array[i])
        dict[array[i]]=count
    return dict
#Take length of array
n=int(input("Enter the length of array:"))
array=[]
#Enter the array elements
for i in range (0,n,1):
    num=int(input("Enter the element of array:"))
    array.append(num)
l=len(array)

#pass to count frequency
frequency=frequency_count(array,l)
print ("The frequency of numbers in array is:",frequency)