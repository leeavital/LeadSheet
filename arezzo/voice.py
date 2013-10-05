class Voice():
	  

   def __init__( self ):
	  self.notesAndRests = []


   def addNote( self, note ):
	  self.notesAndRests.append( note )  
	  return self


   def addRest( self, rest ):
	  self.notesAndRests.append( rest )

   def addChord( self, chord ):
	  self.notesAndRests.append( chord ) 
   
