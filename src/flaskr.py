from flask import Flask, render_template
from flask import request
from midiutil.MidiFile import MIDIFile
from threading import Thread
from writer import writeMidi
import flask
import json
import med_jazz
import os
import random
import subprocess

app = Flask(__name__)

app.config['TESTING'] = False
# app.config['PORT'] = 80


# I don't know where to put this...
class Context:

  """holds tempo"""

  def __init__(self, tempo):
    self.tempo = tempo
    self.track = 0


class ConvertJob(Thread):

  def __init__(self, id, data):
    Thread.__init__(self)
    self.id = id
    self.data = data

  def run(self):
    print "running"

    self.midiname = "files/" + str(self.id) + ".mid"
    self.wavname = "files/" + str(self.id) + ".wav"
    context = Context(self.data["tempo"])
    leadsheet = [(x, 4) for x in self.data["chords"]]

    score = med_jazz.getScore(leadsheet, repeat=2, countoff=True)

    theFile = MIDIFile(16)
    theFile.addTempo(0, 0, context.tempo)

    writeMidi(score, context, 0, theFile)

    binfile = open(self.midiname, "wb")
    theFile.writeFile(binfile)
    binfile.close()

    # now turn it into an wav
    subprocess.call(["./convert.sh", self.midiname, self.wavname])

    print "here we are..."


@app.route('/')
def hello_world():
  return flask.send_file("./static/index.html", mimetype="text/html")


@app.route('/fonts/<path>')
def serve_fonts(path):
  print "serving " + path
  return flask.send_file("./static/fonts/" + str(path))


@app.route('/music', methods=["GET"])
def music():

  print request.form
  print request.form.getlist("chords[]")

  data = {}
  data["tempo"] = int(request.args["tempo"])
  data["chords"] = [str(x) for x in request.args.getlist("chords[]")]

  rand = "".join([str(int(random.random() * 10)) for x in range(0, 20)])

  t = ConvertJob(rand, data)
  t.run()  # that was stupid..
  # t.join()

  return flask.send_file(t.wavname, mimetype="audio/wav")

if __name__ == '__main__':
  print "starting"
  app.run(host="0.0.0.0")
