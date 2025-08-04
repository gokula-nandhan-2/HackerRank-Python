# Enter your code here. Read input from STDIN. Print output to STDOUT
temp = input().split(" ")
N = int(temp[0])
M = int(temp[1])

# Upside
for i in range(1,N,2):
    pattern = ".|." * i
    print(pattern.center(M,"-"))
    
# Center
print("WELCOME".center(M,"-")) 

# Downside
for i in range(N-2,0,-2):
    pattern = ".|." * i
    print(pattern.center(M,"-"))
        
