from math import acos
from vector import *
from matrix import *


# Multiplies vector by scalar k
# Returns new vector
# Input: Vector object and integer representing factor to multiply by
def scalarMultiplyVector ( vec , k ):
  new_vec = Vector( vec.getSize() )

  for i in range( 1 , vec.getSize() + 1 ):
    new_vec.vector[i - 1] = k * vec.getEntry( i )
  
  return new_vec


# Divides vector by scalar k
# Returns new vector
# Input: Vector object and integer representing factor to divide by
def scalarDivideVector ( vec , k ):
  new_vec = Vector( vec.getSize() )

  for i in range( 1 , vec.getSize() + 1 ):
    if vec.getEntry( i ) % k != 0:
      print( "Vector cannot be divided by scalar k evenly" )

      return

    new_vec.vector[i - 1] = int( vec.getEntry( i ) / k )
  
  return new_vec


# Multiplies matrix by scalar k
# Returns new matrix
# Input: Matrix object and integer representing factor to multiply by
def scalarMultiplyMatrix ( mat , k ):
  m , n = mat.getDimensions()
  new_mat = Matrix( m , n )

  for i in range( 1 , n + 1 ):
    new_mat.matrix[i - 1] = scalarMultiplyVector( mat.getVector( i ) , k )
  
  return new_mat


# Divides matrix by scalar k
# Returns new matrix
# Input: Matrix object and integer representing factor to divide by
def scalarDivideMatrix ( mat , k ):
  m , n = mat.getDimensions()
  new_mat = Matrix( m , n )

  for i in range( 1 , n + 1 ):
    new_mat.matrix[i - 1] = scalarDivideVector( mat.getVector( i ) , k )

    if new_mat.matrix[i - 1] is None:
      print( "Matrix cannot be divided by scalar k evenly" )

      return
  
  return new_mat


# Multiplies two matrices together
# Returns new matrix
# Input: Two Matrix objects
def multiplyMatrix ( mat1 , mat2 ):
  m1 , n1 = mat1.getDimensions()
  m2 , n2 = mat2.getDimensions()

  if m1 != n2 or m2 != n1:
    print( "Matrices cannot be multiplied together" )

    return

  new_mat = Matrix( mat1.getNumOfRows() , mat2.getNumOfColumns() )
  m , n = new_mat.getDimensions()

  for row in range( 1 , m + 1 ):
    num_list = mat1.getRow( row )
    temp_row = Vector( len( num_list ) )
    temp_row.createVector( num_list )

    for col in range( 1 , n + 1 ):
      new_mat.matrix[col - 1].vector[row - 1] = dotProduct( temp_row , mat2.getVector( col ) )
  
  return new_mat

  
# Multiplies matrix and vector together
# Returns new vector
# Input: Matrix object and Vector object
def multiplyMatrixVector ( mat , vec ):
  m , n = mat.getDimensions()
  
  if n != vec.getSize():
    print( "Matrix cannot be multiplied with vector" )

    return
  
  new_vec = Vector( m )
  for i in range( 1 , new_vec.getSize() + 1 ):
    num_list = mat.getRow( i )
    tempRow = Vector( len( num_list ) )
    tempRow.createVector( num_list )

    new_vec.vector[i - 1] = dotProduct( tempRow , vec )
  
  return new_vec


# Finds dot product of two vectors
# Returns dot product as integer
# Input: two Vector objects of same size
def dotProduct ( vec1 , vec2 ):
  if vec1.getSize() != vec2.getSize():
    print( "Dot product cannot be calculated due to differing sizes" )

    return

  dot_product = 0
  for i in range( 1 , vec1.getSize() + 1 ):
    dot_product += vec1.getEntry( i ) * vec2.getEntry( i )
  
  return dot_product


# Finds distance between two vectors
# Returns the distance as float
# Input: two Vector objects of same size
def distance ( vec1 , vec2 ):
  difference = vec1 - vec2

  return difference.length()


# Finds angle between two non-zero vectors
# Returns the angle as float
# Input: two Vector objects of same size
def angle ( vec1 , vec2 ):
  dot_product = dotProduct( vec1 , vec2 ) / ( vec1.length() * vec2.length() )

  return acos( dot_product )


# Checks whether two vectors are orhogonal or not
# Returns boolean
# Input: two Vector objects of same size
def areOrthogonal ( vec1 , vec2 ):
  return dotProduct( vec1 , vec2 ) == 0

  
     