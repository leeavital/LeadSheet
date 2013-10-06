import arezzo


import random


def pianoComp( root , quality ):
   
   
   root = arezzo.Note( root + '4', 1, 1 )
   
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
   
   if  n < .5:
	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 5, 12 ) )
   	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 7, 12 ) )
   else:
	  m.addNote( arezzo.Rest( 2, 12 ) )
   	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 4, 12 ) )
	  m.addNote( arezzo.ToneCluster( [root, third, fifth], 2, 4 ) )

   return m

