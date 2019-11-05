def power_set(k):
    if k == N:
        print(a)
    else:
        a[k]=1; power_set(k+1)
        a[k]=0; power_set(k+1)