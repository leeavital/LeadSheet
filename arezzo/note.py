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


class Note:
   
   def __init__( self, value, noteCount, countType ):
	  """value: comes in as A4"""
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






if __name__ == "__main__":
   
   # test unpacking of 
   
    
   # test "hertz"
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

