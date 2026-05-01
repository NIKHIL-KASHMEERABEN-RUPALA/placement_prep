
def find_Dominant_Number(arr):

    if not arr:
        return []
    
    freq = {}

    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    unique_count = len(freq)

    dominant_number = []

    for num,count in freq.items():
        if count>unique_count:
            dominant_number.append(num)
        
    
    return dominant_number

arr1 = [1, 2, 3, 1, 1, 4, 5, 1, 1, 1]
print(find_Dominant_Number(arr1))

arr2 = [1, 1, 1, 2, 2, 2, 3]
print(find_Dominant_Number(arr2))
