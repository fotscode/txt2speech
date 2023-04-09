#!/bin/bash

# list of all the files to be processed in a directory
for file in $(exa ./segments/* -1)
do
    echo "Processing $file"
    sleep 5
    python ./generate_tts.py $file
done
