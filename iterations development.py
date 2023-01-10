#    This contains all the iterations for any help
# every function is a iteration somewhat

# FIRST FEW ARE FOR CONCEPTUAL CORECTNESS
# LATER THE ALGO WAS IMPROVED TO OTHER FORM

# here you can see the gradual progress of this algo form recursive to iterative
# and more optimmized
# at later stages of testing i used randomly generted sorted array for real life arrays replication

def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0): # add max fn,fn2
    # fn = fn or [l-fn]
    # fp = fn+1
    # fp1=i
    # fn1=j
    
    # next itter  planing i and j where to put them
    # re-find  fibs of compaired length
    
    # fib desend lower then i-j
    # want f's big 2 in function arg
    
    # fa2 bigger
    if fn1 == 0 : # can go to 0
        fp=fa2
        fn=fa1  
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=fn1,fp1
        print("hoho")
    else :
        while (0 > fa1 > fn1-fp1): #=======================================================+++++++++++++++++
            fa1,fa2,fs=fa2-(fa1<<2),fa1,fa2 #----------------------
        # next 
        #fp=fa1
        #fn=((fa1+fa2)>>1)-(fa1<<1)   #---------------------- ############ check these
        #fn2=(fp<<1 )+fn #----------------------
        #fp2=(fn2<<1 )-fp #----------------------
        fp=fa1
        fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
        fn2=(fa2+fa1)>>1 #----------------------
        fp2= fa2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest
   
    flag=True
    while(fn > 1 and fp > 1 ):
        print("1",flag,fn,fp,fn1,fp1,fn2,fp2,fp1-fn,fn1+fp,fp1-fn1)
        if arr[fp1-fn] < x < arr[fn1+fp]:
            # next -1
            fn2,fn=fn,fn2 - (fn<<2) #----------------------
            fp2,fp=fp,fp2 - (fp<<2 ) #----------------------
            flag=False
        elif x < arr[fp1-fn] :
            if flag:
                if arr[prv] <= x < arr[fp1-fn]:
                    f1=(fn+fn2)>>1 #----------------------
                    f2=f1-fn
                    if prv > fp1-f2:
                        return xx(arr,x,fp1-fn,prv,fn,fn2) # bw prv and fn
                    elif prv > fp1-f1:
                        if x == arr[fp1-f2]:
                            return  fp1-f2
                        elif x < arr[fp1-f2]:
                            return  xx(arr,x,fp1-f2,prv,fn,fn2) #prv ,f2
                        elif x <  arr[fp1-fn]:
                            return xx(arr,x,fp1-fn,fp1-f2,fn,fn2) # f2, fn
                    elif prv > fp1-fn2:
                        if x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1,prv,fn,fn2) #prv ,f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2,fp1-f1,fn,fn2) # f1, f2
                        elif x <  arr[fp1-fn]:
                            return xx(arr,x,fp1-fn,fp1-f2,fn,fn2) # f2, fn
                    elif prv < fp1-fn2:
                        if x == arr[fp1-fn2]:
                            return  fp1-fn2
                        elif x < arr[fp1-fn2]:
                            return  xx(arr,x,fp1-fn2,prv,fn,fn2) #prv ,fn2
                        elif x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1,fp1-fn2,fn,fn2) #fn2 ,f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2,fp1-f1,fn,fn2) # f1, f2
                        elif x <  arr[fp1-fn]:
                            return xx(arr,x,fp1-fn,fp1-f2,fn,fn2) # f2, fn
                else:
                    print("f")
                    return -1

            else :
                f1=(fn+fn2)>>1 #----------------------
                if x== arr[fp1-f1]:
                    return fp1-f1
                elif x <  arr[fp1-f1]:
                    return xx(arr,x,fp1-f1,fp1-fn2,fn,fn2)
                else:
                    f2=f1-fn
                    if x == arr[fp1-f2]:
                        return fp1-f2
                    elif x < arr[fp1-f2]:
                        return xx(arr,x,fp1-f2,fp1-f1,fn,fn2)
                    else :
                        return xx(arr,x,fp1-fn,fp1-f2,fn,fn2)
        elif x == arr[fp1-fn]:
            return fp1-fn
        
        elif x > arr[fn1+fp]:
            if flag :
                if arr[fn1+fp] < x <= arr[prv1]:
                    f1=(fp+fp2)>>1 #----------------------
                    f2=f1-fp 
                    if prv1 < fn1+f2:
                        return xx(arr,x,prv1,fn1+fp,fp,fp2) # bw prv1 and fp
                    elif prv1 < fn1+f1:
                        if x == arr[fn1+f2]:
                            return  fn1+f2
                        elif x > arr[fn1+f2]:
                            return  xx(arr,x,prv1,fn1+f2,fp,fp2) #prv1 ,f2
                        elif x >  arr[fn1+fp]:
                            return xx(arr,x,fn1+f2,fn1+fp,fp,fp2) # f2, fp
                    elif prv1 < fn1+fp2:
                        if x == arr[fn1+f1]:
                            return  fn1+f1
                        elif x > arr[fn1+f1]:
                            return  xx(arr,x,prv1,fn1+f1,fp,fp2) #prv1 ,f1
                        elif x == arr[fn1+f2]:
                            return fn1+f2
                        elif x >  arr[fn1+f2]:
                            return xx(arr,x,fn1+f1,fn1+f2,fp,fp2) # f1, f2
                        elif x >  arr[fn1+fp]:
                            return xx(arr,x,fn1+f2,fn1+fp,fp,fp2) # f2, fp
                else:
                    return -1
            else :            
                f1=(fp+fp2)>>1 #----------------------
                if x== arr[fn1+f1]:
                    return fn1+f1
                elif x > arr[fn1+f1]:
                    return xx(arr,x,fn1+fp2,fn1+f1,fp,fp2)
                else:
                    f2=f1-fp
                    if x == arr[fn1+f2]:
                        return fn1+f2
                    elif x > arr[fn1+f2]:
                        return xx(arr,x,fn1+f1,fn1+f2,fp,fp2)
                    else :
                        return xx(arr,x,fn1+f2,fn1+fp,fp,fp2)
        elif x == arr[fn1+fp]:
            return fn1+fp
        elif (fn1+fp) <= (fp1-fn) :
            print("bo",fn1+fp,fp1-fn,fn,fp,fn1,fp1,fn2,fp2)
            return -1


arr=[i for i in range(1,10001)]
l=len(arr)
f1=1
f11=3
f21=13
while (f21 < l):
    f1,f11,f21=f11,f21,(f21<<2)+f1  #----------------------
print(f1,f11,f21,((f11+f21)>>1)-(f11<<1))
print(xx(arr,2000,fp1=l,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11)) #----------------------
print(xx(arr,2000,fp1=l,fn1=0,fa1=5425,fa2=8970)) #----------------------






if arr[prv] <= x < arr[fn]:
    
    f1=(fn+fn2) #----------------------
    f2=f1-fn
    if prv > f2:
        return xx(arr,x,fp1-fn,prv,fn,fn2) # bw prv and fn
    elif prv > f1:
        if x == arr f2:
            return  f2
        elif x < f2:
            return  xx(arr,x,fp1-f2,prv,fn,fn2) #prv ,f2
        elif x <  fn:
            return xx(arr,x,fp1-fn,fp1-f2,fn,fn2) # f2, fn
    elif prv > fn2:
        if x == arr f1:
            return  f1
        elif x < f1:
            return  xx(arr,x,fp1-f1,prv,fn,fn2) #prv ,f1
        if x == arr f2
            return f2
        elif x <  f2:
            return xx(arr,x,fp1-f2,fp1-f1,fn,fn2) # f1, f2
        elif x <  fn:
            return xx(arr,x,fp1-fn,fp1-f2,fn,fn2) # f2, fn
    elif prv < fn2:
        if x == arr fn2:
            return  fn2
        elif x < fn2:
            return  xx(arr,x,fp1-fn2,prv,fn,fn2) #prv ,fn2
        elif x == arr f1:
            return  f1
        elif x < f1:
            return  xx(arr,x,fp1-f1,fp1-fn2,fn,fn2) #fn2 ,f1
        if x == arr f2
            return f2
        elif x <  f2:
            return xx(arr,x,fp1-f2,fp1-f1,fn,fn2) # f1, f2
        elif x <  fn:
            return xx(arr,x,fp1-fn,fp1-f2,fn,fn2) # f2, fn
