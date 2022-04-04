# Represents vector
class Vector ( object ):

  # Creates zero vector of given length
  def __init__ ( self , size = 2 ):
    self.vector = []

    count = 0
    while count < self.num_of_entries:
      self.vector.append( 0 )
      
      count += 1
  
  # Creates nonzero vector using given list of entries
  def createVector ( self , list ):
    if self.getSize() != len( list ):
      print( "Given list cannot be used to create vector" )

      return
    
    for index in range( self.vector ):
      self.vector[index] = list[index]
  
  # Returns number of entries in vector
  def getSize ( self ):
    return len( self.vector )
  
  # Checks whether vector is zero vector or not
  def isZeroVector( self ):
    for entry in self.vector:
      if entry != 0:
        return False
    
    return True

  # Prints out vector 
  def __str__ ( self ):
    vec = ""

    for entry in self.vector:
      vec += "[ " + str( entry ) + " ]\n"
    
    return vec