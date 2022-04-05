# Represents vector
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
      self.vector[i] = list[i]

  # Adds new entry to vector
  def addEntry ( self , entry ):
    self.vector.append( entry )
  
  # Returns number of entries in vector
  def getSize ( self ):
    return len( self.vector )
  
  # Checks whether vector is zero vector or not
  # Returns boolean
  def isZeroVector( self ):
    for entry in self.vector:
      if entry != 0:
        return False
    
    return True

  # Returns string form of vector
  def __str__ ( self ):
    vec = "[ "

    for i in range( len( self.vector ) ):
      vec += str( self.vector[i] )

      if i != len( self.vector ) - 1:
        vec += " , "
    
    vec += "]"
    
    return vec