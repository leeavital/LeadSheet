# fout hihat quarter notes
import arezzo


# Drum to Note values (for reference only, this should be in an enum)
# A#2 -- open high hat
# F#2 -- closed high hat
# B1 -- Acoustic Bass drum
# C1 -- Bass drup
# E2 --snare drum 2
# D#3 -- crash


i = 0


def simpleHats():

  global i

  m = arezzo.Measure()

  v = arezzo.Voice()
  v.addNote(arezzo.Note('A#2', 1, 4))
  v.addNote(arezzo.Note('F#2', 2, 12))
  v.addNote(arezzo.Note('F#2', 1, 12))

  v.addNote(arezzo.Note('A#2', 1, 4))
  v.addNote(arezzo.Note('F#2', 2, 12))
  v.addNote(arezzo.Note('F#2', 1, 12))

  m.addVoice(v)

  v = arezzo.Voice()

  # splash on the first downbeat
  # flam(?) on the last downbeat
  # four measure phrases!
  if i == 0:
    v.addNote(arezzo.Note('D#3', 1, 1))
    m.addVoice(v)
  elif i == 3:
    v.addNote(arezzo.Rest(8, 12))
    v.addNote(arezzo.Note('E2', 3, 12))
    v.addNote(arezzo.Note('E2', 1, 12))
    m.addVoice(v)

  i = (i + 1) % 4

  # bass drum
  v = arezzo.Voice()
  v.addNote(arezzo.Note('C2', 8, 12))
  v.addNote(arezzo.Note('C2', 3, 12))
  v.addNote(arezzo.Note('C2', 1, 12))

  # this doesn't work so well...so we'll leave it out!
  # bass drum
  # v = arezzo.Voice()
  # v.addNote( arezzo.Note( 'C2', 8, 12)  )
  # v.addNote( arezzo.Note( 'C2', 3, 12)  )
  # v.addNote( arezzo.Note( 'C2', 1, 12)  )

  return m
