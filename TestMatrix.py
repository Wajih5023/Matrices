from vector import *
from operations import *

v1 = Vector( 3 )
v1.createVector( [2 , 4 , 7] )
v2 = Vector( 3 )
v2.createVector( [4 , 5 , 9] )

print( angle( v1 , v2 ) )