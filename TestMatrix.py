from vector import *
from operations import *

v1 = Vector( 3 )
v1.createVector( [2 , 4 , 7] )
print( v1 )

v2 = Vector( 3 )
v2.createVector( [2 , 4 , 7] )
print( v2 )

print( dotProduct( v1 , v2 ) )
print( areOrthogonal( v1 , v2 ) )
