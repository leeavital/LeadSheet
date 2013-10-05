import arezzo
import arezzo.instruments as a_instruments

from writer import writeMidi

from midiutil.MidiFile import MIDIFile


class Context:
   """holds tempo"""   
   def __init__( self, tempo  ):
	  self.tempo = tempo
	  self.track = 0



leadsheet = []
leadsheet.append( ('em', 4) )
leadsheet.append( ('am', 4) )
leadsheet.append( ('dm', 4) )
leadsheet.append( ('g', 4) )
leadsheet.append( ('c', 4) )




context = Context( 120 )


theFile = MIDIFile( 2 )
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



bassStaff = arezzo.Staff( a_instruments.FRETLESS_BASS )
bassStaff.addMeasure( m1 )
bassStaff.addMeasure( m0 )
bassStaff.addMeasure( m2 )

violinStaff = arezzo.Staff( a_instruments.VIOLIN )
violinStaff.addMeasure( m0 )
violinStaff.addMeasure( m2 )
violinStaff.addMeasure( m1 )

score = arezzo.Score( )
score.addStaff( bassStaff )
score.addStaff( violinStaff )


writeMidi( score , context, 0, theFile )

binfile = open("output.mid", "wb")
theFile.writeFile( binfile )
binfile.close()
