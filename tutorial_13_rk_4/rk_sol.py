def f_te(x, te , tp , m_dot):
    n = nx(m_dot,x)
    g = gamma(n , tp , te)
    l = lmd(n,te)
    term1 = ((4*np.pi*mp*rg**3)/(3*kb*m_dot))*g*(x**2)
    term2 = te*((3*x-4)/(3*x*(x-1)))
    #print(term1 , term2)
    val = -term2 -term1
    return val
    
def f_tp(x, te , tp , m_dot):
    n = nx(m_dot,x)
    g = gamma(n , tp , te)
    l = lmd(n,te)
    term1 = ((4*np.pi*mp*rg**3)/(3*kb*m_dot))*g*(x**2)
    term2 = te*((3*x-4)/(3*x*(x-1)))
    #print(term1 , term2)
    val = -term2 -term1
    return val