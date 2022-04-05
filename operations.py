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

# Subtracts two vectors of same length
# Returns new vector
def subtractVectors ( v1 , v2 ):
  if v1.getSize() != v2.getSize():
    print( "Vectors cannot be subtracted due to differing sizes" )

    return
  
  vec = Vector( v1.getSize() )
  for i in range( v1.getSize() ):
    vec.vector[i] = v1.vector[i] - v2.vector[i]

  return vec

# Multiplies vector by scalar k
# Returns new vector
def multiplyVector ( v , k ):
  vec = Vector( v.getSize() )

  for i in range( v.getSize() ):
    vec.vector[i] = k * v.vector[i]
  
  return vec
     