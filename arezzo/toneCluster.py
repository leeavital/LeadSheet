import arezzo

class ToneCluster:
   
   def __init__( self, notes, noteCount, countType ):
	  """notes: [ arezzo.Note ]
		 noteCount: see Note
		 countType: see Note

		 Even though this takes a list of notes, it 
		 throws the time value of each individual note away
	  """
	  self.notes = notes
	  self.time = (noteCount, countType )

   def around( self, note ):
	  """centers a tone cluster around a given note, 
		 useful for figuring out the most natural sounding
		 inversion

		 WARNING: right now this only shifts individual notes DOWN
		 the workaround is to first raise the chord up an octave and THEN
		 do the lowering"""
	  
	  newNotes = []
	  center = note.midicode()
	   
	  for n in self.notes: 
		 
		 # center = 50 
		 # outer = 70 -> 58 -> 46
		 outer = n.midicode()
		 while abs(outer - center) > abs(outer - center - 12):
			n = n.eightVB()
			outer = n.midicode()
		 
		 
		 newNotes.append( n )

	  return ToneCluster( newNotes, self.time[0], self.time[1] )

	  

			   


   
   def copy( self ):
	  
	  ns = [n.copy() in self.notes]
	  return ToneCluster( ns, self.time[0], self.time[1] )

	      
