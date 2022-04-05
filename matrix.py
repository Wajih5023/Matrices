from vector import *


# Represents a matrix
class Matrix( object ):
  

  # Creates zero matrix from given number of entries and columns
  def __init__ ( self , m = 2 , n = 2 ):
    self.matrix = []

    for i in range( n ):
      self.matrix.append( Vector( m ) )
  

  # Creates nonzero matrix from given list of Vectors
  def createMatrix( self , vec_list ):
    if self.getNumOfColumns() != len( vec_list ):
      print( "Given list does not have same number of vectors as matrix" )

      return
    
    for i in range( 1 , self.getNumOfColumns() + 1 ):
      if self.getVector( i ).getSize() != vec_list[i - 1].getSize():
        print( "A vector in list does not have same length as corresponding vector in matrix" )

        return
    
    for i in range( self.getNumOfColumns() ):
      self.matrix[i] = vec_list[i]
  

  # Changes current matrix to zero matrix
  def reset( self ):
    m , n = self.getDimensions()
    self.__init__( m , n )

    
  # Returns entry at specified row and column as integer
  def getEntry ( self , m , n ):
    if m <= 0 or n <= 0 or m > self.getNumOfRows() or n > self.getNumOfColumns():
      print( "Out of Range" )

      return

    return self.getVector( n ).getEntry( m )


  # Returns list of entries in specified row as list
  def getRow ( self , row ):
    if row <= 0 or row > self.getNumOfRows():
      print( "Out of Range" )

      return
    
    entries = []
    for i in range( 1 , self.getNumOfColumns() + 1 ):
      entries.append( self.getEntry( row , i ) )
    
    return entries


  # Returns vector at specified position as Vector object
  def getVector ( self , column ):
    if column <= 0 or column > self.getNumOfColumns():
      print( "Out of Range" )
      
      return

    return self.matrix[column - 1]
  

  # Returns number of entries in each column as integer
  def getNumOfRows ( self ):
    return self.getVector( 1 ).getSize()


  # Returns number of column in matrix as integer
  def getNumOfColumns ( self ):
    return len( self.matrix )


  # Returns the dimensions of the matrix as two integers
  def getDimensions ( self ):
    return self.getNumOfRows() , self.getNumOfColumns()
  

  # Checks whether matrix is zero matrix or not
  # Returns boolean
  def isZeroMatrix ( self ):
    for vec in self.matrix:
      if not vec.isZeroVector():
        return False
    
    return True

  
  # Returns tranpose of matrix as Matrix object
  def transpose ( self ):
    m , n = self.getDimensions()
    mat = Matrix( n , m )

    for i in range( 1 , m + 1 ):
      num_list = self.getRow( i )
      new_vec = Vector( n )
      new_vec.createVector( num_list )

      mat.matrix[i - 1] = new_vec

    return mat


  # Adds two matrices of same dimensions together
  # Returns new matrix
  def __add__ ( self , other ):
    m1 , n1 = self.getDimensions()
    m2 , n2 = other.getDimensions()

    if m1 != m2 or n1 != n2:
      print( "Matrices cannot be added due to differing dimensions" )

      return
  
    mat = Matrix( m1 , n1 )
    for i in range( 1 , n1 + 1 ):
      mat.matrix[i - 1] = self.getVector( i ) + other.getVector( i )

    return mat

  
  # Subtracts two matrices of same dimensions
  # Returns new matrix
  def __sub__ ( self , other ):
    m1 , n1 = self.getDimensions()
    m2 , n2 = other.getDimensions()

    if m1 != m2 or n1 != n2:
      print( "Matrices cannot be subtracted due to differing dimensions" )

      return
  
    mat = Matrix( m1 , n1 )
    for i in range( 1 , n1 + 1 ):
      mat.matrix[i - 1] = self.getVector( i ) - other.getVector( i )

    return mat


  # Multiplies two matrices together
  # Returns new matrix
  def multiplyMatrix ( self , other ):
    m1 , n1 = self.getDimensions()
    m2 , n2 = other.getDimensions()

    if m1 != n2 or m2 != n1:
      print( "Matrices cannot be multiplied together" )

      return

    mat = Matrix( a.getNumOfRows() , b.getNumOfColumns() )
    m , n = mat.getDimensions()

    for row in range( 1 , m + 1 ):
      num_list = a.getRow( row )
      temp_row = Vector( len( num_list ) )
      temp_row.createVector( num_list )

      for col in range( 1 , n + 1 ):
        mat.matrix[col - 1].vector[row - 1] = dotProduct( temp_row , b.getVector( col ) )
  
    return mat

  
  # Checks whether two matrices are equal or not
  # Returns boolean
  def __eq__ ( self , other ):
    if self.getNumOfColumns() != other.getNumOfColumns():
      return False

    for i in range( 1 , self.getNumOfColumns() + 1 ):
      if self.getVector( i ) != other.getVector( i ):
        return False
    
    return True

  
  # Returns string form of matrix
  def __str__ ( self ):
    mat_str = ""

    for m in range( 1 , self.getNumOfRows() + 1 ):
      mat_str += "[ "

      for n in range( 1 , self.getNumOfColumns() + 1 ):
        mat_str += str( self.getEntry( m , n ) ) + " "

      mat_str += "]\n"

    return mat_str
      