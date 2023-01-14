import more_itertools as mm
from timeit import default_timer as  timer
arr=mm.random_combination(range(1,10005000),r=10000000)
l=len(arr)
del mm
f1=3
f11=13
f21=55
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

rp2=f21
f11=f11

print(l ,"hello 2 21 233 ")

def kartik_strafe_ss(arr,x,rp2,rp,l): # arr,x,rp1=0,rn1=0,fa1=0,fa2=0,x1=None
#    global c
#    c=0
    rn1=0
    c2=rn1+rp
    x2=arr[c2]
    #def kartik_strafe_s(arr,x,rp2,rp,l,n2,c2,x2): # arr,x,rp1=0,rn1=0,fa1=0,fa2=0,x1=None
    if x == arr[l]:
        return l
    gg=True
    while(rp > 0 ):
#        c+=1
#        print(rp,rp2)
        if x < x2:
            l=c2
            rp,rp2=rp2-(rp*11),rp
            gg=False
        elif x > x2:
            rn1=c2 #1.1.2
            if gg:
                while ( rp > l-rn1): # edited last
                    rp,rp2=rp2-(rp*11),rp
            gg=True

        else :
            return c2            
        c2=(rn1+rp)<<2
        x2=arr[c2]
    else:
        
        if l > rn1+rp+1 and x == arr[rn1+rp+1]:
            return rn1+rp+1
        elif l > rn1+rp+2 and x == arr[rn1+rp+2]:
            return rn1+rp+2
        return -1


print("kartik_strafe_sss","\n")
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

print("---------------------------non uniform all good")
cc=[ kartik_strafe_ss(arr,i,rp2,f11,l) for i in arr] #----------------------
cc2=[ i  for i in range(l+1) if cc[i]  == -1 or cc[i] != i ] #----------------------
print(cc2[:10],len(cc2))



del arr


# RESULTS ----------------------------------------------------------------------


#[11, 17, 31, 43, 53, 54, 56, 65, 70, 90]
#array length 10000
#fibMonaccianSearch 
#
#---------------------------AVG tim
#7.4363732090205306e-06
#---------------------------not there AVG tim
#8.663728503597667e-06
#---------------------------agg tim
#0.07214208799996413
#---------------------------not there agg tim
#0.08487322399923869
#---------------------------non uniform all good
#[] 0
#987 4181 17711
#kartik_strafe_s 
#
#---------------------------AVG tim
#4.077717764457412e-06
#---------------------------not there AVG tim
#5.193186819387222e-06
#---------------------------agg tim
#0.03895090799960599
#---------------------------not there agg tim
#0.050423452999893925
#---------------------------non uniform all good
#[] 0






#[6, 7, 14, 30, 31, 44, 52, 71, 73, 88]
#array length 10000
#fibMonaccianSearch 
#
#---------------------------AVG tim
#7.4363041887409054e-06
#---------------------------not there AVG tim
#8.620073798556405e-06
#---------------------------agg tim
#0.07251622100011446
#---------------------------not there agg tim
#0.0848702389994287
#---------------------------non uniform all good
#[] 0
#987 4181 17711
#kartik_strafe_s 
#
#---------------------------AVG tim
#4.110122403233066e-06
#---------------------------not there AVG tim
#5.229889994085214e-06
#---------------------------agg tim
#0.03993491099936364
#---------------------------not there agg tim
#0.05207003499890561
#---------------------------non uniform all good
#[] 0
#


#fibMonaccianSearch 
#
#---------------------------AVG tim
#1.374199968993782e-05 0.0008404150000842492 1.0149999525310704e-06
#---------------------------not there AVG tim
#1.5200827231633483e-05 0.000869429999966087 1.1498000048959511e-05
#---------------------------agg tim
#134.44408429799978
#---------------------------not there agg tim
#143.5775165949999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#6.966458216784815e-06 0.0007596010000270326 6.820000635343604e-07
#---------------------------not there AVG tim
#8.537645535027657e-06 0.0007221969999591238 4.273999820725294e-06
#---------------------------agg tim
#68.02357666299986
#---------------------------not there agg tim
#82.90312939100022




#fibMonaccianSearch 
#
#---------------------------AVG tim
#1.4163468805353717e-05 0.0009263490001103492 1.0320000001229346e-06
#---------------------------not there AVG tim
#1.575100460207502e-05 0.0006268940001064038 1.204999989568023e-05
#---------------------------agg tim
#139.7867404069998
#---------------------------not there agg tim
#145.04687118499987
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#7.01267835105389e-06 0.0005907119998482813 7.23000084690284e-07
#---------------------------not there AVG tim
#8.474360409463735e-06 0.0006878439999127295 4.303999958210625e-06
#---------------------------agg tim
#68.10377232300016
#---------------------------not there agg tim
#83.30132079899977
#


