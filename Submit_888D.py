import math
     
     
s = input().split()
n = int(s[0])
k = int(s[1])
     
def Count_ALP_C(n, k):
        count = 0
        
        for m in range(k+1):
            count += math.comb(n, m) * d(m)
        
        return count
        
def d(m):
    if (m==0):
        return 1
    if (m==1):  
        return 0
    if (m==2):
        return 1
    if (m==3):
        return 2
    if (m==4):
        return 9
            
print(Count_ALP_C(n,k))