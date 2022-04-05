from vector import *

# Adds two vectors of same length together
# Returns new vector
def addVectors ( v1 , v2 ):
  if v1.getSize() != v2.getSize():
    print( "Vectors cannot be added due to differing sizes" )

    return
  
  vec = Vector( v1.getSize() )
  for i in range( v1.getSize() ):
    vec.vector[i] = v1.vector[i] + v2.vector[i]

  return vec
    