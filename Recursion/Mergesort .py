def merge(arr1,arr2):
    mergedarray =[]
    indexOfarr1 = 0
    indexOfarr2 =0
    while indexOfarr1 < len(arr1) and  indexOfarr2 < len(arr2):
        if arr1[indexOfarr1] >= arr2[indexOfarr2]:
            mergedarray.append(arr2[indexOfarr2])
            indexOfarr2+=1
        else:
            mergedarray.append(arr1[indexOfarr1])
            indexOfarr1 += 1
       
    if len(arr1) > indexOfarr1:
        
        print("i am running here")
        print(arr1[indexOfarr1:len(arr1)])
        mergedarray += arr1[indexOfarr1:len(arr1)]
        return mergedarray
        
    if len(arr2) > indexOfarr2:
        print("indexofarr2",indexOfarr2)
        print("i am in the wrong place")
        mergedarray += arr2[indexOfarr2:len(arr2)]
        return mergedarray
        
        
        
#print(merge([1,8,9],[2,4,10]))
    





def MergeSort(arr):
        
        
       if len(arr) ==1:
            return arr
       middle = len(arr)//2
       first = arr[0:middle]
       second = arr[middle:len(arr)]
#    print("second",second)
 #   print("first",first)
    #eturn MergeSort(first)
    
    
       return merge(MergeSort(first),MergeSort(second))
    #print(firsthalf)
    
    
    #print("i am secondhalf",seconhalf)
   
  
 
print(MergeSort([5,4,3,2,1,7,9]))

#arr =[5,4,3,2,1]
#middle = len(arr)//2
#print(arr[0:middle+1])
#print(arr[middle+1:len(arr)])