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
    x2=arr[c2]
    if x == arr[l]:
        return l
    gg=True
    while(rp > 0 ):
        if x < x2:
            l=c2
            rp,rp2=rp2-(rp<<2),rp
            gg=False
        elif x > x2:
            rn1=c2
            if gg:
                while ( rp > l-rn1):
                    rp,rp2=rp2-(rp<<2),rp
            gg=True

        else :
            return c2            
        c2=rn1+rp
        x2=arr[c2]
    else:
        
        if x == arr[rn1+rp+1]:
            return rn1+rp+1
        return -1


print(arr[:10],l)

#print("kartik_strafe_s 3 13","\n")
#print("---------------------------AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    kartik_strafe_s(arr,i,rp2,f11,l)
#    end= timer()
#    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
#print(sum(xx)/(l+1),max(xx),min(xx))
#
#print("---------------------------not there AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    kartik_strafe_s(arr,i+0.1,rp2,f11,l)
#    end= timer()
#    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
#print(sum(xx)/(l+1),max(xx),min(xx)) 
#
#
#print("---------------------------agg tim")
#start= timer()
#cc=[ kartik_strafe_s(arr,i,rp2,f11,l) for i in arr]
#end= timer()
#print(end-start)
#
#print("---------------------------not there agg tim")
#start= timer()
#cc=[ kartik_strafe_s(arr,i+0.1,rp2,f11,l) for i in arr]
#end= timer()
#print(end-start)
#
#print("---------------------------non uniform all good")
#cc=[ kartik_strafe_s(arr,i,rp2,f11,l) for i in arr] #----------------------
#cc2=[ i  for i in range(l+1) if cc[i]  == -1 or cc[i] != i ] #----------------------
#print(cc2[:10],len(cc2))


l=len(arr)

fibMMm2 = 0  # (m-2)'th Fibonacci No.
fibMMm1 = 1  # (m-1)'th Fibonacci No.
fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
while (fibM < l):
    fibMMm2 = fibMMm1
    fibMMm1 = fibM
    fibM = fibMMm2 + fibMMm1

def fibMonaccianSearch(arr, x, n,fibM,fibMMm2,fibMMm1):
    offset = -1
    while (fibM > 1):
        i=min(offset+fibMMm2, n-1)

        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1  
            offset = i            

        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1            

        else:
            return i
    if(fibMMm1 and arr[n-1] == x):
        return n-1
    return -1

#from collections import Counter

#print("---------------------------AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    fibMonaccianSearch(arr, i, l,fibM,fibMMm2,fibMMm1)
#    end= timer()
#    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
#print(sum(xx)/l,max(xx),min(xx))
#
#print("---------------------------not there AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    fibMonaccianSearch(arr, i+0.1, l,fibM,fibMMm2,fibMMm1)
#    end= timer()
#    xx.append(end-start)
#    #    xx.append(round(end-start,7))
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
#print(sum(xx)/l,max(xx),min(xx))
#
#print("---------------------------agg tim")
#start= timer()
#cc=[ fibMonaccianSearch(arr, i, l,fibM,fibMMm2,fibMMm1) for i in arr]
#end= timer()
#print(end-start)
#
#print("---------------------------not there agg tim")
#start= timer()
#cc=[ fibMonaccianSearch(arr, i+0.1 , l,fibM,fibMMm2,fibMMm1) for i in arr]
#end= timer()
#print(end-start)


def binary(arr,x,l):
    lo=0
    hi=l-1
    while (hi - lo) > 1:
        mid=(hi+lo)//2
        if arr[mid] < x :
            lo=mid + 1
        else :
            hi = mid
    if arr[lo] == x:
        return lo
    elif arr[hi] == x:
        return hi
    else :
        return -1

l=len(arr)

#print("binary","\n")
#print("---------------------------AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    bins(arr,i,l)
#    end= timer()
#    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
#print(sum(xx)/(l),max(xx),min(xx))
#
#print("---------------------------not there AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    bins(arr,i+0.1,l)
#    end= timer()
#    xx.append(end-start)
    #data= Counter([ round(i,6) for  i in xx])
    #print("--",data.most_common(10))
