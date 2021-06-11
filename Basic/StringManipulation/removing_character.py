def RemoveCharacter(string,char):
    b=list(string)# covert string into list
    a=0
    l = len(b)
    for i in range (0,l,1):# we find the frequency that how many time that character is occur
        if b[i]==char:
            a+=1
    for i in range(0,a,1):# we remove that character from the list by how many time it occur in list
        b.remove(char)
    l=len(b)
    x=''
    for i in range (0,l,1):#Now the character elements in list is concatenated in x to return that string from which the required character is removed
        x=x+b[i]
    return x
#Take the string and character which we want to remove
string=input("Enter your string:")
char=input("Enter character that you want to remove:")
new_string=RemoveCharacter(string,char)
print("String after removing character:",new_string)