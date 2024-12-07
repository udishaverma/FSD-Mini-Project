#find factors of a given number n

n=int(input("Enter n: "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print(f"The factors of {n} are {factors}")