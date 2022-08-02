#! /bin/zsh

for FILE in $(ls); do; if [ -d $FILE ]; then; echo "DIR $FILE">&1; else; echo "FILE $FILE">&1; fi ; done
# for FILE in $(ls); do; if [ -d $FILE ]; then; echo "DIR $FILE"; else; echo "FILE $FILE"; fi ; done