
for i in range(1,100):
    o=1
    m=0
    while o<=i:
        if i % o == 0:
            m=m+1
    
        o=o+1 
    if m == 2:
        print(i)