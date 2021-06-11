def left_rotate(array,num):
    #Run the loop iterations equal to number of rotation we first store the first element
    #Then we push the array to left by give index to the next index element and at the last give
    #the first element at the last index of array
    for j in range (0,rotation_number,1):
        a=array[0]
        for k in range (0,length-1,1):
            array[k]=array[k+1]
        array[length-1]=a
    return (array)
#take length of array
length=int(input("Enter array size:"))
array=[]
#Enter array values
for i in range (0,length,1):
    num=int(input("Enter array element:"))
    array.append(num)
print("\nEntered array is:",array)
#Enter the number which array rotate
rotation_number=int(input("\nEnter number of rotations:"))
array= left_rotate(array,rotation_number)
print(array)
