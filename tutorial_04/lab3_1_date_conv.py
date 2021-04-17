#convert to julian calender to gregorian and vice versa

def n_to_j(Y,M,D):
    if(M==1 or M==2):   
        M=M+12
        Y=Y-1

    A = int(Y/100)
    B = int(A/4)
    C = 2-A+B
    E = int(365.25*(Y+4716))
    F = int(30.6001*(M+1))
    JD= C+D+E+F-1524.5
    print(JD)

def j_to_n(JD):
    Q = JD+0.5
    Z = int(Q)
    W = int((Z - 1867216.25)/36524.25)
    X = int(W/4)
    A = Z+1+W-X
    B = A+1524
    C = int((B-122.1)/365.25)
    D = int(365.25*C)
    E = int((B-D)/30.6001)
    F = int(30.6001*E)

    print('day:', B-D-F+(Q-Z))
    if(E<=12):  E=E-1
    else:   E=E-13
    print('month:', E)
    if(E==1 or E==2): print('year:', C-4715 )
    else: print('year:', C-4716 )
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

val=input("give a date:")


if(is_number(val)): 
    print('JD')
    j_to_n(float(val))
else:
    values = val.split('/')
    if(len(values)!=3 or int(values[1])>12 or int(values[1])<1 or int(values[0])>31): print('invalid date')
    else:   n_to_j(int(values[2]),int(values[1]),int(values[0]))
    
