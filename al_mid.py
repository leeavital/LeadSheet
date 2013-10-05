import arezzo


from writer import writeMidi

from midiutil.MidiFile import MIDIFile


class Context:
   """holds tempo"""   
   def __init__( self, tempo  ):
	  self.tempo = tempo






context = Context( 120 )


theFile = MIDIFile( 1 )
theFile.addTrackName( 0, 0, "Sample Track" )
theFile.addTempo( 0, 0, context.tempo )


   
    



TEMPO = 60


m0 = arezzo.Measure()
m0.addNote( arezzo.Rest(1, 1 ) )

m1 = arezzo.Measure()
m1.addNote( arezzo.Note( 'E3', 1, 4 ) )
m1.addNote( arezzo.Note( 'E#3', 1, 4 ) )
m1.addNote( arezzo.Note( 'G3', 1, 4 ) )
m1.addNote( arezzo.Note( 'A3', 1, 4 ) )

m2 = arezzo.Measure()
m2.addNote( arezzo.Note( 'A3', 1, 1 ) )


bassStaff = arezzo.Staff( )
bassStaff.addMeasure( m0 )
bassStaff.addMeasure( m1 )
bassStaff.addMeasure( m2 )

score = arezzo.Score( )
score.addStaff( bassStaff )



writeMidi( score , context, 0, theFile )

binfile = open("output.mid", "wb")
theFile.writeFile( binfile )
binfile.close()
