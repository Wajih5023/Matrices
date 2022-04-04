class Vector ( object ):
  def __init__ ( self , size = 2 ):
    self.vector = []
    self.num_of_entries = size

    count = 0
    while count < self.num_of_entries:
      self.vector.append( 0 )
      
      count += 1
  
  def __str__ ( self ):
    vec = ""

    for entry in self.vector:
      vec += "[ " + str( entry ) + " ]\n"
    
    return vec