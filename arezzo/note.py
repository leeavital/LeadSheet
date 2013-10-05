midiByLetter = {}
midiByLetter['C'] = 60 
midiByLetter['C#'] = midiByLetter['DB'] = 61 
midiByLetter['D'] = 62
midiByLetter['D#'] = midiByLetter['EB'] =  63
midiByLetter['E'] = midiByLetter['FB'] = 64
midiByLetter['E#'] = midiByLetter['F'] =   65
midiByLetter['GB'] = midiByLetter['F#'] = 66
midiByLetter['G'] = 67
midiByLetter['G#'] = midiByLetter['AB'] = 68
midiByLetter['A'] = 69
midiByLetter['A#'] = midiByLetter['BB'] =  70
midiByLetter['B'] = 71

lettersByMidi = {}
for letter, mid in midiByLetter.iteritems():
   lettersByMidi[ mid ] = letter

print lettersByMidi


class Note:
   
   def __init__( self, value, noteCount, countType ):
	  """value: comes in as A4
		 noteCount: how many of the countType
		 countType: what denomination of beat

		 possible combinations of countType and noteCount are 1,1 (whole note)
		 1,4 (quarter note), 1,3(half note in a triplet tuple)
	  """
	  self.letter, self.octave = value[0:len(value) - 1].upper(), int(value[-1])
	  self.time = ( noteCount, countType )

   # deprecated
   def hertz( self ):
	  raise Exception("deprecated") 
	  factor = 2 ** ( self.octave - 4 )
	  return factor * midiByLetter[ self.letter ]

   def midicode( self ):
	  r = midiByLetter[ self.letter ] + (12 * (self.octave - 4))
	  return r
   
   
   
   def interval( self, inter ): 
	  c = self.copy()
	  mid = c.midicode()
	  mid = mid + inter # half steps up	  
	  
	  # ensure between 60 and 71
	  mid = (mid % 12) + 60


	  c.letter = lettersByMidi[ mid ]

	  # we may need to adjust new octave assignments
	  if inter > 0 and self.midicode() > c.midicode():
		 c.octave = c.octave + 1
	  
	  return c

	  


   def fifth( self ):
	  return self.interval( 7 )	  

   def copy( self ):
	  return Note( self.letter + str(self.octave), self.time[0], self.time[1])
	   






if __name__ == "__main__":
   
   # tests...
    
   # test unpacking of 
   n1 = Note( 'A4', 4, 4 )
   assert( n1.letter == 'A' )
   assert( n1.octave == 4 )
   assert( n1.midicode() == 69 )


   n2 = Note( 'a5', 4, 4 )
   assert( n2.letter == 'A' )
   assert( n2.octave == 5 )
   assert( n2.midicode() == 81 )


   n2 = Note( 'a6', 4, 4 )
   assert( n2.letter == 'A' )
   assert( n2.octave == 6 )
   assert( n2.midicode() == 93 )

   
   n2 = Note( 'c#3', 4, 4 )
   assert( n2.letter == 'C#' )
   assert( n2.octave == 3 )


   n2 = Note( 'cb3', 4, 4 )
   assert( n2.letter == 'CB' )
   assert( n2.octave == 3 )

   n2 = Note( 'c2', 4, 4 )
   assert( n2.letter == 'C' )
   assert( n2.octave == 2 )
   assert( n2.midicode() == 36 )

   n3 = n2.fifth()
   assert( n3.letter == "G" )
   
   n3 = n2.interval( 6 ) # dimished fifth
   assert( n3.letter == "GB" or n3.letter == "F#" )

   

