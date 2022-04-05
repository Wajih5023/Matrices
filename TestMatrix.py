from vector import *
from operations import *

v1 = Vector( 3 )
v1.createVector( [1 , 3 , 5] )
print( v1 )

v2 = Vector( 3 )
v2.createVector( [2 , 4 , 7] )
print( v2 )

print( multiplyVector( v1 , 3 ) )

