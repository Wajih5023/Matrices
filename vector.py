from math import sqrt


# Represents a vector
class Vector ( object ):


  # Creates zero vector of given length
  def __init__ ( self , size = 2 ):
    self.vector = []

    count = 0
    while count < size:
      self.vector.append( 0 )
      
      count += 1

  
  # Creates nonzero vector using given list of entries
  def createVector ( self , list ):
    if self.getSize() != len( list ):
      print( "Given list does not have same length as vector" )

      return
    
    for i in range( len( self.vector ) ):
      self.vector[i] = int( list[i] )

  
  # Changes current vector into zero vector
  def reset ( self ):
    self.__init__( self.getSize() )


  # Adds new entry to vector
  def addEntry ( self , entry ):
    self.vector.append( entry )

  
  # Returns entry at specified position as integer
  def getEntry ( self , index ):
    if index <= 0 or index > self.getSize():
      print( "Out of Range" )
      
      return

    return self.vector[index - 1]
    

  # Returns number of entries in vector
  def getSize ( self ):
    return len( self.vector )

  
  # Checks whether vector is zero vector or not
  # Returns boolean
  def isZeroVector ( self ):
    for entry in self.vector:
      if entry != 0:
        return False
    
    return True

  
  # Finds the length of a vector
  # Returns the length as float
  def length ( self ):
    dot_product = 0

    for entry in self.vector:
      dot_product += entry ** 2

    return sqrt( dot_product )


  # Checks whether two vectors are equal or not
  # Returns boolean
  def __eq__ ( self , other ):
    if self.getSize() != other.getSize():
      return False

    for i in range( 1 , self.getSize() + 1 ):
      if self.getEntry( i ) != other.getEntry( i ):
        return False
    
    return True

      
  # Returns string form of vector
  def __str__ ( self ):
    vec_str = ""

    for entry in self.vector:
      vec_str += "[ " + str( entry ) + " ]\n"
    
    return vec_str