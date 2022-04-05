from vector import *

# Adds two vectors of same length together
# Returns new vector
def addVectors ( u , v ):
  if u.getSize() != v.getSize():
    print( "Vectors cannot be added due to differing sizes" )

    return
  
  vec = Vector( u.getSize() )
  for i in range( u.getSize() ):
    vec.vector[i] = u.vector[i] + v.vector[i]

  return vec

# Subtracts two vectors of same length
# Returns new vector
def subtractVectors ( u , v ):
  if u.getSize() != v.getSize():
    print( "Vectors cannot be subtracted due to differing sizes" )

    return
  
  vec = Vector( u.getSize() )
  for i in range( u.getSize() ):
    vec.vector[i] = u.vector[i] - v.vector[i]

  return vec

# Multiplies vector by scalar k
# Returns new vector
def multiplyVector ( v , k ):
  vec = Vector( v.getSize() )

  for i in range( v.getSize() ):
    vec.vector[i] = k * v.vector[i]
  
  return vec

# Finds dot product of two vectors
# Returns dot product as integer
def dotProduct( u , v ):
  if u.getSize() != v.getSize():
    print( "Dot product cannot be calculated due to differing sizes" )

    return

  dot_product = 0
  for i in range( u.getSize() ):
    dot_product += u.vector[i] * v.vector[i]
  
  return dot_product

  
     