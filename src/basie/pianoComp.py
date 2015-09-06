import arezzo


import random


# we'll cycle through this variable
i = 0


def pianoComp(root, quality):

  global i

  root = arezzo.Note(root + '6', 1, 1)

  if quality == "dim":
    fifth = root.interval(6)
  elif quality == "aug":
    fifth = "8"
  else:
    fifth = root.fifth()

  if quality == "m" or quality == "dim":
    third = root.interval(3)
  else:
    third = root.interval(4)

  m = arezzo.Measure()

  n = random.random()
  pianoAround = arezzo.Note('G4', 1, 1)

  if i == 0:
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 5, 12).around(pianoAround))
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 7, 12).around(pianoAround))
  elif i == 1:
    m.addNote(arezzo.Rest(2, 12))
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 4, 12).around(pianoAround))
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 2, 4).around(pianoAround))
  elif i == 2:
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 1, 4).around(pianoAround))
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 1, 4).around(pianoAround))
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 2, 4).around(pianoAround))
  else:
    m.addNote(arezzo.Rest(5, 12))
    m.addNote(
        arezzo.ToneCluster([root, third, fifth], 7, 12).around(pianoAround))

  # four bar phrases
  i = (i + 1) % 4

  return m
