import arezzo
import arezzo.instruments as a_instruments

from writer import writeMidi

from midiutil.MidiFile import MIDIFile

import re

import basie

import sys


# I don't know where to put this...
class Context:
   """holds tempo"""   
   def __init__( self, tempo  ):
	  self.tempo = tempo
	  self.track = 0



tempo = 120
feel = "Med Jazz"
infile = ""
repeat = 1
for arg in sys.argv:
   if arg.find("tempo=") == 0:
	  tempo = int(arg[6:])

   elif arg.find( "infile=" ) == 0:
	  infile = arg[7:]

   elif arg.find( "repeat=") == 0:
	  repeat = int(arg[7:])



# build the leadsheet
leadsheet = []
for l in open( infile ):
   leadsheet.append( (l, 4 ) )

context = Context( tempo )

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





for i in range( 0, repeat ):
   for chord, time in leadsheet:
      
      
      match = re.match( "([a-gA-G])(#|b|B|)(m|maj|M)?", chord)
      chordcomponents = match.groups()
      root = chordcomponents[0] + chordcomponents[1]
      quality = chordcomponents[2] 
      
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