#print(sum(xx)/(l),max(xx),min(xx)) 
#
#print("---------------------------agg tim")
#start= timer()
#cc=[ bins(arr,i,l) for i in arr]
#end= timer()
#print(end-start)
#
#print("---------------------------not there agg tim")
#start= timer()
#cc=[ bins(arr,i+0.1,l) for i in arr]
#end= timer()
#print(end-start)


l=len(arr)
f1=2
f11=21
f21=233
while (f21 < l):
    f1,f11,f21=f11,f21,(f21*11)+f11  #----------------------
l=l-1
print(f1,f11,f21)
    #gg=((f11+f21)>>1)-(f11<<1)
    #rn2=(f11<<1 )+gg
    #rp2=(rn2<<1 )-f11

# rp2=f21
# f11=f11

# print(l ,"hello 2 21 233 ")

# def kartik_strafe_ss(arr,x,rp2,rp,l): # arr,x,rp1=0,rn1=0,fa1=0,fa2=0,x1=None
# #    global c
# #    c=0
#     rn1=0
#     c2=rn1+rp
#     x2=arr[c2]
#     #def kartik_strafe_s(arr,x,rp2,rp,l,n2,c2,x2): # arr,x,rp1=0,rn1=0,fa1=0,fa2=0,x1=None
#     if x == arr[l]:
#         return l
#     gg=True
#     while(rp > 0 ):
# #        c+=1
# #        print(rp,rp2)
#         if x < x2:
#             l=c2
#             rp,rp2=rp2-(rp*11),rp
#             gg=False
#         elif x > x2:
#             rn1=c2 #1.1.2
#             if gg:
#                 while ( rp > l-rn1): # edited last
#                     rp,rp2=rp2-(rp*11),rp
#             gg=True

#         else :
#             return c2            
#         c2=(rn1+rp)<<2
#         x2=arr[c2]
#     else:
        
#         if l > rn1+rp+1 and x == arr[rn1+rp+1]:
#             return rn1+rp+1
#         elif l > rn1+rp+2 and x == arr[rn1+rp+2]:
#             return rn1+rp+2
#         return -1


# print("kartik_strafe_sss","\n")
#print("---------------------------AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    kartik_strafe_ss(arr,i,rp2,f11,l)
#    end= timer()
#    xx.append(end-start)
#    #data= Counter([ round(i,6) for  i in xx])
#    #print("--",data.most_common(10))
#print(sum(xx)/(l+1),max(xx),min(xx))
#
#print("---------------------------not there AVG tim")
#xx=[]
#for i in arr:
#    start= timer()
#    kartik_strafe_ss(arr,i+0.1,rp2,f11,l)
#    end= timer()
#    #    xx.append(end-start)
#    xx.append(end-start)
#        #data= Counter([ round(i,6) for  i in xx])
#        #print("--",data.most_common(10))
#print(sum(xx)/(l+1),max(xx),min(xx)) 

    #print("---------------------------all good")
    #cc=[ kartik_strafe_ss(arr,i,rp2,f11,l) for i in arr] #----------------------
    #cc2=[ i  for i in arr if kartik_strafe_s(arr,i,rp2,f11,l)  == -1] #----------------------
    #print(cc2[:10],len(cc2))
    #print(sum([i-j for i,j in  zip(arr,cc)]))

#print("---------------------------agg tim")
#start= timer()
#cc=[ kartik_strafe_ss(arr,i,rp2,f11,l) for i in arr]
#end= timer()
#print(end-start)
#
#print("---------------------------not there agg tim")
#start= timer()
#cc=[ kartik_strafe_ss(arr,i+0.1,rp2,f11,l) for i in arr]
#end= timer()
#print(end-start)
#

# print("---------------------------non uniform all good")
# cc=[ kartik_strafe_ss(arr,i,rp2,f11,l) for i in arr] #----------------------
# cc2=[ i  for i in range(l+1) if cc[i]  == -1 or cc[i] != i ] #----------------------
# print(cc2[:10],len(cc2))



del arr


# RESULTS ----------------------------------------------------------------------

