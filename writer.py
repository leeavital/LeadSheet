"""this module defines the write midi function"""

import arezzo


def writeMidi(musicEntity, context, timeOffset, midiFile):

  if isinstance(musicEntity, arezzo.Score):

    for staff in musicEntity.staves:

      # program change, set the instrument
      if staff.instrument() == arezzo.instruments.DRUM_KIT:
        context.track = 10
        # TERRIBLE TERRIBLE TERRIBE, The drum track has to be added
        # last
      else:
        midiFile.addProgramChange(
            context.track, context.track, timeOffset, staff.GMCode())  # frettless bass

      # time offset is always the same
      writeMidi(staff, context, timeOffset, midiFile)
      context.track = context.track + 1

    return timeOffset

  elif isinstance(musicEntity, arezzo.Staff):

    # too lazy for whatever functional bullshit I should be doing instead
    offset = timeOffset
    for measure in musicEntity.measures:
      offset = writeMidi(measure, context, offset, midiFile)

    return offset

  elif isinstance(musicEntity, arezzo.Measure):

    offset = timeOffset  # janks, assumes every voice
    # takes the same amount of time
    for voice in musicEntity.voices:
      writeMidi(voice, context, timeOffset, midiFile)

    return timeOffset + 4

  elif isinstance(musicEntity, arezzo.Voice):

    offset = timeOffset
    for token in musicEntity.notesAndRests:
      offset = writeMidi(token, context, offset, midiFile)

    return offset

  elif isinstance(musicEntity, arezzo.Note):
    # everything is in FOUR
    length = ((musicEntity.time[0] * 1.0) / musicEntity.time[1]) * 4

    # the magic!
    midiFile.addNote(context.track, context.track, musicEntity.midicode(
    ), timeOffset, length, musicEntity.dynamic)

    return timeOffset + length

  elif isinstance(musicEntity, arezzo.Rest):
    # everything is in FOUR
    length = ((musicEntity.time[0] * 1.0) / musicEntity.time[1]) * 4

    return timeOffset + length

  elif isinstance(musicEntity, arezzo.ToneCluster):

    # everything is in FOUR
    length = ((musicEntity.time[0] * 1.0) / musicEntity.time[1]) * 4

    # the other magic!
    for note in musicEntity.notes:
      midiFile.addNote(
          context.track, context.track, note.midicode(), timeOffset, length, note.dynamic)

    return timeOffset + length

  else:
    print "OH SHIT WHAT IS IT?"
    return timeOffset

  # yeah! recursive descent bitch
