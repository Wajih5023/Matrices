from math import sqrt


# Represents a vector
class Vector ( object ):


  # Creates zero vector of given length
  # Input: integer representing size of vector
  def __init__ ( self , size = 2 ):
    self.vector = []

    count = 0
    while count < size:
      self.vector.append( 0 )
      
      count += 1

  
  # Creates nonzero vector using given list of entries
  # Input: list of integers with same length as self.vector
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
  # Input: integer representing entry to be added
  def addEntry ( self , entry ):
    self.vector.append( entry )


  # Changes existing entry in vector
  # Input: two integers representing position of entry to change and new entry
  def setEntry ( self , index , entry ):
    if not ( 0 < index <= self.getSize() ):
      print( "Out of Range" )

      return

    self.vector[index - 1] = entry

  
  # Returns entry at specified position as integer
  # Input: integer representing position of entry
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
  

  # Adds two vectors of same size together
  # Returns new vector
  # Input: second Vector object
  def __add__ ( self , other ):
    if self.getSize() != other.getSize():
      print( "Vectors cannot be added due to differing sizes" )

      return
  
    vec = Vector( self.getSize() )
    for i in range( 1 , self.getSize() + 1 ):
      vec.vector[i - 1] = self.getEntry( i ) + other.getEntry( i )

    return vec

  
  # Subtracts two vectors of same size
  # Returns new vector
  # Input: second Vector object
  def __sub__ ( self , other ):
    if self.getSize() != other.getSize():
      print( "Vectors cannot be subtracted due to differing sizes" )

      return
  
    vec = Vector( self.getSize() )
    for i in range( 1 , self.getSize() + 1 ):
      vec.vector[i - 1] = self.getEntry( i ) - other.getEntry( i )

    return vec


  # Checks whether two vectors are equal or not
  # Returns boolean
  # Input: second Vector object
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