else:
    return -1





if arr[fp] < x <= arr[prv1]:
    
    f1=(fp+fp2) #----------------------
    f2=f1-fp 
    if prv1 < f2:
        return xx(arr,x,prv1,fn1+fp,fp,fp2) # bw prv1 and fp
    elif prv1 < f1:
        if x == arr f2:
            return  f2
        elif x > f2:
            return  xx(arr,x,prv1,fn1+f2,fp,fp2) #prv1 ,f2
        elif x >  fp:
            return xx(arr,x,fn1+f2,fn1+fp,fp,fp2) # f2, fp
    elif prv1 < fp2:
        if x == arr f1:
            return  f1
        elif x > f1:
            return  xx(arr,x,prv1,fn1+f1,fp,fp2) #prv1 ,f1
        if x == arr f2
            return f2
        elif x >  f2:
            return xx(arr,x,fn1+f1,fn1+f2,fp,fp2) # f1, f2
        elif x >  fp:
            return xx(arr,x,fn1+f2,fn1+fp,fp,fp2) # f2, fp
else:
    return -1

if arr[prv] <= x < arr[fn]:
    f2=
    if x > arr[fp1-f2]:
        if prv =< fp1-f2:
            return xx() # bw f2 and fn
        else :
            return xx() # bw prv and fn
    else:
        f1=
        if x > arr[fp1-f1]:
            if prv =< fp1-f1:
                return xx() # bw f1 and f2
            else :
                return xx() # bw prv and f2
        else:
            if x > 
            
            return xx() # bw prv and f1
else :
    return -1


if arr[prv1] <= x < arr[fn]:
    f2=
    if x > arr[fp1-f2]:
        if prv1 =< fp1-f2:
            return xx() # bw f2 and fn
        else :
            return xx() # bw prv1 and fn
    else:
        f1=
        if x > arr[fp1-f1]:
            if prv1 =< fp1-f1:
                return xx() # bw f1 and f2
            else :
                return xx() # bw prv1 and f2
        else:
            return xx() # bw prv1 and f1
else :
    return -1









if  x >= f2 =< fp1 :
    if x == arr[fp1-f2]:
        return fp1-f2
    
    return xx() # bw f2 and fn
else :
    f1=
    if  x >= f1 =< fp1 :
        if x == arr[fp1-f1]:
            return fp1-f1
        return xx() # bw f1 and f2
    elif x >= fn2 =< fp1 :
        return xx() # bw fn2 and f1
    return xx() # bw fn2 and f1

f2= ##############################################
if  x >= f2 =< fp1 :
    if x == arr[fp1-f2]:
        return fp1-f2
    
    return xx() # bw f2 and fn
else :
    f1=
    if  x >= f1 =< fp1 :
        if x == arr[fp1-f1]:
            return fp1-f1
        return xx() # bw f1 and f2
    elif x >= fn2 =< fp1 :
        return xx() # bw fn2 and f1
    return xx() # bw fn2 and f1
 check  fn2,f1,f2 indexes in upper limit of arr 
return xx(arr,x,fp1-f1,qwqw,fn,fn2) # handling first limits of Area of interset 









def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None): # add max fn,fn2
    # fn = fn or [l-fn]
    # fp = fn+1
    # fp1=i
    # fn1=j
    
    # next itter  planing i and j where to put them
    # re-find  fibs of compaired length
    
    # fib desend lower then i-j
    # want f's big 2 in function arg
    print("initial",fa1,fa2)
    # fa2 bigger
    if x1==True: # can go to 0
        fp=fa2
        fn=fa1  
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=fn1,fp1
        print("hoho")
    else :
        while ( fa1 > fp1-fn1):
            fa1,fa2=fa2-(fa1<<2),fa1 #----------------------
            print("after",fa1,fa2,fp1-fn1)
            print(x1,"...>")
        # next 
        #fp=fa1
        #fn=((fa1+fa2)>>1)-(fa1<<1)   #---------------------- ############ check these
        #fn2=(fp<<1 )+fn #----------------------
        #fp2=(fn2<<1 )-fp #----------------------
        fp=fa1
        fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
        fn2=(fa2+fa1)>>1 #----------------------
        fp2= fa2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest
   
    flag=True
    while(fn > -1 or fp > 0 ):
        print(">>>>","flag:",flag,"fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1)
        if arr[fp1-fn] < x < arr[fn1+fp]:
            # next -1
            print("boopn fn2,fn",fn2,fn)
            print("boopp fn2,fn",fp2,fp)
            fn,fn2=fn2-(fn<<2),fn #----------------------
            fp,fp2=fp2-(fp<<2),fp #----------------------
            #fn2,fn=fn,fn2 - (fn<<2) #----------------------
            #fp2,fp=fp,fp2 - (fp<<2 ) #----------------------
            print("boopn1 fn2,fn",fn2,fn)
            print("boopp1 fn2,fn",fp2,fp)
            flag=False
        elif x == arr[fp1-fn]:
            return fp1-fn
        elif x < arr[fp1-fn] :
            print("fdsf------",fp1-fn)
            if flag:
                if arr[prv] <= x < arr[fp1-fn]:
                    print("fdsf------1")
                    f1=(fn+fn2)>>1 #----------------------
                    f2=f1-fn
                    print(fp1-f2,fp1-f1,fp1-f2)
                    if  arr[prv] == x:
                        return prv
                    elif arr[fp1-f2]==x: # new edit
                        return fp1-f2
                    elif arr[fp1-f1]==x:
                        return fp1-f1
                    elif arr[fp1-f2]==x:
                        return fp1-f2   # new edit
                    elif prv > fp1-f2:
                        print("fdsf------2")
                        return xx(arr,x,fp1-fn-1,prv+1,fp,fp2) # bw prv and fn `1
                    elif prv > fp1-f1:
                        print("fdsf------3")
                        if x == arr[fp1-f2]:
                            return  fp1-f2
                        elif x < arr[fp1-f2]:
                            return  xx(arr,x,fp1-f2-1,prv+1,fp,fp2) #prv ,f2 `22
                        elif x <  arr[fp1-fn]:
                            return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `23
                    elif prv > fp1-fn2:
                        print("fdsf------4")
                        if x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1-1,prv+1,fp,fp2) #prv ,f1 `31
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2  `32
                        elif x <  arr[fp1-fn]:
                            return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn  `33
                    elif prv < fp1-fn2:
                        print("fdsf------5")
                        if x == arr[fp1-fn2]:
                            return  fp1-fn2
                        elif x < arr[fp1-fn2]:
                            return  xx(arr,x,fp1-fn2-1,prv+1,fp,fp2) #prv ,fn2  `41
                        elif x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2) #fn2 ,f1  `42
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2 `43
                        elif x <  arr[fp1-fn]:
                            return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `44
                    else :
                        print("?")
                        return -1
                else:
                    print("f")
                    return -1

            else :
                print("->/") 
                f1=(fn+fn2)>>1 #----------------------
                if x== arr[fp1-f1]:
                    return fp1-f1
                elif x <  arr[fp1-f1]:
                    return xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2)
                else:
                    f2=f1-fn
                    if x == arr[fp1-f2]:
                        return fp1-f2
                    elif x < arr[fp1-f2]:
                        return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2)
                    else :
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2)

        elif x == arr[fn1+fp]:
            return fn1+fp        
        elif x > arr[fn1+fp]:
            if flag :
                print(arr[fn1+fp],"dsafdsf++++++++++++==")
                if arr[fn1+fp] < x <= arr[prv1]:
                    if  arr[prv1] == x:
                        return prv1
                    f1=(fp+fp2)>>1 #----------------------
                    f2=f1-fp 
                    if prv1 < fn1+f2:
                        return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2) # bw prv1 and fp
                    elif prv1 < fn1+f1:
                        if x == arr[fn1+f2]:
                            return  fn1+f2
                        elif x > arr[fn1+f2]:
                            return  xx(arr,x,prv1-1,fn1+f2+1,fp,fp2) #prv1 ,f2
                        elif x >  arr[fn1+fp]:
                            return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                    elif prv1 < fn1+fp2:
                        if x == arr[fn1+f1]:
                            return  fn1+f1
                        elif x > arr[fn1+f1]:
                            return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
                        elif x == arr[fn1+f2]:
                            return fn1+f2
                        elif x >  arr[fn1+f2]:
                            return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2) # f1, f2
                        elif x >  arr[fn1+fp]:
                            return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                else:
                    return -1
            else :        
                print("->/")    
                f1=(fp+fp2)>>1 #----------------------
                if x== arr[fn1+f1]:
                    return fn1+f1
                elif x > arr[fn1+f1]:
                    return xx(arr,x,fn1+fp2-1,fn1+f1+1,fp,fp2)
                else:
                    f2=f1-fp
                    if x == arr[fn1+f2]:
                        return fn1+f2
                    elif x > arr[fn1+f2]:
                        return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2)
                    else :
                        return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2)

        elif (fn1+fp) >= (fp1-fn) :
        elif fn1 >= fp1 :
            print("bo",fn1+fp,fp1-fn,fn,fp,fn1,fp1,fn2,fp2)
            return -1
    else:
        return -101




















