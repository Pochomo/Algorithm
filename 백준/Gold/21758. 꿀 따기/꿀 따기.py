import sys
input = sys.stdin.readline
 
n = int(input()) 
data = list(map(int,input().split())) 

ans=0

sum=[] 
sum.append(data[0]) 

for i in range(1,n): 
    sum.append(sum[i-1]+data[i]) 
    
#왼쪽 끝에 벌통
for i in range(1,n-1): 
    ans=max(ans,sum[n-2]+sum[i-1]-data[i])

#오른쪽 끝에 벌통
for i in range(1, n-1):
    ans = max(ans, sum[n-1] - data[0] - data[i] + sum[n-1] - sum[i]) 

#중앙에 벌통
for i in range(1,n-1): 
    ans=max(ans,sum[n-2] - data[0] + data[i])
       
print(ans)