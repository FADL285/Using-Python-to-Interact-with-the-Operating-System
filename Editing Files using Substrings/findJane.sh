#!/bin/bash

files=$(grep " jane " ~/data/list.txt | cut -d ' ' -f 3)
for file in $files; do
  if [ -e $HOME$file ]; then
    echo $HOME$file >> oldFiles.txt;
  fi
done