
def dot(v1,v2):
    return(sum([e1*e2 for e1,e2 in zip(v1,v2)]))

def m_multiply(m1,m2):
    m1 = np.asarray(m1)
    m2 = np.asarray(m2)
    i = m1.shape[0]
    j1 = m1.shape[1]
    j2 = m2.shape[0]
    k = m2.shape[1]
    if(j1==j2):
        m_final = np.zeros((i,k))
        for i_itr in range(i):
            for k_itr in range(k):
                v1 = m1[i_itr,:]
                v2 = m2[:,k_itr]
                m_final[i_itr][k_itr] = dot(v1,v2)
        return m_final
    else :
        raise ValueError('dim invalid')

import numpy as np
'''
m1 = np.asarray([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.asarray([[10,20,30],[40,50,60],[70,80,90]])

m3 = np.asarray([[1,2,3],[4,5,6]])
m4 = np.asarray([[10,20],[40,50],[70,80]])

#m1 = [[1,2,3],[4,5,6],[7,8,9]]
#m2 = [[10,20,30],[40,50,60],[70,80,90]]


m_ans = m_multiply(m3,m4)
print(m_ans)

print(np.matmul(m3,m4))

m5 = np.asarray([[1,2],[3,4],[5,6]])
m6 = np.asarray([2,3])
m7 = np.asarray([ [2,3]])
m6 = np.reshape(m6 , (len(m6),1))
m_ans = m_multiply_v2(m5,m6)
print(m_ans)

print(np.matmul(m5,m6))

import numpy as np
m3 = np.asarray([[1,2],[4,5],[1,4]])
#print(m3.T.shape)
m4 = np.asarray([1,2,3])
m4 = np.reshape(m4,(len(m4),1))
#print(m4.shape)
m_ans = m_multiply(m3.T,m4)
print(m_ans)


'''