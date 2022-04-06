# Personally used to test the other files in Matrices

from vector import *
from matrix import *
from operations import *

v1 = Vector( 3 )
v1.createVector( [2 , 6 , 7] )
#print( v1 )
v2 = Vector( 3 )
v2.createVector( [4 , 5 , 9] )
#print( v2 )
v3 = Vector( 3 )
v3.createVector( [3 , 3 , 6] )
#print( v3 )
v4 = Vector( 3 )
v4.createVector( [1 , 2 , 3] )
#print( v4 )


mat = Matrix( 3 , 2 )
mat.createMatrix( [v1 , v2] )
print( mat )
mat2 = Matrix( 3 , 3 )
mat2.createMatrix( [v2 , v4 , v3] )
print( mat2 )

print( mat - mat2 )
print( mat2 - mat )