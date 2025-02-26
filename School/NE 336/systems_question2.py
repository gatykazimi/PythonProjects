# Gaty Kazimi
# 20956021

from scipy.optimize import fsolve

def tempfunc (z):
    [tc, th, jc, jh]=z
    f = [(5.67e-8)*tc**4+17.41*tc-jc-5188.18,
         jc-0.71*jh+7.46*tc-2352.71,
         (5.67e-8)*th**4+1.865*th-jh-2250,
         jh-0.71*jc+7.46*jh-11093]
    
    return f

t_initial = 298#K
jc_initial = 3000#W/m^2
jh_initial = 5000#W/m^2

# a) fsolve method
print(fsolve(tempfunc,[t_initial,t_initial,jc_initial,jh_initial]))
# Result:
# [ 319.25868667  469.93693093  959.16616226 1391.72671102]

# b) Newton's method
tol = 1e-6

x, y = symbols('x y')
Jxy=.jacobian([x, y])