#fibMonaccianSearch 
#
#---------------------------AVG tim
#1.303533153029714e-05 0.000776840999947126 9.789999921849812e-07
#---------------------------not there AVG tim
#1.4560610081094126e-05 0.0007726559999809979 1.1212999993404082e-05
#---------------------------agg tim
#129.72669319300007
#---------------------------not there agg tim
#144.86409760700008
#---------------------------non uniform all good
#^Z
#[1]+  Stopped                 python3 rnn.py




#fibMonaccianSearch 
#
#---------------------------AVG tim
#1.2980801210255664e-05 0.0007190499998159794 9.899999895424116e-07
#---------------------------not there AVG tim
#1.4510959333851565e-05 0.0003518500000154745 1.1198000038348255e-05
#---------------------------agg tim
#129.0158963460001
#---------------------------not there agg tim
#143.84768183999995
#---------------------------non uniform all good
#[] 0
#(6, 8, 23, 54, 82, 85, 86, 99, 116, 128) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#6.96000316147728e-06 0.0010603519999676791 7.139997251215391e-07
#---------------------------not there AVG tim
#8.519243757902229e-06 0.000559107999833941 4.300999989936827e-06
#---------------------------agg tim
#69.19327190000013
#---------------------------not there agg tim
#84.43711529799975
#---------------------------non uniform all good
#[] 0




#fibMonaccianSearch 
#
#---------------------------AVG tim
#1.297320766531525e-05 0.0006816430000071705 9.830000635702163e-07
#---------------------------not there AVG tim
#1.458989038946711e-05 0.0003192740000486083 1.1118000202259282e-05
#---------------------------agg tim
#128.54079512199996
#---------------------------not there agg tim
#145.30597051600034
#---------------------------non uniform all good
#[] 0
#(1, 7, 23, 34, 39, 49, 53, 55, 65, 70) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#6.942785415209554e-06 0.0006328850004138076 6.559998837474268e-07
#---------------------------not there AVG tim
#8.506160674541168e-06 0.0006650770001215278 4.367999736132333e-06
#---------------------------agg tim
#68.26217449199976
#---------------------------not there agg tim
#83.63723055799983
#---------------------------non uniform all good
#[] 0




#fibMonaccianSearch 
#
#---------------------------AVG tim
#1.2966538621700737e-05 0.0010458180004206952 9.540003702568356e-07
#---------------------------not there AVG tim
#1.4558863090472915e-05 0.0007655090003026999 1.0942000699287746e-05
#---------------------------agg tim
#130.02745505199982
#---------------------------not there agg tim
#146.63939741299964
#---------------------------non uniform all good
#[] 0
#(1, 7, 12, 50, 74, 82, 85, 93, 100, 107) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#6.9550332086444435e-06 0.00010938200011878507 6.440004653995857e-07
#---------------------------not there AVG tim
#8.498074211666645e-06 0.00010479000047780573 4.261999492882751e-06
#---------------------------agg tim
#70.46444781300033
#---------------------------not there agg tim
#85.21204331499939
#---------------------------non uniform all good
#[] 0


#fibMonaccianSearch 
#
#(21, 41, 45, 47, 57, 61, 63, 66, 68, 72) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#7.096470993157743e-06 0.00018145300055039115 6.209993443917483e-07
#---------------------------not there AVG tim
#8.659528162302186e-06 0.000518175999786763 4.128000000491738e-06
#---------------------------agg tim
#69.5786815219999
#---------------------------not there agg tim
#84.41467969899986
#---------------------------non uniform all good
#[] 0
#







#fibMonaccianSearch 
#
#---------------------------AVG tim
#-- [(1.423e-05, 50174)] [(1.423e-05, 50174), (1.428e-05, 50043)]
#1.3924962018070527e-05 9.430699992662994e-05 1.027000052999938e-06
#---------------------------not there AVG tim
#-- [(1.57e-05, 79223)] [(1.57e-05, 79223), (1.531e-05, 75930)]
#1.554750014110159e-05 0.0001160130000243953 1.1970999821642181e-05
#(20, 36, 39, 46, 54, 69, 72, 106, 115, 146) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#-- [(7.05e-06, 52779)] [(7.05e-06, 52779), (6.79e-06, 51787)]
#6.934916791217938e-06 6.492900001831003e-05 6.830000529589597e-07
#---------------------------not there AVG tim
#-- [(8.47e-06, 49466)] [(8.47e-06, 49466), (8.73e-06, 47752)]
#8.504860024118307e-06 6.771000016669859e-05 4.184999852441251e-06




#fibMonaccianSearch 
#
#---------------------------AVG tim
#-- [(1.342e-05, 56539)] [(1.342e-05, 56539), (1.337e-05, 56161)]
#1.3035727672364693e-05 0.00023111400014386163 9.54999904934084e-07
#---------------------------not there AVG tim
#-- [(1.479e-05, 95110)] [(1.479e-05, 95110), (1.441e-05, 93387)]
#1.4625112496203838e-05 0.0002326419999008067 1.1246000212850049e-05
#(20, 29, 31, 32, 40, 88, 95, 103, 104, 110) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#-- [(7.1e-06, 50993)] [(7.1e-06, 50993), (6.88e-06, 50840)]
#6.976935746397794e-06 8.294100007333327e-05 6.380000741046388e-07
#---------------------------not there AVG tim
#-- [(8.47e-06, 49098)] [(8.47e-06, 49098), (8.43e-06, 48289)]
#8.484933892023491e-06 0.00020654899981309427 4.234999778418569e-06




