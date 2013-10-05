# patter for walking bass

import arezzo

def randomWalkingBassPattern( basenote, quality ):
   """basenote comes in as just a letter (a. F#)
      quality can only be a triad quality (m, M, dim, aug), 
	  if none is given, assume major"""
   
    

   return oneTwoThreeFive   





def oneTwoThreeFive(basenote, quality ):

   root = arezzo.Note( basenote, 1, 4 )
   second = root.interval( 2 )

   if quality == "m" or quality == "dim": 
	  third = root.interval( 3 ) 
   else :
	  
	  root.interval( 4 )

   fourth = root.interval(  5 )

   fifth = root.fifth( )

   m = arezzo.Measure()
   m.addNote( root , 1, 4 )
   m.addNote( second, 1, 4 )
   m.addNote( third , 1, 4 )
   m.addNote( fifth , 1, 4 )
    



