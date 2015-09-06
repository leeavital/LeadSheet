# runs AL mid and plays the file with timidity 
python al_mid.py infile=examples/autumn_leaves.txt tempo=200 repeat=2
## wtf, not really sure why drums are on 11 and not 10 like I told them to be
timidity output.mid -D 11 -Ow -o   - | lame - -b 64 output.mp3
audacious output.mp3
