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
  def isZeroMatrix( self ):
    for vec in self.matrix:
      if not vec.isZeroVector():
        return False
    
    return True

  
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
      