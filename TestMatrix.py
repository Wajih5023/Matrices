from vector import *
from matrix import *
from operations import *

v1 = Vector( 3 )
v1.createVector( [2 , 6 , 7] )
print( v1 )
v2 = Vector( 3 )
v2.createVector( [4 , 5 , 9] )
print( v2 )
v3 = Vector( 3 )
v3.createVector( [3 , 3 , 6] )
print( v3 )


print( mat )
print( mat.getEntry( 3 , 3 ) )