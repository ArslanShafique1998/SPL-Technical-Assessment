def common_sequence(a,b):
    x=''   #initialize the empty string
    maximum=max(len(a),len(b)) #check which string has maximum length
    if maximum==len(a): #If first string has maximum length then compare this first string
        for i in range (0,maximum,1):      # each element with second string to find which elements are common
            for j in range (0,len(b),1):
                if a[i]==b[j]:
                    if a[i] in x:
                        pass
                    else:
                        x=x+a[i]      #add the common string element in x
    elif maximum==len(b): # If second string has maximum length then do the same thing as we do above
        for i in range (0,maximum,1):
            for j in range (0,len(a),1):
                if b[i]==a[j]:
                    if b[i] in x:
                        pass
                    else:
                        x=x+b[i]
    return x #return the common string
#Take inputs of two strings
string1=input("Enter string 1:")
string2=input("Enter string 2:")
#Pass strings from the function to find subsequence pattern
common= common_sequence(string1,string2)
print("Common Subsequence is :",common)