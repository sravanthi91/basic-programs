n=int(input())
k=n
reverse=0
while(n!=0):
    r=n%10
    reverse=reverse*10+r
    n=n//10
if(k==reverse):
    print("palindrome")
else:
    print("not palindrome")

    