#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#8.577700469405398e-06 0.00016105600002447318 5.250001322565367e-07
#---------------------------not there AVG tim
#1.0342141906829761e-05 8.251200006270665e-05 4.662000037569669e-06
#---------------------------agg tim
#84.02351237700009
#---------------------------not there agg tim
#101.60765460099992
#fibb 3 13 
#
#---------------------------AVG tim
#1.0686052394754097e-05 7.561600000371982e-05 8.519998573319754e-07
#---------------------------not there AVG tim
#1.2166568663927615e-05 9.075000002667366e-05 9.649000048739254e-06
#---------------------------agg tim
#104.63681180499998
#---------------------------not there agg tim
#119.95206746000008


#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#9.83309035560394e-06 0.025090353999985382 5.68000132261659e-07
#---------------------------not there AVG tim
#1.0804059450626483e-05 0.0006951360001039575 4.580999984682421e-06
#---------------------------agg tim
#84.05184503400005
#---------------------------not there agg tim
#101.85226660499984
#fibb 3 13 
#
#---------------------------AVG tim
#1.0752612118459364e-05 0.0005897490000279504 8.450001587334555e-07
#---------------------------not there AVG tim
#1.2777158808254717e-05 0.0019322599996485224 9.666000096331118e-06
#---------------------------agg tim
#105.92763819399988
#---------------------------not there agg tim
#119.69817694800031


#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#8.557602534024181e-06 0.0002442920003886684 5.669999154633842e-07
#---------------------------not there AVG tim
#1.0362754408405044e-05 0.0003222149998691748 4.735999937111046e-06
#---------------------------agg tim
#84.26382411500026
#---------------------------not there agg tim
#101.53610395700025
#fibb 3 13 
#
#---------------------------AVG tim
#1.0872139041106448e-05 0.0002961589998449199 9.069999578059651e-07
#---------------------------not there AVG tim
#1.2391252063007823e-05 0.008218049999868526 9.689999842521502e-06
#---------------------------agg tim
#105.86313079899992
#---------------------------not there agg tim
#122.66424773400013
#

#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#8.953117799384881e-06 0.0005258010000943614 5.700003384845331e-07
#---------------------------not there AVG tim
#1.0410031590300378e-05 0.0017288770000050135 4.465000074560521e-06
#---------------------------agg tim
#87.83572448900031
#---------------------------not there agg tim
#103.38555879100022
#fibb 3 13 
#
#---------------------------AVG tim
#1.081928215419357e-05 0.0003170889995089965 8.480001270072535e-07
#---------------------------not there AVG tim
#1.2254372997986501e-05 0.00031317400043917587 9.671000043454114e-06
#---------------------------agg tim
#105.36024417399949
#---------------------------not there agg tim
#120.15731555799994

# without x2
#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#7.296504748879761e-06 0.0004215560002194252 6.310001481324434e-07
#---------------------------not there AVG tim
#8.715544915826285e-06 0.0003854469996440457 4.291000550438184e-06
#---------------------------agg tim
#73.42458984600034
#---------------------------not there agg tim
#91.45123536400024
#fibb 3 13 
#
#---------------------------AVG tim
#1.116359600038877e-05 0.00044162200083519565 8.950000847107731e-07
#---------------------------not there AVG tim
#1.2630813841420058e-05 0.00026413499927002704 9.706000128062442e-06
#---------------------------agg tim
#114.0402806810007
#---------------------------not there agg tim
#130.57423117300004


#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#7.158425973869544e-06 0.0004214950004097773 6.249993020901456e-07
#---------------------------not there AVG tim
#8.673995687672595e-06 0.00031527500050287927 4.265999450581148e-06
#---------------------------agg tim
#69.21986417599965
#---------------------------not there agg tim
#85.69452984899999
#fibb 3 13 
#
#---------------------------AVG tim
#1.08986588910524e-05 0.0005154700002094614 9.40000063565094e-07
#---------------------------not there AVG tim
#1.247544736734917e-05 0.0004604460000336985 9.738999324326869e-06
#---------------------------agg tim
#109.65049266300048
#---------------------------not there agg tim
#122.51861194199955
#

#changing order

