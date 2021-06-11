def substrings(a,b):
    #Check which string have minimum length
    minimum=min(len(a),len(b))
    inc=0
    if minimum==len(a):# We check each element of shortest string throughout on the longest string and check either the string match
        #not include the spaces
        for i in range (0,len(a),1):
            for j in range (0,len(b),1):
                if a[i]==b[j] and a[i]!=" ":
                    inc+=1
        if inc > 0:
            return 1
        else:
            return 0
    elif minimum==len(b):# same thing is done if shortest length is of second string
        for i in range (0,len(b),1):
            for j in range (0,len(a),1):
                if b[i]==a[j] and b[i]!=" ":
                    inc+=1
        if inc > 0:
            return 1
        else:
            return 0
#Take two strings
a=input("Enter string 1:")
b=input("Enter string 2:")
output=substrings(a,b)
print(output)
