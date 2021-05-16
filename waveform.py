
n=int(input())
r=n%10
n=n//10
if(r%2==0):
    s=True
else:
    s=False
while(n!=0):
    r=n%10
    n=n//10
    if(s==True and r%2==1):
        s=False
    elif(s==False and r%2==0):
        s=True
    else:
        print("not a waveform")
        break
else:
    print("waveform")
    
