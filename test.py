from vector import Vector
from matrix import Matrix

r2 = 2 ** 0.5
r6 = 6 ** 0.5
s1 = r6 - r2
s2 = r6 + r2
pi = 22/7

rM_FERME_TA_GUEULE_ALEXANDRE = Matrix.rotation3( -pi/12, Vector( [ 0, 1, 0 ] ) ).round( 3 )
print( rM_FERME_TA_GUEULE_ALEXANDRE * Vector( [ s2/4, 0 , s1/4 ] ) )