def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None): # add max fn,fn2
    # fn = fn or [l-fn]
    # fp = fn+1
    # fp1=i
    # fn1=j
    
    # next itter  planing i and j where to put them
    # re-find  fibs of compaired length
    
    # fib desend lower then i-j
    # want f's big 2 in function arg
    print("initial",fa1,fa2)
    # fa2 bigger
    if x1==True: # can go to 0
        fp=fa2
        fn=fa1  
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=fn1,fp1
        print("hoho")
    else :
        while ( fa1 > fp1-fn1):
            fa1,fa2=fa2-(fa1<<2),fa1 #----------------------
            print("after",fa1,fa2,fp1-fn1)
        # next 
        #fp=fa1
        #fn=((fa1+fa2)>>1)-(fa1<<1)   #---------------------- ############ check these
        #fn2=(fp<<1 )+fn #----------------------
        #fp2=(fn2<<1 )-fp #----------------------
        fp=fa1
        fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
        fn2=(fa2+fa1)>>1 #----------------------
        fp2= fa2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest
   
    flag=True
    while(fn > -1 or fp > 0 ):
        print(">>>>","flag:",flag,"fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1)
        if arr[fp1-fn] < x < arr[fn1+fp]:
            # next -1
            print("boopn fn2,fn",fn2,fn)
            print("boopp fn2,fn",fp2,fp)
            fn,fn2=fn2-(fn<<2),fn #----------------------
            fp,fp2=fp2-(fp<<2),fp #----------------------
            print("boopn1 fn2,fn",fn2,fn)
            print("boopp1 fn2,fn",fp2,fp)
            flag=False
        elif x == arr[fp1-fn]:
            return fp1-fn
        elif x == arr[fn1+fp]:
            return fn1+fp        

        elif x < arr[fp1-fn] :
            print("fdsf------",fp1-fn)
            if flag:
                if arr[prv] <= x :
                    print("fdsf------1")
                    f1=(fn+fn2)>>1 #----------------------
                    f2=f1-fn
                    print("}}",fp1-f2,fp1-f1,fp1-fn2,prv)
                    if  arr[prv] == x:
                        return prv
                    elif prv >= fp1-f2:
                        print("fdsf------2")
                        return xx(arr,x,fp1-fn-1,prv+1,fp,fp2) # bw prv and fn `1
                    elif prv >= fp1-f1:
                        print("fdsf-----/-3")
                        if x == arr[fp1-f2]:
                            return  fp1-f2
                        elif x < arr[fp1-f2]:
                            return  xx(arr,x,fp1-f2-1,prv+1,fp,fp2) #prv ,f2 `22
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `23
                    elif prv >= fp1-fn2:
                        print("fdsf------4")
                        if x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1-1,prv+1,fp,fp2) #prv ,f1 `31
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2  `32
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn  `33
                    elif prv <= fp1-fn2:
                        print("fdsf------5")
                        if x == arr[fp1-fn2]:
                            return  fp1-fn2
                        elif x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x < arr[fp1-fn2]:
                            return  xx(arr,x,fp1-fn2-1,prv+1,fp,fp2) #prv ,fn2  `41
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2) #fn2 ,f1  `42
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2 `43
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `44
                    else :
                        print("?")
                        return -1
                else:
                    print("f")
                    return -1

            else :
                print("->/") 
                f1=(fn+fn2)>>1 #----------------------
                f2=f1-fn
                if x== arr[fp1-f1]:
                    return fp1-f1
                elif x == arr[fp1-f2]:
                    return fp1-f2
                elif x <  arr[fp1-f1]:
                    return xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2)
                elif x < arr[fp1-f2]:
                    return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2)
                return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2)

        elif x > arr[fn1+fp]:
            if flag :
                print(arr[fn1+fp],"dsafdsf++++++++++++==")
                if x <= arr[prv1]:
                    f1=(fp+fp2)>>1 #----------------------
                    f2=f1-fp 
                    if  arr[prv1] == x:
                        return prv1
                    elif prv1 <= fn1+f2:
                        return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2) # bw prv1 and fp
                    elif prv1 <= fn1+f1:
                        if x == arr[fn1+f2]:
                            return  fn1+f2
                        elif x > arr[fn1+f2]:
                            return  xx(arr,x,prv1-1,fn1+f2+1,fp,fp2) #prv1 ,f2
                        return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                    elif prv1 <= fn1+fp2:
                        if x == arr[fn1+f1]:
                            return  fn1+f1
                        elif x == arr[fn1+f2]:
                            return fn1+f2
                        elif x > arr[fn1+f1]:
                            return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
                        elif x >  arr[fn1+f2]:
                            return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2) # f1, f2
                        return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                    else :
                        print("?")
                        return -1
                else:
                    return -1
            else :        
                print("->/")    
                f1=(fp+fp2)>>1 #----------------------
                f2=f1-fp
                if x== arr[fn1+f1]:
                    return fn1+f1
                elif x == arr[fn1+f2]:
                    return fn1+f2
                elif x > arr[fn1+f1]:
                    return xx(arr,x,fn1+fp2-1,fn1+f1+1,fp,fp2)
                elif x > arr[fn1+f2]:
                    return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2)
                return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2)

        elif (fn1+fp) >= (fp1-fn) :
        #elif fn1 >= fp1 :
            print("bo",fn1+fp,fp1-fn,fn,fp,fn1,fp1,fn2,fp2)
            return -1
    else:
        return -101




arr=[i for i in range(1,100000)]
arr=[ i+0.10 for i in arr ]

arr=[i for i in range(1,100000)]
arr=[i for i in range(-15,-1)] # min for arr len() = 14
arr=[i for i in range(1,10000000)]
arr=[i for i in range(1,40000000)]
arr=[i for i in range(9000000,10000000)]
arr=[i for i in range(1,7000000)]
arr=[i for i in range(700000,800000)]
print(len(arr))
print(arr)
l=len(arr)
f1=3
f11=13
f21=55
while (f21 < l):
    f1,f11,f21=f11,f21,(f21<<2)+f11  #----------------------
