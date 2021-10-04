import sys
 

def solution(arr, x):
 
    
    closestSum = sys.maxsize
 
    
    for i in range (len(arr)) :
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len( arr)):
             
                
                if(abs(x - closestSum) >
                abs(x - (arr[i] +
                arr[j] + arr[k]))):
                    closestSum = (arr[i] +
                                    arr[j] + arr[k])
             
    
    return closestSum
 

if __name__ == "__main__":
     
    arr = [ -1, 2, 1, -4 ]
    x = 1
     
    print(solution(arr, x))
