def orderedsequentialSearch(alist,item):
    pos=0
    found=False
    stop=False
    while pos < len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos=pos+1
    return found

a=[1,2,4,12,3,6,24]
print(orderedsequentialSearch(a,5))