print(f1,f11,f21,((f11+f21)>>1)-(f11<<1))
  #print(xx(arr,2000,fp1=l,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11)) #----------------------
print(xx(arr,106,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))
print(xx(arr,1,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))

[772548, 772549, 772551, 772552, 772603, 772604, 772606, 772607, 772747, 772748]


from timeit import default_timer as  timer

start= timer()
print(xx(arr,772551,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))
print(xx(arr,772550,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))

cc=[ xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) for i in arr] #----------------------

print(sum([i-j for i,j in  zip(arr,cc)]))

cc=[ True if xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) > -1 else False for i in arr] #----------------------

cc2=[ i  for i in arr if xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True)  == -1] #----------------------

cc3=[ i for i in cc2 if i > -1] #----------------------

print(cc2[:10],len(cc2))

c=[xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) for i in arr]
 #v=[ True if i > -1 else False for i in cc]
print(sum(cc),"-------------")
end= timer()
print(end-start)
n=[  for i in zip(cc,arr)]
print([ i for i in zip(cc,arr,c)])

cc=[xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) for i in arr]
print(cc[:100])
print(len(arr))




def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None): # add max fn,fn2
    if x1==True: # can go to 0
        fp=fa2
        fn=fa1  
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=fn1,fp1
    else :
        while ( fa1 > fp1-fn1):
            fa1,fa2=fa2-(fa1<<2),fa1 #----------------------
        fp=fa1
        fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
        fn2=(fa2+fa1)>>1 #----------------------
        fp2= fa2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest
   
    flag=True
    while(fn > -1 or fp > 0 ):
        if arr[fp1-fn] < x < arr[fn1+fp]:
            fn,fn2=fn2-(fn<<2),fn #----------------------
            fp,fp2=fp2-(fp<<2),fp #----------------------
            flag=False
        elif x == arr[fp1-fn]:
            return fp1-fn
        elif x == arr[fn1+fp]:
            return fn1+fp        

        elif x < arr[fp1-fn] :
            if flag:
                if arr[prv] <= x :
                    f1=(fn+fn2)>>1 #----------------------
                    f2=f1-fn
                    if  arr[prv] == x:
                        return prv
                    elif prv >= fp1-f2:
                        return xx(arr,x,fp1-fn-1,prv+1,fp,fp2) # bw prv and fn `1
                    elif prv >= fp1-f1:
                        if x == arr[fp1-f2]:
                            return  fp1-f2
                        elif x < arr[fp1-f2]:
                            return  xx(arr,x,fp1-f2-1,prv+1,fp,fp2) #prv ,f2 `22
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `23
                    elif prv >= fp1-fn2:
                        if x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1-1,prv+1,fp,fp2) #prv ,f1 `31
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2  `32
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn  `33
                    elif prv <= fp1-fn2:
                        if x == arr[fp1-fn2]:
                            return  fp1-fn2
                        elif x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x < arr[fp1-fn2]:
                            return  xx(arr,x,fp1-fn2-1,prv+1,fp,fp2) #prv ,fn2  `41
                        elif x < arr[fp1-f1]:
                            return  xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2) #fn2 ,f1  `42
                        elif x <  arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2 `43
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `44
                    else :
                        return -1
                else:
                    return -1

            else :
                f1=(fn+fn2)>>1 #----------------------
                f2=f1-fn
                if x== arr[fp1-f1]:
                    return fp1-f1
                elif x == arr[fp1-f2]:
                    return fp1-f2
                elif x <  arr[fp1-f1]:
                    return xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2)
                elif x < arr[fp1-f2]:
                    return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2)
                return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2)

        elif x > arr[fn1+fp]:
            if flag :
                if x <= arr[prv1]:
                    f1=(fp+fp2)>>1 #----------------------
                    f2=f1-fp 
                    if  arr[prv1] == x:
                        return prv1
                    elif prv1 <= fn1+f2:
                        return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2) # bw prv1 and fp
                    elif prv1 <= fn1+f1:
                        if x == arr[fn1+f2]:
                            return  fn1+f2
                        elif x > arr[fn1+f2]:
                            return  xx(arr,x,prv1-1,fn1+f2+1,fp,fp2) #prv1 ,f2
                        return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                    elif prv1 <= fn1+fp2:
                        if x == arr[fn1+f1]:
                            return  fn1+f1
                        elif x == arr[fn1+f2]:
                            return fn1+f2
                        elif x > arr[fn1+f1]:
                            return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
                        elif x >  arr[fn1+f2]:
                            return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2) # f1, f2
                        return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                    else :
                        return -1
                else:
                    return -1
            else :        
                f1=(fp+fp2)>>1 #----------------------
                f2=f1-fp
                if x== arr[fn1+f1]:
                    return fn1+f1
                elif x == arr[fn1+f2]:
                    return fn1+f2
                elif x > arr[fn1+f1]:
                    return xx(arr,x,fn1+fp2-1,fn1+f1+1,fp,fp2)
                elif x > arr[fn1+f2]:
                    return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2)
                return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2)

        elif (fn1+fp) >= (fp1-fn) :
            return -1
    else:
        return -101













    def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None): # add max fn,fn2
        if x1==True: # can go to 0
            fp=fa2
            fn=fa1  
            fn2=(fp<<1 )+fn #----------------------
            fp2=(fn2<<1 )-fp #----------------------
            prv,prv1=fn1,fp1
        else: # when  prv
            while ( fa1 > fp1-fn1):
                fa1,fa2=fa2-(fa1<<2),fa1 #----------------------
            fp=fa1
            fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
            fn2=(fa2+fa1)>>1 #----------------------
            fp2= fa2 #----------------------
            prv,prv1=fn1,fp1 # used for area of intrest
    #        if fp2 <= 55 :
    #            x1=False
    #    else : # when None
    #        fp=(fa2+fa1)>>1
    #        fn=fp-fa1   #----------------------
    #        fn2=fp+fa2 #----------------------
    #        fp2=fa2+fn2 #----------------------
    #        prv,prv1=fn1,fp1 # used for area of intrest
       
        flag=True
        while(fn > -1 or fp > 0 ):
    #        print(">>>>","flag:",flag,"fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence n : ",fn2-fn,"diffence p : ",fp2-fp)
            
            if arr[fp1-fn] < x < arr[fn1+fp]:
                fn,fn2=fn2-(fn<<2),fn #----------------------
                fp,fp2=fp2-(fp<<2),fp #----------------------
                flag=False
            elif x == arr[fp1-fn]:
                return fp1-fn
            elif x == arr[fn1+fp]:
                return fn1+fp

    #        elif fp <= 55 :
            elif fp <= 233  :
    #            print(">>>>","flag:",flag,"fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence n:",fn2-fn,"diffence p:",fp2-fp)
                if x < arr[fp1-fn] :
                    if flag:
                        if arr[prv] <= x :
                            f1=(fn+fn2)>>1 #----------------------
                            f2=f1-fn
                            if  arr[prv] == x:
                                return prv
                            elif prv >= fp1-f2:
                                return xx(arr,x,fp1-fn-1,prv+1,fp,fp2) # bw prv and fn `1
                            elif prv >= fp1-f1:
                                if x == arr[fp1-f2]:
                                    return  fp1-f2
                                elif x < arr[fp1-f2]:
                                    return  xx(arr,x,fp1-f2-1,prv+1,fp,fp2) #prv ,f2 `22
                                return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `23
                            elif prv >= fp1-fn2:
                                if x == arr[fp1-f1]:
                                    return  fp1-f1
                                elif x == arr[fp1-f2]:
                                    return fp1-f2
                                elif x < arr[fp1-f1]:
                                    return  xx(arr,x,fp1-f1-1,prv+1,fp,fp2) #prv ,f1 `31
                                elif x <  arr[fp1-f2]:
                                    return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2  `32
                                return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn  `33
                            elif prv <= fp1-fn2:
                                if x == arr[fp1-fn2]:
                                    return  fp1-fn2
                                elif x == arr[fp1-f1]:
                                    return  fp1-f1
                                elif x == arr[fp1-f2]:
                                    return fp1-f2
                                elif x < arr[fp1-fn2]:
                                    return  xx(arr,x,fp1-fn2-1,prv+1,fp,fp2) #prv ,fn2  `41
                                elif x < arr[fp1-f1]:
                                    return  xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2) #fn2 ,f1  `42
                                elif x <  arr[fp1-f2]:
                                    return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2 `43
                                return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `44
                            else :

                                return -1
                        else:
                            return -1

                    else :
                        f1=(fn+fn2)>>1 #----------------------
                        f2=f1-fn
                        if x== arr[fp1-f1]:
                            return fp1-f1
                        elif x == arr[fp1-f2]:
                            return fp1-f2
                        elif x <  arr[fp1-f1]:
                            return xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2)
                        elif x < arr[fp1-f2]:
                            return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2)
                        return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2)

                elif x > arr[fn1+fp]:
                    if flag :
                        if x <= arr[prv1]:
                            f1=(fp+fp2)>>1 #----------------------
                            f2=f1-fp 
                            if  arr[prv1] == x:
                                return prv1
                            elif prv1 <= fn1+f2:
                                return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2) # bw prv1 and fp
                            elif prv1 <= fn1+f1:
                                if x == arr[fn1+f2]:
                                    return  fn1+f2
                                elif x > arr[fn1+f2]:
                                    return  xx(arr,x,prv1-1,fn1+f2+1,fp,fp2) #prv1 ,f2
                                return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                            elif prv1 <= fn1+fp2:
                                if x == arr[fn1+f1]:
                                    return  fn1+f1
                                elif x == arr[fn1+f2]:
                                    return fn1+f2
                                elif x > arr[fn1+f1]:
                                    return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
                                elif x >  arr[fn1+f2]:
                                    return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2) # f1, f2
                                return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
                            else :
                                return -1
                        else:
                            return -1
                    else :        
                        f1=(fp+fp2)>>1 #----------------------
                        f2=f1-fp
                        if x== arr[fn1+f1]:
                            return fn1+f1
                        elif x == arr[fn1+f2]:
                            return fn1+f2
                        elif x > arr[fn1+f1]:
                            return xx(arr,x,fn1+fp2-1,fn1+f1+1,fp,fp2)
                        elif x > arr[fn1+f2]:
                            return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2)
                        return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2)

    #        elif  x1 == None :        
            elif x < arr[fp1-fn] :
    #            print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff ",fp1-fn1)
                if flag:
                    if arr[prv] <= x :
                        if  arr[prv] == x:
                            return prv
                        elif prv <= fp1-fn2:
                            return xx(arr,x,fp1-fn2-1,prv+1,fp,fp2)
                        return xx(arr,x,fp1-fn-1,prv+1,fp,fp2)
                    else:
    #                    print("===1")
                        return -1
                else :
                    return xx(arr,x,fp1-fn-1,fp1-fn2+1,fp,fp2)

            elif x > arr[fn1+fp]:
    #            print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff ",fp1-fn1)
                if flag :
                    if x <= arr[prv1]:
                        if  arr[prv1] == x:
                            return prv1
                        return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2)
                    else:
    #                    print("===2")
                        return -1
                else :        
                    return xx(arr,x,fn1+fp2-1,fn1+fp+1,fp,fp2)
            elif (fn1+fp) >= (fp1-fn) :
    #            print("===3")
                return -1
        else:
            return -101










