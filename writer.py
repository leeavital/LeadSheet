"""this module defines the write midi function"""


import arezzo

def writeMidi( musicEntity, context, timeOffset, midiFile ):
   
   # print "writeMidi with %s at %f" % ( musicEntity, timeOffset )
   
      
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
	  length = ((musicEntity.time[0] * 1.0) / musicEntity.time[1])  * 4 # everything is in FOUR
	  
	   
	  # the magic! 
	  print "adding a note at %f beats  for %f beats  at midicode %d" % (timeOffset, length, musicEntity.midicode() )
	  midiFile.addNote( 0, 10, musicEntity.midicode(), timeOffset, length, 100 )  

   
	  return timeOffset + length

   elif isinstance( musicEntity, arezzo.Rest ):
	  length = ((musicEntity.time[0] * 1.0) / musicEntity.time[1])  * 4  # everything is in FOUR
	  
	  return timeOffset + length

	      
   else:
	  print "OH SHIT WHAT IS IT?"
	  return timeOffset

   # yeah! recursive descent bitch!
