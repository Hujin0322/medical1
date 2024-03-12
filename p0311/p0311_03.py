for i in range(1,10):
    #if i==2: break
    for j in range(1,10):
        if j==5:
            temp=1
            break
        print(f'{i}*{j}={i*j}')
    if temp==1: break