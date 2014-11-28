import arezzo
import basie
import re

import arezzo.instruments


def getScore(leadsheet, **args):

  if "repeat" in args:
    repeat = args["repeat"]
  else:
    repeat = 1

  if "countoff" in args:
    countoff = args["countoff"]
  else:
    countoff = False

  score = arezzo.Score()

  # go through the chords
  bassStaff = arezzo.Staff(arezzo.instruments.FRETLESS_BASS)
  drumStaff = arezzo.Staff(arezzo.instruments.DRUM_KIT)
  pianoStaff = arezzo.Staff(arezzo.instruments.PIANO)

  if countoff:

    # add count off measure
    rMeasure = arezzo.Measure()
    rMeasure.addNote(arezzo.Rest(1, 1))
    bassStaff.addMeasure(rMeasure)
    pianoStaff.addMeasure(rMeasure)

    countOffMeasure = arezzo.Measure()
    countOffMeasure.addNote(arezzo.Note('F#2', 1, 4))  # F#2 is a closed hihat
    countOffMeasure.addNote(arezzo.Note('F#2', 1, 4))
    countOffMeasure.addNote(arezzo.Note('F#2', 1, 4))
    countOffMeasure.addNote(arezzo.Note('F#2', 1, 4))
    drumStaff.addMeasure(countOffMeasure)

  for i in range(0, repeat):
    for chord, time in leadsheet:

      match = re.match("([a-gA-G])(#|b|B|)(m|maj|M)?", chord)
      chordcomponents = match.groups()
      root = chordcomponents[0] + chordcomponents[1]
      quality = chordcomponents[2]

      measure = basie.randomWalkingBassPattern(root, quality)
      bassStaff.addMeasure(measure)

      measure = basie.pianoComp(root, quality)
      pianoStaff.addMeasure(measure)

      drumStaff.addMeasure(basie.simpleHats())

  score.addStaff(bassStaff)
  score.addStaff(pianoStaff)
  score.addStaff(drumStaff)

  return score
