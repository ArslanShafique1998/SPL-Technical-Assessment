def find_pairs(array,target):
    pairs=[]
    l=len(array)
    #initialize the tuple
    p=()
    #We add each element with the rest of high index elements For example array=[1,2,3,4]
    #Then take first element 1 and add other high index 1+2,1+3,1+4, then take 2 and 2+3,2+4
    # then take 3 so add high index 3+4. By this we can check each possibility by edition.
    for i in range (0,l,1):
        for j in range (i,l,1):
            if array[i]+array[j]==target: #if the addition equals to target value
                p=(array[i],array[j]) #then put that pair in tuple and then put that tuple in array
                pairs.append(p)
    l=len(pairs)
    for i in range (0,l,1):
        for j in range (i+1,l,1):
            if pairs[i][0]==pairs[j][1] and pairs[i][1]==pairs[j][0]:#if we have identical tuples then it remove on tuple
                pairs.remove(pairs[i])
            elif pairs[i][0]==pairs[j][0] and pairs[i][1]==pairs[j][1]:
                pairs.remove(pairs[i])
    return pairs
#Take the length of array
n=int(input("Enter the length of array:"))
array=[]
#Take elements of array
for i in range (0,n,1):
    num=int(input("Enter the element of array:"))
    array.append(num)
#Take target value
target=int(input("Enter the target value:"))
#Pass the array and target value
pairs= find_pairs(array,target)
print("Pairs are:",pairs)