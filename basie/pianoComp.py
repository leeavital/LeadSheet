import arezzo


import random



permutation  = [3,5]

def pianoComp( root , quality ):
   
   print permutation   
   root = arezzo.Note( root + '6', 1, 1 )
   
   if quality == "dim":
	  fifth = root.interval( 6 )
   elif quality == "aug":
	  fifth = "8"
   else:
	  fifth = root.fifth()
   

   


   if quality == "m" or quality == "dim":
      third = root.interval( 3 )
   else:
      third = root.interval( 4 )


   m = arezzo.Measure()
   

   n = random.random()
   
   
   pianoAround = arezzo.Note( 'G4', 1, 1)
    
   if n < .5:
	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 5, 12 ).around( pianoAround)  )
   	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 7, 12 ).around( pianoAround ) )
   else:
	  m.addNote( arezzo.Rest( 2, 12 ) )
   	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 4, 12 ).around( pianoAround ) )
	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 2, 4 ).around( pianoAround )  )

   return m

