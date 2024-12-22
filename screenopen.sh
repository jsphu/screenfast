#!/bin/bash

name="$1"

if [ -z "$name" ]; then 
  name="$(cat /dev/urandom | tr -dc 'a-z'| head -c 2)"
fi

if screen -ls | grep -q "\.$name"; then
  screen -r "$name"
else 
  screen -S "$name"
fi
