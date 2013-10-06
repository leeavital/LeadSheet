import arezzo
import arezzo.instruments as a_instruments

from writer import writeMidi

from midiutil.MidiFile import MIDIFile

import re

import basie


class Context:
   """holds tempo"""   
   def __init__( self, tempo  ):
	  self.tempo = tempo
	  self.track = 0



leadsheet = []
# leadsheet.append( ('em', 4) )
leadsheet.append( ('am', 4) )
leadsheet.append( ('d', 4) )
leadsheet.append( ('g', 4) )
leadsheet.append( ('c', 4) )
leadsheet.append( ('F#dim', 4) )
leadsheet.append( ('B', 4) )
leadsheet.append( ('em', 4) )
leadsheet.append( ('em', 4) ) # this should actually be a rest
leadsheet.append( ('am', 4) )
leadsheet.append( ('d', 4) )
leadsheet.append( ('g', 4) )
leadsheet.append( ('c', 4) )
leadsheet.append( ('F#dim', 4) )






context = Context( 200 )


theFile = MIDIFile( 16 )
# theFile.addTrackName( 0, 0, "Sample Track" )
theFile.addTempo( 0, 0, context.tempo )


TEMPO = 120

score = arezzo.Score()

   

# go through the chords
bassStaff = arezzo.Staff( arezzo.instruments.FRETLESS_BASS )
drumStaff = arezzo.Staff( arezzo.instruments.DRUM_KIT )
pianoStaff = arezzo.Staff( arezzo.instruments.PIANO )

# add count off measure
rMeasure = arezzo.Measure()
rMeasure.addNote( arezzo.Rest(1,1) )
bassStaff.addMeasure( rMeasure )
pianoStaff.addMeasure( rMeasure )

countOffMeasure = arezzo.Measure()
countOffMeasure.addNote( arezzo.Note('F#2', 1, 4) ) # F#2 is a closed hihat
countOffMeasure.addNote( arezzo.Note('F#2', 1, 4) )
countOffMeasure.addNote( arezzo.Note('F#2', 1, 4) )
countOffMeasure.addNote( arezzo.Note('F#2', 1, 4) )
drumStaff.addMeasure( countOffMeasure )



for chord, time in leadsheet:
   
   
   match = re.match( "([a-gA-G])(#|b|B|)(m|maj|M)?", chord)
   chordcomponents = match.groups()
   root = chordcomponents[0] + chordcomponents[1]
   quality = chordcomponents[2] 
   
   print "chord %s with quality %s" % (root, quality ) 
   
   measure =  basie.randomWalkingBassPattern( root, quality )
   bassStaff.addMeasure( measure ) 


   measure = basie.pianoComp( root , quality )
   pianoStaff.addMeasure( measure )
   


   drumStaff.addMeasure( basie.simpleHats() )


score.addStaff( bassStaff )
score.addStaff( pianoStaff )
score.addStaff( drumStaff )

     

   
   




writeMidi( score , context, 0, theFile )

binfile = open("output.mid", "wb")
theFile.writeFile( binfile )
binfile.close()
