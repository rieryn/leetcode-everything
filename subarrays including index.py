def f(arr, k):
    pref = {0:1,1:0}
    cnt = 0
    incl = 0
    for i in range(0, len(arr)):
        if arr[i] == k:
            incl = 1
        if incl>0:
            cnt+= pref[incl-1]
        pref[incl] += 1
        print (pref)
    return cnt