def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None): # add max fn,fn2
    if x1==True: # can go to 0
        fp=fa2
        fn=fa1  
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=fn1,fp1
    else: # when  prv
        while ( fa1 > fp1-fn1):
            fa1,fa2=fa2-(fa1<<2),fa1 #----------------------
        fp=fa1
        fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
        fn2=(fa2+fa1)>>1 #----------------------
        fp2= fa2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest
        if fp2 <= 55 :
            x1=False
    else : # when None
        fp=(fa2+fa1)>>1
        fn=fp-fa1   #----------------------
        fn2=fp+fa2 #----------------------
        fp2=fa2+fn2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest

    while(fn > -1 or fp > 0 ):
        print("fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence n : ",fn2-fn,"diffence p : ",fp2-fp)
        #print(f"xx(arr,x,fp1={fp1},fn1={fn1},fa1={fa1},fa2={fa2},x1=None)")
        
        if arr[fp1-fn] < x < arr[fn1+fp]:
            fn,fn2=fn2-(fn<<2),fn #----------------------
            fp,fp2=fp2-(fp<<2),fp #----------------------
            flag=False
        elif x == arr[fp1-fn]:
            return fp1-fn
        elif x == arr[fn1+fp]:
            return fn1+fp




    #        elif fn <= 1  :
    #            print(">>>>","flag:",flag,"fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence n:",fn2-fn,"diffence p:",fp2-fp)
    #            if x < arr[fp1-fn] :
    #                if flag:
    #                    if arr[prv] <= x :
    #                        f1=(fn+fn2)>>1 #----------------------
    #                        f2=f1-fn
    #                        if  arr[prv] == x:
    #                            return prv
    #                        elif prv >= fp1-f2:
    #                            return xx(arr,x,fp1-fn-1,prv+1,fp,fp2) # bw prv and fn `1
    #                        elif prv >= fp1-f1:
    #                            if x == arr[fp1-f2]:
    #                                return  fp1-f2
    #                            elif x < arr[fp1-f2]:
    #                                return  xx(arr,x,fp1-f2-1,prv+1,fp,fp2) #prv ,f2 `22
    #                            return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `23
    #                        elif prv >= fp1-fn2:
    #                            if x == arr[fp1-f1]:
    #                                return  fp1-f1
    #                            elif x == arr[fp1-f2]:
    #                                return fp1-f2
    #                            elif x < arr[fp1-f1]:
    #                                return  xx(arr,x,fp1-f1-1,prv+1,fp,fp2) #prv ,f1 `31
    #                            elif x <  arr[fp1-f2]:
    #                                return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2  `32
    #                            return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn  `33
    #                        elif prv <= fp1-fn2:
    #                            if x == arr[fp1-fn2]:
    #                                return  fp1-fn2
    #                            elif x == arr[fp1-f1]:
    #                                return  fp1-f1
    #                            elif x == arr[fp1-f2]:
    #                                return fp1-f2
    #                            elif x < arr[fp1-fn2]:
    #                                return  xx(arr,x,fp1-fn2-1,prv+1,fp,fp2) #prv ,fn2  `41
    #                            elif x < arr[fp1-f1]:
    #                                return  xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2) #fn2 ,f1  `42
    #                            elif x <  arr[fp1-f2]:
    #                                return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2) # f1, f2 `43
    #                            return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2) # f2, fn `44
    #                        else :
    #
    #                            return -1
    #                    else:
    #                        return -1
    #
    #                else :
    #                    f1=(fn+fn2)>>1 #----------------------
    #                    f2=f1-fn
    #                    if x== arr[fp1-f1]:
    #                        return fp1-f1
    #                    elif x == arr[fp1-f2]:
    #                        return fp1-f2
    #                    elif x <  arr[fp1-f1]:
    #                        return xx(arr,x,fp1-f1-1,fp1-fn2+1,fp,fp2)
    #                    elif x < arr[fp1-f2]:
    #                        return xx(arr,x,fp1-f2-1,fp1-f1+1,fp,fp2)
    #                    return xx(arr,x,fp1-fn-1,fp1-f2+1,fp,fp2)
    #
    #            elif x > arr[fn1+fp]:
    #                if flag :
    #                    if x <= arr[prv1]:
    #                        f1=(fp+fp2)>>1 #----------------------
    #                        f2=f1-fp 
    #                        if  arr[prv1] == x:
    #                            return prv1
    #                        elif prv1 <= fn1+f2:
    #                            return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2) # bw prv1 and fp
    #                        elif prv1 <= fn1+f1:
    #                            if x == arr[fn1+f2]:
    #                                return  fn1+f2
    #                            elif x > arr[fn1+f2]:
    #                                return  xx(arr,x,prv1-1,fn1+f2+1,fp,fp2) #prv1 ,f2
    #                            return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
    #                        elif prv1 <= fn1+fp2:
    #                            if x == arr[fn1+f1]:
    #                                return  fn1+f1
    #                            elif x == arr[fn1+f2]:
    #                                return fn1+f2
    #                            elif x > arr[fn1+f1]:
    #                                return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
    #                            elif x >  arr[fn1+f2]:
    #                                return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2) # f1, f2
    #                            return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2) # f2, fp
    #                        else :
    #                            return -1
    #                    else:
    #                        return -1
    #                else :        
    #                    f1=(fp+fp2)>>1 #----------------------
    #                    f2=f1-fp
    #                    if x== arr[fn1+f1]:
    #                        return fn1+f1
    #                    elif x == arr[fn1+f2]:
    #                        return fn1+f2
    #                    elif x > arr[fn1+f1]:
    #                        return xx(arr,x,fn1+fp2-1,fn1+f1+1,fp,fp2)
    #                    elif x > arr[fn1+f2]:
    #                        return xx(arr,x,fn1+f1-1,fn1+f2+1,fp,fp2)
    #                    return xx(arr,x,fn1+f2-1,fn1+fp+1,fp,fp2)

    #        elif  x1 == None :        
    #        elif x < arr[fp1-fn] :
    #            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
    #            if flag:
    #                if arr[prv] <= x :
    #                    if  arr[prv] == x:
    #                        return prv
    #                    elif prv <= fp1-fn2:
    #                        if x == arr[fp1-fn2]:
    #                            return  fp1-fn2
    #                        elif x < arr[fp1-fn2]:
    #                            return xx(arr,x,fp1-fn2-1,prv+1,fp,fp2)
    #                        
    #                    return xx(arr,x,fp1-fn-1,prv+1,fp,fp2)
    #                else:
    #             #       print("===1")
    #                    return -1
    #            else :
    #                return xx(arr,x,fp1-fn-1,fp1-fn2+1,fp,fp2)
    #
    #        elif x > arr[fn1+fp]:
    #            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
    #            if flag :
    #                if x <= arr[prv1]:
    #                    if  arr[prv1] == x:
    #                        return prv1
    #                    return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2)
    #                else:
    #              #      print("===2")
    #                    return -1
    #            else :        
    #                return xx(arr,x,fn1+fp2-1,fn1+fp+1,fp,fp2)
    #        elif (fn1+fp) >= (fp1-fn) :
    #            #print("===3")
    #            return -1





        elif x < arr[fp1-fn] :
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
            f1=(fn+fn2)>>1 #----------------------
            if arr[prv] <= x :
                if  arr[prv] == x:
                    return prv
                elif prv <= fp1-f1:
                    if x == arr[fp1-f1]:
                        return  fp1-f1
                    elif x < arr[fp1-f1]:
                        return xx(arr,x,fp1-f1-1,prv+1,fp,fp2)
                    return xx(arr,x,fp1-fn-1,fp1-f1-1,fp,fp2)                    
                return xx(arr,x,fp1-fn-1,prv+1,fp,fp2)
            else:
         #       print("===1")
                return -1

        elif x > arr[fn1+fp]:
            f1=(fp+fp2)>>1 #----------------------
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
            if x <= arr[prv1]:
                if  arr[prv1] == x:
                    return prv1
                elif prv1 >= fn1+f1:
                    if x == arr[fn1+f1]:
                        return  fn1+f1
                    elif x > arr[fn1+f1]:
                        return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
                    return xx(arr,x,fn1+f1-1,fn1+fp+1,fp,fp2) # f2, fp

                return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2)
            else:
          #      print("===2")
                return -1
        elif (fn1+fp) >= (fp1-fn) :
            #print("===3")
            return -1

    else:
        return -101


 ITERATIVE <<<<<<<<<<<<<<<<<<



