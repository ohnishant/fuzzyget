#!/bin/bash

for file in ./logs/*; do
  if [ -f "$file" ]; then
    truncate -s 0 "$file"
  fi
done