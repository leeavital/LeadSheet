midiByLetter = {}
midiByLetter['C'] = 261.63
midiByLetter['C#'] = midiByLetter['Db'] = 277.18
midiByLetter['D'] = 293.66
midiByLetter['D#'] = midiByLetter['Eb'] =  311.13
midiByLetter['E'] = midiByLetter['Fb'] = 329.63
midiByLetter['E#'] = midiByLetter['F'] =   349.23
midiByLetter['Gb'] = midiByLetter['F#'] = 369.99
midiByLetter['G'] = 392.00
midiByLetter['G#'] = midiByLetter['Ab'] = 415.30
midiByLetter['A'] = 440
midiByLetter['A#'] = midiByLetter['Bb'] =  466.16
midiByLetter['B'] = 493.88


class Note:
   
   def __init__( self, value, noteCount, countType ):
	  self.letter, self.octave = value[0:len(value) - 1].upper(), int(value[-1])
	  self.time = ( noteCount, countType )

   def hertz( self ):
	  
	  factor = 2 ** ( self.octave - 4 )
	  return factor * midiByLetter[ self.letter ]

	  
	  return 440






if __name__ == "__main__":
   
   # test unpacking of 
   
    
   # test "hertz"
   n1 = Note( 'A4', 4, 4 )
   assert( n1.letter == 'A' )
   assert( n1.octave == 4 )
   assert( n1.hertz() == 440 )


   n2 = Note( 'a5', 4, 4 )
   assert( n2.letter == 'A' )
   assert( n2.octave == 5 )
   assert( n2.hertz() == 880 )

