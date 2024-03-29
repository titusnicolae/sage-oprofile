# This file was *autogenerated* from the file batch/r08.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_10 = Integer(10); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4)
def right(f,a,b,n):
   Deltax = (b-a)/n; c=a; est=_sage_const_0 
   for i in range(n):
       c += Deltax
       est += f(c)
   return est*Deltax

var('x')
__time__=misc.cputime(); __wall__=misc.walltime(); v = right(x**_sage_const_2 ,_sage_const_0 ,_sage_const_5 ,_sage_const_10 **_sage_const_4 ); print "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
