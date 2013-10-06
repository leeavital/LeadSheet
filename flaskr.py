from flask import Flask, render_template
import random

from threading import Thread

from flask import request
import json
import flask


from writer import writeMidi

from midiutil.MidiFile import MIDIFile
import med_jazz

import subprocess

app = Flask(__name__)

app.config['TESTING'] = True 



# I don't know where to put this...
class Context:
   """holds tempo"""   
   def __init__( self, tempo  ):
	  self.tempo = tempo
	  self.track = 0



class ConvertJob( Thread ):
   
   def __init__(self, id, data ):
	  self.id = id
	  self.data = data
   
   def run(self):
	  print "running"
	  
	  midiname = "files/" + str(self.id) + ".mid"
	  mp3name = "files/" + str(self.id) + ".mp3"
	  context = Context( self.data["tempo"] )
	  leadsheet = [(x, 4) for x in self.data["chords"] ] 
	  
	  score = med_jazz.getScore( leadsheet, repeat=2, countoff=True)
	  
	  theFile = MIDIFile( 16 )
	  theFile.addTempo( 0, 0, context.tempo )

	  writeMidi( score, context, 0, theFile )

	  binfile = open(  midiname, "wb" )
	  theFile.writeFile( binfile )
	  binfile.close()


	  # now turn it into an mp3
	  # cmd = "timidity %s -D 11 -Ow -o - " % midiname # | lame - -b 64 %s" % (midiname, mp3name)
	  import os	  
	  os.execv( "convert.sh", ["", midiname , mp3name  ] )




@app.route('/')
def hello_world():
   return render_template( 'index.html' )



@app.route('/music', methods=["POST"])
def music():
   
   
   print request.form 
   print request.form.getlist( "chords[]" )

   data = {}
   data["tempo"] = int(request.form["tempo"])
   data["chords"] = [str(x) for x in request.form.getlist("chords[]") ]
   
   rand = "".join([ str(int(random.random() * 10)) for x in range( 0, 20 ) ])

   t = ConvertJob( rand, data )
   t.run()
   
   return flask.jsonify( {"code": rand} )

if __name__ == '__main__':
   app.run()





