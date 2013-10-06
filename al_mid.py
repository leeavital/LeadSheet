import arezzo
import arezzo.instruments as a_instruments

from writer import writeMidi

from midiutil.MidiFile import MIDIFile

import re

import basie

import sys

import med_jazz


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
countoff = True
for arg in sys.argv:
   if arg.find("tempo=") == 0:
	  tempo = int(arg[6:])

   elif arg.find( "infile=" ) == 0:
	  infile = arg[7:]

   elif arg.find( "repeat=") == 0:
	  repeat = int(arg[7:])

   elif arg.find( "countoff=" ) == 0:
	  countoff = arg[10:] == "yes"
   


print "PARSED ARGUMENTS:"
print "tempo: %d" % tempo
print "infile: %s" % infile
print "countoff %s" % countoff
print "repeat %d" % repeat



# build the leadsheet
leadsheet = []
for l in open( infile ):
   leadsheet.append( (l, 4 ) )

context = Context( tempo )

theFile = MIDIFile( 16 )
# theFile.addTrackName( 0, 0, "Sample Track" )
theFile.addTempo( 0, 0, context.tempo )


TEMPO = 120



score = med_jazz.getScore( leadsheet, repeat = repeat, countoff = countoff )
   



writeMidi( score , context, 0, theFile )

binfile = open("output.mid", "wb")
theFile.writeFile( binfile )
binfile.close()
