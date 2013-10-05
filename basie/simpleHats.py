# fout hihat quarter notes
import arezzo


# Drum to Note values (for reference only, this should be in an enum)
# A#2 -- open high hat
# F#2 -- closed high hat
# B1 -- Acoustic Bass drum
# C1 -- Bass drup
# E2 --snare drum 2


def simpleHats():
   
   m = arezzo.Measure()
   
   
   v = arezzo.Voice( )  
   v.addNote( arezzo.Note( 'A#2', 1, 4) )  
   v.addNote( arezzo.Note( 'F#2', 2, 12) )
   v.addNote( arezzo.Note( 'F#2', 1, 12 ) )

   v.addNote( arezzo.Note( 'A#2', 1, 4 ) )
   v.addNote( arezzo.Note( 'F#2', 2, 12 ) )
   v.addNote( arezzo.Note( 'F#2', 1, 12 ) )	 

   m.addVoice( v )
   
   # bass drum
   v = arezzo.Voice()
   v.addNote( arezzo.Note( 'B1', 8, 12)  )
   v.addNote( arezzo.Note( 'B1', 3, 12 )  )
   v.addNote( arezzo.Note( 'B1', 1, 12 )  )

   m.addVoice( v )

   
   # # bass drum
   # v = arezzo.Voice()
   # v.addNote( arezzo.Note( 'C2', 8, 12)  )
   # v.addNote( arezzo.Note( 'C2', 3, 12)  )
   # v.addNote( arezzo.Note( 'C2', 1, 12)  )

   m.addVoice( v )



   return m