#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#6.810363650894669e-06 0.00020782299998245435 6.319996828096919e-07
#---------------------------not there AVG tim
#8.316263047923258e-06 0.0008074509996731649 5.044999852543697e-06
#---------------------------agg tim
#66.06056148599964
#---------------------------not there agg tim
#81.05443002900029
#fibb 3 13 
#
#---------------------------AVG tim
#1.126764762595294e-05 0.00017894099983095657 8.520000847056508e-07
#---------------------------not there AVG tim
#1.2741293709552702e-05 0.00014229800035536755 9.765999493538402e-06
#---------------------------agg tim
#106.08011824799996
#---------------------------not there agg tim
#120.69094659199982


#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#6.717379973897641e-06 6.690800000797026e-05 6.820000635343604e-07
#---------------------------not there AVG tim
#8.311868518530082e-06 0.00010497099992790027 5.0199996621813625e-06
#---------------------------agg tim
#65.36962625699925
#---------------------------not there agg tim
#81.89291224000044
#fibb 3 13 
#
#---------------------------AVG tim
#1.0820994170759878e-05 0.00020854200010944624 8.47000592330005e-07
#---------------------------not there AVG tim
#1.233284621272387e-05 0.00019599699953687377 9.73699934547767e-06
#---------------------------agg tim
#104.8984370240014
#---------------------------not there agg tim
#122.92526126100165
#


#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#6.772821300703367e-06 0.0003736520000074961 6.420000318030361e-07
#---------------------------not there AVG tim
#8.350900335100483e-06 0.00046754099992085685 4.995000040253217e-06
#---------------------------agg tim
#66.23097290299995
#---------------------------not there agg tim
#81.42467106599997
#fibb 3 13 
#
#---------------------------AVG tim
#1.0784696995786942e-05 7.319600013033778e-05 9.030000001075678e-07
#---------------------------not there AVG tim
#1.2472903614778011e-05 0.0008406990000366932 9.727000133352703e-06
#---------------------------agg tim
#105.6580890260002
#---------------------------not there agg tim
#120.65540264399988

#kartik_strafe_s 3 13 
#
#---------------------------AVG tim
#6.998941326603813e-06 0.00012178799988760147 6.479999683506321e-07
#---------------------------not there AVG tim
#8.323901225261556e-06 9.280299991587526e-05 4.94699997943826e-06
#---------------------------agg tim
#66.78858411400006
#---------------------------not there agg tim
#80.04795037899999
#fibb 3 13 
#
#---------------------------AVG tim
#1.0904459114408974e-05 0.00014028600003257452 8.560000424040481e-07
#---------------------------not there AVG tim
#1.2175731762083978e-05 0.00010404099998595484 9.685999884823104e-06
#---------------------------agg tim
#104.38122100899977
#---------------------------not there agg tim
#122.00123498899984
#


#81.05443002900029,120.69094659199982,122.00123498899984,80.04795037899999,120.65540264399988,81.42467106599997,122.92526126100165,81.89291224000044
#104.38122100899977,66.78858411400006,105.6580890260002,66.23097290299995,104.8984370240014,65.36962625699925,106.08011824799996,66.06056148599964




#EXperimental 

arr=mm.random_combination(range(1,10005000),r=10000000)
l=len(arr)
del mm
f1=3
f11=13
f21=55
while (f21 < l):
    f1,f11,f21=f11,f21,(f21<<2)+f11  #----------------------
print(arr[:10],l)
print(f1,f11,f21)
rp2=f21
if l > ((f21+f11)>>1):
    x=(f21<<2)+f11
    f11=(f21+f11)>>1
    rp2=(x+f21)>>1
    print("hh")
elif l > ((f21-f11)>>1):
    f11=(f21-f11)>>1
    rp2=((f21)<<1)-f11
    print("dd")
print(f11,rp2)
l=l-1


def kartik_strafe_s(arr,x,rp2,rp,l):
    rn1=0
    c2=rn1+rp
    x2=arr[c2]
    if x == arr[l]:
        return l
    gg=True
    while(rp > 0 ):

        if x > x2:
            rn1=c2
            if gg:
                while ( rp > l-rn1):
                    rp,rp2=rp2-(rp<<2),rp
            gg=True
        elif x < x2:
            l=c2
            rp,rp2=rp2-(rp<<2),rp
            gg=False
        else :
            return c2            
        c2=rn1+rp
        x2=arr[c2]
    else:
        if x == arr[rn1]:
            return rn1
        elif l > rn1+1  and x == arr[rn1+1]:
            return rn1+1
        return -1