nn=[17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 68, 69, 71, 72, 73, 105, 106, 107, 113, 114, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 258, 260, 261, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 297, 298, 299, 300]

for  i in nn: 
    print(xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))
    print("----     "*9)

print(xx(arr,20,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))
print(xx(arr,299,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))



print(xx(arr,1024,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))


[4831, 4832, 4833, 4834, 4835, 4836, 4837, 4838, 4839, 4840]

print(xx(arr,68,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))

cc=[ xx(arr,i,fp1=l-1,fn1=0,fa1=gg,fa2=f11,x1=True) for i in arr] #----------------------

print(sum([i-j for i,j in  zip(arr,cc) if j> -1 ]))
print([i for i,j in zip(arr,cc) if j == -1][:10])




print(xx(arr,772551,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))
print(xx(arr,772550,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True))

cc=[ xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) for i in arr] #----------------------

print(sum([i-j for i,j in  zip(arr,cc)]))

print(arr[:10],cc[:10],arr[-10:-1],cc[-10:-1])

cc3=[ i for i in cc if i == -1] #----------------------

print(cc3)

cc=[ True if xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) > -1 else False for i in arr] #----------------------

cc2=[ i  for i in arr if xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True)  == -1] #----------------------

cc3=[ i for i in cc2 if i > -1] #----------------------

print(cc2[:10],len(cc2))

c=[xx(arr,i,fp1=l-1,fn1=0,fa1=((f11+f21)>>1)-(f11<<1),fa2=f11,x1=True) for i in arr]
 #v=[ True if i > -1 else False for i in cc]
print(sum(cc),"-------------")


from timeit import default_timer as  timer

start= timer()
cc=[ xx(arr,i,fp1=l-1,fn1=0,fa1=gg,fa2=f11,x1=True) for i in arr] #----------------------
end= timer()
print(end-start)





        elif x < arr[fp1-fn] :
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
            if arr[prv] <= x :
                if  arr[prv] == x:
                    return prv
                elif prv <= fp1-fn2:
                    if x == arr[fp1-fn2]:
                        return  fp1-fn2
                    elif x < arr[fp1-fn2]:
                        return xx(arr,x,fp1-fn2-1,prv+1,fp,fp2)
                return xx(arr,x,fp1-fn-1,prv+1,fp,fp2)
            else:
         #       print("===1")
                return -1

        elif x > arr[fn1+fp]:
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
            if x <= arr[prv1]:
                if  arr[prv1] == x:
                    return prv1
                return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2)
            else:
          #      print("===2")
                return -1
        elif (fn1+fp) >= (fp1-fn) :
            #print("===3")
            return -1









print(gg)

fibMMm2 = 0  # (m-2)'th Fibonacci No.
fibMMm1 = 1  # (m-1)'th Fibonacci No.
fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
while (fibM < l):
    fibMMm2 = fibMMm1
    fibMMm1 = fibM
    fibM = fibMMm2 + fibMMm1


def fibMonaccianSearch(arr, x, n,fibM,fibMMm2,fibMMm1):
    #    fibMMm2 = 5702887
    #    fibMMm1 = 9227465
    #    fibM = 14930352
    #    fibMMm2 = f2
    #    fibMMm1 = f1
    #    fibM = f
    #    # print(fibM,fibMMm2,fibMMm1)
    offset = -1
    while (fibM > 1):
        if n-1 == min(offset+fibMMm2, n-1):
            i=n-1                       
        else :            
            i=offset+fibMMm2        
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

from timeit import default_timer as  timer
start= timer()

