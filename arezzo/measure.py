from voice import Voice


class Measure():
   
   def __init__( self ):
	  
	  # initialize defaults to one voice
	  self.voices = [ Voice() ]

	  self.beats = 4
	  self.divisions = 4


   def timeSignature( self ):
	  return (self.beats, self.divisions)



   def addRest( self, rest  ):
	  self.voices[0].addRest( rest )
	  return self

   def addNote( self, note ):

	  self.voices[0].addNote( note )
	  return self

   def addVoice( self, v ):
	  self.voices.append( v )
