
def checker(arr):
    
    if not arr:
        return[]
    
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if(num>max1):
            max2 = max1
            max1 = num
        elif(num>max2 and num!=max2):
            max2 = num
        
        if(num<min1):
            min2 = min1
            min1 = num
        elif(num<min2 and num!=min2):
            min2 = num
    
    if max2==float('-inf') or min2==float('inf'):
        print(f"The array doesnt have enough distinct elements  ")
    
    return{
        "Maximum": max1,
        "Sec_Maximum" : max2,
        "Minimum" : min1 , 
        "Sec_Minimum" : min2,
    }

print("TEST CASE 1:")
arr1 = [10, 5, 20, 8, 15]
result1 = checker(arr1)

for key,value in result1.items():
    print(f"{key} : {value}")