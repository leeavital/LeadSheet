# fout hihat quarter notes
import arezzo


def simpleHats():
   
   m = arezzo.Measure()
   
   m.addNote( arezzo.Note( 'A#2', 1, 4 ) )
   m.addNote( arezzo.Note( 'F#2', 2, 12 ) )
   m.addNote( arezzo.Note( 'F#2', 1, 12 ) )

   m.addNote( arezzo.Note( 'A#2', 1, 4 ) )
   m.addNote( arezzo.Note( 'F#2', 2, 12 ) )
   m.addNote( arezzo.Note( 'F#2', 1, 12 ) )

   return m
