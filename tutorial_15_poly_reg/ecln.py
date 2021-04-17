import numpy as np

def update_row(r2,r1):
    coeff = r2[0]/r1[0]
    r_temp = r2 - coeff*r1
    return(r_temp)

def update_sub_mat(mat):
    m_temp = []
    m_temp.append(mat[0])
    for i in range(1,np.shape(mat)[0]):
        m_temp.append(update_row(mat[i],mat[0]))
    return (np.asarray(m_temp) )

def calc_ecl(m):
    temp_mat = np.copy(m)
    for i in range(len(temp_mat)):
        temp_mat[i:,i:] = update_sub_mat(temp_mat[i:,i:])
    return(temp_mat)



'''


m2 = np.asarray([[2.0,3.0,-4.0],[1.0,5.0,-1.0]])
print(calc_ecl(m2),'\n')

m3 = np.asarray([[2.0,3.0,-4.0,12.0],[1.0,5.0,-1.0,12.0],[3.0,7.0,-3.0,20.0]])
print(calc_ecl(m3),'\n')

m4 = np.asarray([[1.0,3.0,-4.0,12.0,19],[1.0,5.0,-1.0,12.0,32],[3.0,7.0,-3.0,20.0,56],[1,2,3,4,5]])
print(calc_ecl(m4),'\n')

'''
#m = np.asarray([[2.0,3.0,-4.0],[1.0,5.0,-1.0],[3.0,7.0,-3.0]])
#print(calc_ecl(m))