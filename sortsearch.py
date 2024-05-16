def bubble_sort_2d(arr):
    n=len(arr) #number of rows in the 2D array
    m=len(arr[0]) #number of columnss in the 2D array; assumes all rows have equal length
    total_elements=n*m   #total number of elements in 2D array

    for i in range(total_elements-1):
        #outer loop: goes through all the elemnts in the 2D array

        for j in range(total_elements-1-i):
            #inner loop: goes through the elements, reducing the comparison range each time
            #calculate current position in 2D terms
            row1=j//m
            col1=j%m
            #calculate next position (right next to the current position)
            row2=(j+1)//m
            col2=(j+1)%m
            #compare and possible swap elements
            if arr[row1][col1]>arr[row2][col2]:
                #if the current element is greater than the next, swap them
                arr[row1][col1],arr[row2][col2]=arr[row2][col2],arr[row1][col1]




def search_element(arr,element):
    found=False #initiating a flag to track if the element is found
    for i in range (len(arr)):
        for j in range (len(arr[i])):
            if arr[i][j]==element:
                print(f"element found at the pasition :row{i}, column{j}")
                found=True
                return   #exit the function after finding the element
    if not found:
        print("element not found in the given array")




#example usage:
arr=[[9,2,3],
     [4,5,6],
     [7,8,1]
]
print(arr)
bubble_sort_2d(arr)
print(arr)
#searching for an element
search=int(input("enter the element to search:"))
search_element(arr,search)