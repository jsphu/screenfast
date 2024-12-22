#!/bin/bash

background=0
command=0

check_args(){
    args="$(echo "$@")"
    if $args | grep -q "\-dmS"; then
        background=1
    fi
    if $args | grep -q "\-X"; then
        command=1
    fi
}

check_screens(){
    CREEN=$(screen -ls | wc -l)
    if [ $CREEN -eq 2 ]; then
        echo "No Sockets found in /run/screen/S-$USER."
    else 
        screen -ls
    fi 
}

check_args
ID="$1"

if [ -z "$ID" ]; then
    echo "Error: Empty session-name."
elif screen -S "$ID" -X quit 2>/dev/null; then
    echo "[screen is terminating]"
fi

check_screens
