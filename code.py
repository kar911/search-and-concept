import more_itertools as mm
from timeit import default_timer as  timer
arr=mm.random_combination(range(1,10005000),r=10000000)
l=len(arr)
del mm
f1=1
f11=3
f21=13
while (f21 < l):
    f1,f11,f21=f11,f21,(f21<<2)+f11  #----------------------
l=l-1
print(arr[:10],l)
print(f1,f11,f21)
rp2=f21

def kartik_strafe_s(arr,x,rp2,rp,l):
    rn1=0
    c2=rn1+rp
    if x == arr[l]:
        return l
    gg=True
    while(rp > 0 ):
        if x > arr[c2]:
            rn1=c2
            if gg:
                while ( rp > l-rn1):
                    rp,rp2=rp2-(rp<<2),rp
            gg=True

        elif x < arr[c2]:
            l=c2
            rp,rp2=rp2-(rp<<2),rp
            gg=False
        else :
            return c2            
        c2=rn1+rp
    else:
        
        if x == arr[rn1]:
            return rn1
        return -1



print("kartik_strafe_s 3 13","\n")
print("---------------------------AVG tim")
xx=[]
for i in arr:
    start= timer()
    kartik_strafe_s(arr,i,rp2,f11,l)
    end= timer()
    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
print(sum(xx)/(l+1),max(xx),min(xx))

print("---------------------------'not there' AVG tim")
xx=[]
for i in arr:
    start= timer()
    kartik_strafe_s(arr,i+0.1,rp2,f11,l)
    end= timer()
    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
print(sum(xx)/(l+1),max(xx),min(xx)) 


print("---------------------------total tim")
start= timer()
cc=[ kartik_strafe_s(arr,i,rp2,f11,l) for i in arr]
end= timer()
print(end-start)

print("---------------------------'not there' total tim")
start= timer()
cc=[ kartik_strafe_s(arr,i+0.1,rp2,f11,l) for i in arr]
end= timer()
print(end-start)

print("---------------------------non uniform all good")
cc=[ kartik_strafe_s(arr,i,rp2,f11,l) for i in arr] #----------------------
cc2=[ i  for i in range(l+1) if cc[i]  == -1 or cc[i] != i ] #----------------------
print(cc2[:10],len(cc2))
