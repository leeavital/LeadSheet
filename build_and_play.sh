# runs AL mid and plays the file with timidity 
python al_mid.py infile=examples/autumn_leaves.txt tempo=200
timidity output.mid -D 11 ## wtf
