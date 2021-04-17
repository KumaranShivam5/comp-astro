




def dot(v1,v2):
    return(sum([e1*e2 for e1,e2 in zip(v1,v2)]))

def m_multiply(m1,m2):
        m_final = []
        for i in range (len(m1)):
            temp_vec = []
            for j in range (len(m1)):
                temp_vec.append(dot(m1[i,:],m2[:,j]))
            m_final.append(temp_vec)
        return(m_final)




import numpy as np
m1 = np.asarray([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.asarray([[10,20,30],[40,50,60],[70,80,90]])

m3 = np.asarray([[1,2,3],[4,5,6]])
m4 = np.asarray([[10,20],[40,50],[70,80]])

#m1 = [[1,2,3],[4,5,6],[7,8,9]]
#m2 = [[10,20,30],[40,50,60],[70,80,90]]



m_ans = m_multiply(m3,m4)
print(m_ans)

print(np.matmul(m3,m4))

#print(m_final)