#fibMonaccianSearch 
#
#---------------------------AVG tim
#-- [(1.333e-05, 55702)] [(1.333e-05, 55702), (1.329e-05, 55322)]
#1.2967659011186333e-05 9.07180001377128e-05 9.659997886046767e-07
#---------------------------not there AVG tim
#-- [(1.466e-05, 88333)] [(1.466e-05, 88333), (1.432e-05, 86754)]
#1.4551649347339344e-05 9.65459998951701e-05 1.1145000371470815e-05
#(6, 10, 25, 28, 29, 44, 47, 51, 68, 71) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#-- [(7.1e-06, 49805)] [(7.1e-06, 49805), (6.88e-06, 49446)]
#6.9676002388897355e-06 7.745099992462201e-05 6.66000232740771e-07
#---------------------------not there AVG tim
#-- [(8.43e-06, 49741)] [(8.43e-06, 49741), (8.47e-06, 49156)]
#8.485804212431095e-06 9.480800008532242e-05 4.319000254326966e-06
#




#fibMonaccianSearch 
#
#---------------------------AVG tim
#-- [(1.329e-05, 57708), (1.337e-05, 55964), (1.372e-05, 54847), (1.332e-05, 53069), (1.333e-05, 53011), (1.334e-05, 52536), (1.331e-05, 52521), (1.33e-05, 52332), (1.335e-05, 52194), (1.294e-05, 52025)]
#1.3007227154655084e-05 0.0003667480004878598 9.719997251522727e-07
#---------------------------not there AVG tim
#-- [(1.458e-05, 116091), (1.423e-05, 111913), (1.46e-05, 107236), (1.459e-05, 107010), (1.461e-05, 106328), (1.462e-05, 103133), (1.422e-05, 102035), (1.457e-05, 100652), (1.421e-05, 100432), (1.424e-05, 99957)]
#1.4465694607490423e-05 0.0007128139995984384 1.1186999472556636e-05
#(7, 28, 29, 40, 41, 42, 47, 67, 75, 94) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#-- [(6.84e-06, 52122), (7.1e-06, 51567), (7.01e-06, 49367), (7.27e-06, 49276), (7.08e-06, 47820), (7.05e-06, 47752), (7.06e-06, 47604), (6.83e-06, 47569), (7.07e-06, 47528), (7.09e-06, 47296)]
#6.959784425248836e-06 0.00022802900002716342 6.789996405132115e-07
#---------------------------not there AVG tim
#-- [(8.39e-06, 47602), (8.64e-06, 47111), (8.47e-06, 46541), (8.13e-06, 45991), (8.73e-06, 45588), (8.21e-06, 44508), (8.42e-06, 44337), (8.43e-06, 44189), (8.4e-06, 44109), (8.44e-06, 43934)]
#8.527028961510495e-06 0.0002983579997817287 4.321000233176164e-06
#



#fibMonaccianSearch 
#
#---------------------------AVG tim
#-- [(1.3e-05, 4010713), (1.4e-05, 2851127), (1.2e-05, 1895957), (1.1e-05, 616215), (1.5e-05, 352770), (1e-05, 167095), (9e-06, 42313), (1.6e-05, 13105), (1.8e-05, 11414), (1.7e-05, 11362)]
#1.3009138193582566e-05 0.000188915999387973 9.710001904750243e-07
#---------------------------not there AVG tim
#-- [(1.5e-05, 4497863), (1.4e-05, 4130034), (1.3e-05, 741463), (1.6e-05, 553386), (1.2e-05, 18286), (1.9e-05, 16493), (1.7e-05, 15755), (1.8e-05, 11773), (2e-05, 5553), (2.1e-05, 1179)]
#1.4531278109502909e-05 9.902599958877545e-05 1.1221000022487715e-05

#(21, 34, 41, 55, 77, 78, 92, 99, 119, 126) 9999999
#1346269 5702887 24157817
#kartik_strafe_s 
#
#---------------------------AVG tim
#-- [(7e-06, 4315547), (6e-06, 2540693), (8e-06, 2214487), (5e-06, 541941), (9e-06, 292620), (4e-06, 53077), (1e-05, 11547), (1.1e-05, 7686), (1.2e-05, 7586), (1.3e-05, 3419)]
#6.9210661320033975e-06 9.21260007089586e-05 6.919999577803537e-07
#---------------------------not there AVG tim
#-- [(8e-06, 3509911), (9e-06, 3470840), (7e-06, 1301997), (1e-05, 1255872), (6e-06, 164787), (1.1e-05, 153997), (1.2e-05, 17312), (1.3e-05, 16759), (1.4e-05, 16544), (1.5e-05, 14752)]
#8.612052388861593e-06 0.00010612799997034017 4.276000254321843e-06
#


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