cc=[ fibMonaccianSearch(arr, i+0.10, l,fibM,fibMMm2,fibMMm1) for i in arr]
print(fibMonaccianSearch(arr,9000000.10 , l,fibM,fibMMm2,fibMMm1))
end= timer()
print(end-start)



from timeit import default_timer as  timer

start= timer()
lp=[ fibMonaccianSearch(arr, i, 1000000) for i in arr]

end= timer()
print(end-start)



def xx(arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None): # add max fn,fn2



    if x1==True: # can go to 0
        fp=fa2
        fn=fa1  
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=fn1,fp1
    else: # when  prv
        while ( fa1 > fp1-fn1):
            fa1,fa2=fa2-(fa1<<2),fa1 #----------------------
        fp=fa1
        fn=((fa1+fa2)>>1)-(fa1<<1)   #----------------------
        fn2=(fa2+fa1)>>1 #----------------------
        fp2= fa2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest
        if fp2 <= 55 :
            x1=False
    else : # when None
        fp=(fa2+fa1)>>1
        fn=fp-fa1   #----------------------
        fn2=fp+fa2 #----------------------
        fp2=fa2+fn2 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest

    while(fn > -1 or fp > 0 ):
        print("fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence n : ",fn2-fn,"diffence p : ",fp2-fp)
        #print(f"xx(arr,x,fp1={fp1},fn1={fn1},fa1={fa1},fa2={fa2},x1=None)")
        
        if arr[fp1-fn] < x < arr[fn1+fp]:
            fn,fn2=fn2-(fn<<2),fn #----------------------
            fp,fp2=fp2-(fp<<2),fp #----------------------
            flag=False
        elif x == arr[fp1-fn]:
            return fp1-fn
        elif x == arr[fn1+fp]:
            return fn1+fp

        elif x < arr[fp1-fn] :
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
            f1=(fn+fn2)>>1 #----------------------
            if arr[prv] <= x :
                if  arr[prv] == x:
                    return prv
                elif prv <= fp1-f1:
                    if x == arr[fp1-f1]:
                        return  fp1-f1
                    elif x < arr[fp1-f1]:
                        return xx(arr,x,fp1-f1-1,prv+1,fp,fp2)
                    return xx(arr,x,fp1-fn-1,fp1-f1+1,fp,fp2)                    
                return xx(arr,x,fp1-fn-1,prv+1,fp,fp2)
            else:
         #       print("===1")
                return -1

        elif x > arr[fn1+fp]:
            f1=(fp+fp2)>>1 #----------------------
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
            if x <= arr[prv1]:
                if  arr[prv1] == x:
                    return prv1
                elif prv1 >= fn1+f1:
                    if x == arr[fn1+f1]:
                        return  fn1+f1
                    elif x > arr[fn1+f1]:
                        return  xx(arr,x,prv1-1,fn1+f1+1,fp,fp2) #prv1 ,f1
                    return xx(arr,x,fn1+f1-1,fn1+fp+1,fp,fp2) # f2, fp

                return xx(arr,x,prv1-1,fn1+fp+1,fp,fp2)
            else:
          #      print("===2")
                return -1
        elif (fn1+fp) >= (fp1-fn) :
            #print("===3")
            return -1

    else:
        return -101


