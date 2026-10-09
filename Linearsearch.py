# ######    LINEAR    SEARCH 


n = int(input("Enter a number of list : "))

arr=[]


# Enter the elements which  user can store in list


print("Enter element: ")

for i in range (n):
    arr.append(int(input()))

#This is the  element which user can search in list

key = int(input("Enter value to search: "))
 
for i in range(n):

    if arr[i] == key :

     print(f"The search element is found at index{i}. ")
     break
    
else:
    print("THE value is not found.")


####    H A M M A D       N E U R A L


    

