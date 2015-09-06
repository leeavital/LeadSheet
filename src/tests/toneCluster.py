import arezzo


c7 = arezzo.Note( 'C7', 1, 1 )
c2 = arezzo.Note( 'C2', 1, 1)
e7 = arezzo.Note( 'e7', 1, 1)
a7 = arezzo.Note( 'a7', 1, 1)
a1 = arezzo.Note( 'a1', 1, 1)


# test for around
tc = arezzo.ToneCluster( [c7], 1, 1)

tc0 = tc.around( arezzo.Note( 'C2', 1, 1 ) )
assert( not tc.notes[0].midicode() == tc0.notes[0].midicode() )
assert( tc0.notes[0].midicode() == c2.midicode() ) 



tc = arezzo.ToneCluster( [a7], 1, 1 )
tc0 = tc.around( arezzo.Note( 'C2', 1, 1 ) )
assert( tc0.notes[0].midicode() == a1.midicode() )



tc = arezzo.ToneCluster( [a7], 1, 1 )
tc0 = tc.around( arezzo.Note( 'C2', 1, 1 ) )
assert( tc0.notes[0].midicode() == a1.midicode() )





