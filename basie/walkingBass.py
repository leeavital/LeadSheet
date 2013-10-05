# patter for walking bass

import arezzo

def randomWalkingBassPattern( basenote, quality ):
   """basenote comes in as just a letter (a. F#)
      quality can only be a triad quality (m, M, dim, aug), 
	  if none is given, assume major"""
   
    

   return oneTwoThreeFive( basenote, quality )





def oneTwoThreeFive(basenote, quality ):

   root = arezzo.Note( basenote + "2", 1, 4 )
   second = root.interval( 2 )

   if quality == "m" or quality == "dim": 
	  third = root.interval( 3 ) 
   else :
	  third = root.interval( 4 )

   
   if quality == "dim":
	  fifth = root.interval( 6 )
   elif quality == "aug":
	  fifth = root.interval( 8 )
   else:
	  fifth = root.interval( 7 )

   m = arezzo.Measure()
   m.addNote(  root )
   m.addNote(  second )
   m.addNote(  third )
   m.addNote(  fifth )

   return m
    



