s = list(input())
m = int(input()) 
transformations = [int(i)-1 for i in input().split()]
transformations.sort() 

index = 0 

for i in range(len(s) // 2): 
    while index < len(transformations) and transformations[index] <= i:
        index += 1 
        
    if index % 2 == 1:
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1],s[i] 
        
        
print("".join(s))