def kartik_strafe_s(arr,x,fp,fn,l): # arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None
    fn2=(fp<<1 )+fn #----------------------
    fp2=(fn2<<1 )-fp #----------------------
    prv,prv1=0,l
    fn1,fp1=0,l
    print("_____+++__________+++")
    while(fn > -1 or fp > 0 ):
        print("fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fn2:",fn2,"fp2:",fp2,"fp1-fn:",fp1-fn,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence n : ",fn2-fn,"diffence p : ",fp2-fp)
        if arr[fp1-fn] < x < arr[fn1+fp]:
            fn,fn2=fn2-(fn<<2),fn #----------------------
            fp,fp2=fp2-(fp<<2),fp #----------------------
            flag=False
        elif x == arr[fp1-fn]:
            return fp1-fn
        elif x == arr[fn1+fp]:
            return fn1+fp

        elif x < arr[fp1-fn] :
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
            f1=(fn+fn2)>>1 #----------------------
            if arr[prv] <= x :
                if  arr[prv] == x:
                    return prv
                elif prv <= fp1-f1:
                    if x == arr[fp1-f1]:
                        return  fp1-f1
                    elif x < arr[fp1-f1]:
                        fp1,fn1=fp1-f1-1,prv+1
                    else :fp1,fn1=fp1-fn-1,fp1-f1+1                    
                else :
                    fp1,fn1=fp1-fn-1,prv+1              
            else:
         #       print("===1")
                return -1

        elif x > arr[fn1+fp]:
            f1=(fp+fp2)>>1 #----------------------
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
            if x <= arr[prv1]:
                if  arr[prv1] == x:
                    return prv1
                elif prv1 >= fn1+f1:
                    if x == arr[fn1+f1]:
                        return  fn1+f1
                    elif x > arr[fn1+f1]:
                        fp1,fn1=prv1-1,fn1+f1+1                    
                    else :
                        fp1,fn1=fn1+f1-1,fn1+fp+1                    
                else :
                    fp1,fn1=prv1-1,fn1+fp+1              
            else:
          #      print("===2")
                return -1
        elif (fn1+fp) >= (fp1-fn) :
            #print("===3")
            return -1
        while ( fp > fp1-fn1):
            print("++______+++++++")
            fp,fp2=fp2-(fp<<2),fp #----------------------
        fn=((fp+fp2)>>1)-(fp<<1)   #----------------------
        fn2=(fp2+fp)>>1 #----------------------
        prv,prv1=fn1,fp1 # used for area of intrest

    else:
        return -1

print(kartik_strafe_s(arr,772551,f11,gg,l-1))



cc=[ kartik_strafe_s(arr,i,f11,gg,l) for i in arr] #----------------------

from timeit import default_timer as  timer
start= timer()
cc=[ kartik_strafe_s(arr,i,f11,gg,l) for i in arr] #----------------------
end= timer()
print(end-start)
print(sum([i-j for i,j in  zip(arr,cc)]))


    def kartik_strafe_s(arr,x,fp,fn,l): # arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=0,l
        fn1,fp1=0,l
    #    print("_____+++__________+++")
        while(fp > 0 ):
            f1=(fp+fp2)>>1
    #        c1=fp1-fp
    #        c2=fn1+fp
    #        x1=arr[c1]
    #        x2=arr[c2]
    #        n1=arr[prv]
    #        n2=arr[prv1]
    #        print("fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fp2:",fp2,"fp1-fp:",fp1-fp,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence p : ",fp2-fp)
            if arr[fp1-fp] < x < arr[fn1+fp]:
    #            fn,fn2=fn2-(fn<<2),fn #----------------------
                fp,fp2=fp2-(fp<<2),fp #----------------------
    #            flag=False
            elif x == arr[fp1-fp]:
                return fp1-fp
            elif x == arr[fn1+fp]:
                return fn1+fp

            elif x < arr[fp1-fp] :
                #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
    #            f1=(fp+fp2)>>1 #----------------------
                if arr[prv] <= x :
                    if  arr[prv] == x:
                        return prv
                    elif prv <= fp1-f1:
                        if x == arr[fp1-f1]:
                            return  fp1-f1
                        elif x < arr[fp1-f1]:
                            fp1,fn1=fp1-f1-1,prv+1
                        else :
                            fp1,fn1=fp1-fp-1,fp1-f1+1                    
                    else :
                        fp1,fn1=fp1-fp-1,prv+1              
                else:
    #                print("===1")
                    return -1

            elif x > arr[fn1+fp]:
    #            f1=(fp+fp2)>>1 #----------------------
                #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
                if x <= arr[prv1]:
                    if  arr[prv1] == x:
                        return prv1
                    elif prv1 >= fn1+f1:
                        if x == arr[fn1+f1]:
                            return  fn1+f1
                        elif x > arr[fn1+f1]:
                            fp1,fn1=prv1-1,fn1+f1+1                    
                        else :
                            fp1,fn1=fn1+f1-1,fn1+fp+1                    
                    else :
                        fp1,fn1=prv1-1,fn1+fp+1              
                else:
    #                print("===2")
                    return -1
            elif (fn1+fp) >= (fp1-fp) :
                #print("===3")
                return -1
            while ( fp > fp1-fn1):
    #            print("++______+++++++")
                fp,fp2=fp2-(fp<<2),fp #----------------------
    #        fn=((fp+fp2)>>1)-(fp<<1)   #----------------------
    #        fn2=(fp2+fp)>>1 #----------------------
            prv,prv1=fn1,fp1 # used for area of intrest

        else:
            if x == arr[fn1+fp+1]:
                return fn1+fp+1
            return -1


from timeit import default_timer as  timer
start= timer()
cc=[ kartik_strafe_s(arr,i,f11,gg,l) for i in arr] #----------------------
end= timer()
print(end-start)


print(sum([i-j for i,j in  zip(arr,cc)]))
cc2=[ i  for i in arr if kartik_strafe_s(arr,i,f11,gg,l)  == -1] #----------------------

cc3=[ i for i in cc2 if i > -1] #----------------------
[4, 7, 38, 41, 59, 62, 93, 96]
print(cc2[:10],len(cc2))
print(len(arr[:-2]))
print(kartik_strafe_s(arr,96,f11,gg,l))


    def kartik_strafe_s(arr,x,fp,fn,l): # arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None
        fn2=(fp<<1 )+fn #----------------------
        fp2=(fn2<<1 )-fp #----------------------
        prv,prv1=0,l
        fn1,fp1=0,l
        #print("_____+++__________+++")
        while(fp > 0 ):
            f1=(fp+fp2)>>1
            f2=f1-fp
            c1=fp1-fp
            c2=fn1+fp
            x1=arr[c1]
            x2=arr[c2]
            n1=arr[prv]
            n2=arr[prv1]
    #        ff1=arr[fp1-f1]
    #        ff2=arr[fp1-f2]
    #        ff3=arr[fn1+f1]
    #        ff4=arr[fn1+f2]
            #print("fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fp2:",fp2,"fp1-fp:",fp1-fp,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence p : ",fp2-fp)
            if x1 < x < x2:
                fp,fp2=fp2-(fp<<2),fp #----------------------
            elif x == x1:
                return c1
            elif x == x2:
                return c2

            elif x < x1 :
                #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 1  ",fp1-fn1)
                if n1 <= x :
                    if  n1 == x:
                        return prv
    #                elif prv >= fp1-f2:
    #                    return xx(arr,x,fp1-fn-1,prv+1,fp,fp2) # bw prv and fn `1
                    elif prv <= fp1-f1:
                        if x == ff1:
                            return  fp1-f1
                        elif x < ff1:
                            fp1,fn1=fp1-f1-1,prv+1
                        else :
                            fp1,fn1=c1-1,fp1-f1+1                    
                    else :
                        fp1,fn1=c1-1,prv+1              
                else:
                    #print("===1")
                    return -1

            elif x > x2:
                #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
                if x <= n2:
                    if  n2 == x:
                        return prv1
                    elif prv1 >= fn1+f1:
                        if x == ff3:
                            return  fn1+f1
                        elif x > ff3:
                            fp1,fn1=prv1-1,fn1+f1+1                    
                        else :
                            fp1,fn1=fn1+f1-1,c2+1                    
                    else :
                        fp1,fn1=prv1-1,c2+1              
                else:
                    #print("===2")
                    return -1
            elif (c2) >= (c1) :
                #print("===3")
                return -1
            while ( fp > fp1-fn1):
                #print("++______+++++++")
                fp,fp2=fp2-(fp<<2),fp #----------------------
            #fn=((fp+fp2)>>1)-(fp<<1)   #----------------------
            #fn2=(fp2+fp)>>1 #----------------------
            prv,prv1=fn1,fp1 # used for area of intrest

        else:
            if x == arr[fn1+fp+1]:
                return fn1+fp+1
            return -1



arr=[i for i in range(1,100000)]
arr=[ i+0.10 for i in arr ]

arr=[i for i in range(1,100000)]
arr=[i for i in range(-15,-1)] # min for arr len() = 14
arr=[i for i in range(1,10000000)]
arr=[i for i in range(1,40000000)]
arr=[i for i in range(9000000,10000000)]
arr=[i for i in range(1,7000000)]
arr=[i for i in range(700000,800000)]
print(len(arr))
print(arr)
l=len(arr)
f1=3
f11=13
f21=55
while (f21 < l):
    f1,f11,f21=f11,f21,(f21<<2)+f11  #----------------------
print(f1,f11,f21,((f11+f21)>>1)-(f11<<1))


l=l-1
gg=((f11+f21)>>1)-(f11<<1)


fn2=(f11<<1 )+gg
fp2=(fn2<<1 )-f11
def kartik_strafe_s(arr,x,fp2,fp,l): # arr,x,fp1=0,fn1=0,fa1=0,fa2=0,x1=None
    fn1,fp1=0,l
    #    c=0
    #print("_____+++__________+++")
    s=True
    while(fp > 0 ):
        
        f1=(fp+fp2)>>1
        c2=fn1+fp
    #        print(c2,fp,f1)
        x2=arr[c2]
        n2=arr[l]
        #print("fn:",fn,"fp:",fp,"fn1/prv:",fn1,"fp1/prv1:",fp1,"fp2:",fp2,"fp1-fp:",fp1-fp,"fn1+fp:",fn1+fp,"fp1-fn1:",fp1-fn1,"diffence p : ",fp2-fp)
        if x < x2:
            fp,fp2=fp2-(fp<<2),fp #----------------------
            s=False
        elif x == x2:
            return c2
        elif x > x2:
            #print("fn1/prv:",fn1,"fp1/prv1:",fp1,"diff 2  ",fp1-fn1)
            if x <= n2:
                if n2 == x:
                    return l
                elif l >= fn1+f1:
                    if x == arr[fn1+f1]:
                        return  fn1+f1
                    elif x > arr[fn1+f1]:
                        fp1,fn1=l-1,fn1+f1+1
                    else :
                        fp1,fn1=fn1+f1-1,c2+1
                else :
                    fp1,fn1=l-1,c2+1
                    s=True
            else:
                #print("===2")
                return -1
        elif (c2) >= (c1) :
            #print("===3")
            return -1
        l=fp1        
        if s:
            while ( fp > fp1-fn1):
                fp,fp2=fp2-(fp<<2),fp #----------------------


    else:
        if x == arr[fn1+fp+1]:
            return fn1+fp+1
        return -1


from timeit import default_timer as  timer
start= timer()
cc=[ kartik_strafe_s(arr,i,fp2,f11,l) for i in arr]
print(kartik_strafe_s(arr,1.10,fp2,f11,l))
print(kartik_strafe_s(arr,9000000.10,fp2,f11,l))
print(kartik_strafe_s(arr,9000000,fp2,f11,l))
end= timer()
print(end-start)


xx=[]
for i in arr:
    start= timer()
    kartik_strafe_s(arr,i,fp2,f11,l)
    fibMonaccianSearch(arr, i, l,fibM,fibMMm2,fibMMm1)
    end= timer()
    xx.append(end-start)
print(sum(xx)/l)    


cc=[ kartik_strafe_s(arr,i,fp2,f11,l) for i in arr] #----------------------
cc2=[ i  for i in arr if kartik_strafe_s(arr,i,fp2,f11,l)  == -1] #----------------------
print(cc2[:10],len(cc2))
print(sum([i-j for i,j in  zip(arr,cc)]))


print(cc)

print(kartik_strafe_s(arr,9000337,f11,gg,l))

