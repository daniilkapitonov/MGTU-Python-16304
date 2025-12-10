def sq(x):
    return x*x

def f_chet(x):
    return x%2!=0



sp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sp = list(filter(lambda x:x<10,sp))
print(sp)
sp = list(filter(f_chet,sp))
print(sp)
sp = list(map(sq,sp))
print(sp)