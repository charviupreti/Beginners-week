def bubble(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

def insertion(arr):
    for i in range(len(arr)):
        m=arr[i]
        j=i-1
        while j>=0 and arr[j]>m:
            arr[j+1]=arr[j]
            j-=1
        arr[j + 1] = m 
       
arr=[5,4,1,2,3]
bubble(arr)
print(*arr)
arr=[5,4,1,2,3]
insertion(arr)
print(*arr)
            