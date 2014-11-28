# patter for walking bass

import arezzo
import random


def randomWalkingBassPattern(basenote, quality):
  """basenote comes in as just a letter (a. F#)
     quality can only be a triad quality (m, M, dim, aug), 
         if none is given, assume major"""

  n = random.random()
  if n < .75:
    return oneTwoThreeFive(basenote, quality)
  elif n < .9:
    return oneOneFiveFive(basenote, quality)
  else:
    return fiveFiveOneOne(basenote, quality)

  return oneOneFiveFive(basenote, quality)


def oneTwoThreeFive(basenote, quality):

  root = arezzo.Note(basenote + "2", 1, 4)
  second = root.interval(2)

  if quality == "m" or quality == "dim":
    third = root.interval(3)
  else:
    third = root.interval(4)

  if quality == "dim":
    fifth = root.interval(6)
  elif quality == "aug":
    fifth = root.interval(8)
  else:
    fifth = root.interval(7)

  m = one235Pattern()
  m.addNote(root.louder())
  m.addNote(second)
  m.addNote(third)
  m.addNote(fifth)

  return m


def oneOneFiveFive(basenote, quality):

  root = arezzo.Note(basenote + "2", 1, 4)

  if quality == "dim":
    fifth = root.interval(6)
  elif quality == "aug":
    fifth = root.interval(8)
  else:
    fifth = root.interval(7)

  m = one155Pattern()
  m.addNote(root.louder())
  m.addNote(root)
  m.addNote(fifth)
  m.addNote(fifth)

  return m


def fiveFiveOneOne(basenote, quality):

  root = arezzo.Note(basenote + "2", 1, 4)

  if quality == "dim":
    fifth = root.interval(6)
  elif quality == "aug":
    fifth = root.interval(8)
  else:
    fifth = root.interval(7)

  m = five5OneOnePattern()

  m.addNote(fifth.louder())
  m.addNote(fifth)
  m.addNote(root)
  m.addNote(root)

  return m


class one235Pattern(arezzo.Measure):
  pass


class one155Pattern(arezzo.Measure):
  pass


class five5OneOnePattern(arezzo.Measure):
  pass
