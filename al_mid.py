import arezzo



from midiutil.MidiFile import MIDIFile


class Context:
   """holds tempo"""   
   def __init__( self, tempo  ):
	  self.tempo = tempo






context = Context( 120 )


theFile = MIDIFile( 1 )
theFile.addTrackName( 0, 0, "Sample Track" )
theFile.addTempo( 0, 0, context.tempo )


def writeMidi( musicEntity, context, timeOffset, midiFile ):
   print "writeMidi with %s at %f" % ( musicEntity, timeOffset )
   
      
   if isinstance( musicEntity, arezzo.Score ):
	  
	  print "It was a score!"	  
	  for staff in musicEntity.staves:
		 # time offset is always the same
		 writeMidi( staff, context, timeOffset, midiFile )

	  return timeOffset
   
   elif isinstance( musicEntity, arezzo.Staff ):
	  
	  print "it was a Staff!"
	 
	  # too lazy for whatever functional bullshit I should be doing instead 
	  offset = timeOffset
	  for measure in musicEntity.measures:
		 offset = writeMidi( measure, context, offset, midiFile ) 

	  return offset

   elif isinstance( musicEntity, arezzo.Measure ):
	  
	  print "it's a measure"
	  
	  offset = timeOffset  ## janks, assumes every voice 
						   ## takes the same amount of time
	  for voice in musicEntity.voices:
		 offset = writeMidi( voice, context, timeOffset, midiFile )

	  return offset


   elif isinstance( musicEntity, arezzo.Voice ):
	  print "it's a voice"
	  
	  offset = timeOffset
	  for token in musicEntity.notesAndRests:
		 offset = writeMidi( token, context, offset, midiFile )
		 print "wrote a token at: ", offset

	  return offset

   elif isinstance( musicEntity, arezzo.Note ): 
	  timeDen, timeNum = musicEntity.time 
	  secondsPerBeat = (1 / (context.tempo / 60.0)) 
	  length = ((timeDen / timeNum) * secondsPerBeat) * 4 
	  
	   
	  # the magic! 
	  print "adding a note at %f for %f  seconds at %f hz" % (timeOffset, length, musicEntity.hertz() )
	  midiFile.addNote( 0, 10, musicEntity.hertz(), timeOffset, length, 100 )  

   
	  return timeOffset + length

	      
   else:
	  print "OH SHIT WHAT IS IT?"
	  return timeOffset

   # yeah! recursive descent bitch!
   
    



TEMPO = 60

m1 = arezzo.Measure()
m1.addNote( arezzo.Note( 'E3', 1, 1 ) )


m2 = arezzo.Measure()
m2.addNote( arezzo.Note( 'A3', 1, 1 ) )


bassStaff = arezzo.Staff( )
bassStaff.addMeasure( m1 )
bassStaff.addMeasure( m2 )

score = arezzo.Score( )
score.addStaff( bassStaff )



writeMidi( score , context, 0, theFile )

binfile = open("output.mid", "wb")
theFile.writeFile( binfile )
binfile.close()
