from math import acos
from matrix import *
from vector import *


# Adds two vectors of same size together
# Returns new vector
def addVectors ( u , v ):
  if u.getSize() != v.getSize():
    print( "Vectors cannot be added due to differing sizes" )

    return
  
  vec = Vector( u.getSize() )
  for i in range( 1 , u.getSize() + 1 ):
    vec.vector[i - 1] = u.getEntry( i ) + v.getEntry( i )

  return vec


# Subtracts two vectors of same size
# Returns new vector
def subtractVectors ( u , v ):
  if u.getSize() != v.getSize():
    print( "Vectors cannot be subtracted due to differing sizes" )

    return
  
  vec = Vector( u.getSize() )
  for i in range( 1 , u.getSize() + 1 ):
    vec.vector[i - 1] = u.getEntry( i ) - v.getEntry( i )

  return vec


# Multiplies vector by scalar k
# Returns new vector
def scalarMultiplyVector ( v , k ):
  vec = Vector( v.getSize() )

  for i in range( 1 , v.getSize() + 1 ):
    vec.vector[i - 1] = k * v.getEntry( i )
  
  return vec


# Adds two matrices of same dimensions together
# Returns new matrix
def addMatrices ( a , b ):
  m1 , n1 = a.getDimensions()
  m2 , n2 = a.getDimensions()

  if m1 != m2 or n1 != n2:
    print( "Matrices cannot be added due to differing dimensions" )

    return
  
  mat = Matrix( m1 , n1 )
  for i in range( 1 , n1 + 1 ):
    mat.matrix[i - 1] = addVectors( a.getVector( i ) , b.getVector( i ) )

  return mat


# Subtracts two matrices of same dimensions
# Returns new matrix
def subtractMatrices ( a , b ):
  m1 , n1 = a.getDimensions()
  m2 , n2 = a.getDimensions()

  if m1 != m2 or n1 != n2:
    print( "Matrices cannot be added due to differing dimensions" )

    return
  
  mat = Matrix( m1 , n1 )
  for i in range( 1 , n1 + 1 ):
    mat.matrix[i - 1] = subtractVectors( a.getVector( i ) , b.getVector( i ) )

  return mat


# Multiplies matrix by scalar k
# Returns new matrix
def scalarMultiplyMatrix ( a , k ):
  m , n = a.getDimensions()
  mat = Matrix( m , n )

  for i in range( 1 , n + 1 ):
    mat.matrix[i - 1] = scalarMultiplyVector( a.getVector( i ) , k )
  
  return mat


# Finds dot product of two vectors
# Returns dot product as integer
def dotProduct ( u , v ):
  if u.getSize() != v.getSize():
    print( "Dot product cannot be calculated due to differing sizes" )

    return

  dot_product = 0
  for i in range( 1 , u.getSize() + 1 ):
    dot_product += u.getEntry( i ) * v.getEntry( i )
  
  return dot_product


# Finds distance between two vectors
# Returns the distance as float
def distance ( u , v ):
  u_minus_v = subtractVectors( u , v )

  return u_minus_v.length()


# Finds angle between two non-zero vectors
# Returns the angle as float
def angle ( u , v ):
  dot_product = dotProduct( u , v ) / ( u.length() * v.length() )

  return acos( dot_product )


# Checks whether two vectors are orhogonal or not
# Returns boolean
def areOrthogonal ( u , v ):
  return dotProduct( u , v ) == 0

  
     