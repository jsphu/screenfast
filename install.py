_screenrc=r"""# Automatically display the session name in the terminal upon attach
#shelltitle "$STY"
#autodetach on

#Disable the welcome message
startup_message off

#screen -X echo "Attached to session: $STY"

# Display a welcome message and session name when attaching
backtick 1 0 0 echo "$STY"
hardstatus alwayslastline
hardstatus string "Attached to: %1`"
"""

_screenopen=r"""#!/bin/bash

name="$1"

if [ -z "$name" ]; then 
  name="$(cat /dev/urandom | tr -dc 'a-z'| head -c 2)"
fi

if screen -ls | grep -q "\.$name"; then
  screen -r "$name"
else 
  screen -S "$name"
fi
"""

_screenkill=r"""#!/bin/bash

check_screens(){
    CREEN=$(screen -ls | wc -l)
    if [ $CREEN -eq 2 ]; then
        echo "No Sockets found in /run/screen/S-$USER."
    else 
        screen -ls
    fi 
}

ID="$1"

if [ -z "$ID" ]; then
    echo "Error: Empty session-name."
elif screen -S "$ID" -X quit 2>/dev/null; then
    echo "[screen is terminating]"
fi

check_screens
"""

import os

home=os.path.expanduser("~")

def scriptsDir():
    scripts=os.path.join(home,".scripts")
    if not os.path.isdir(scripts):
        os.mkdir(scripts)
    return scripts

def bashrcExists():
    try:
        bashrc = os.path.join(home, ".bashrc")
        with open(bashrc, "r") as f:
            bashrc_content = f.read()
            if ".bash_aliases" not in bashrc_content and \
                    ".aliases" not in bashrc_content:
                print("Warning: Neither .bash_aliases nor",
                    ".aliases is sourced in .bashrc.")
                print("Add the following to your .bashrc:")
                print('if [ -f ~/.bash_aliases ]; then\n',
                    '. ~/.bash_aliases\nfi')
                return False
        return True
    except:
        print("Error: ./.bashrc is not found.")
        return None

def screenopen():
    home=scriptsDir()
    directory=os.path.join(home,"screenopen.sh")
    with open(directory, "w") as scropen:
        scropen.write(_screenopen)
        print("{} is created.".format(directory))
    return directory

def screenkill():
    home=scriptsDir()
    directory=os.path.join(home,"screenkill.sh")
    with open(directory, "w") as scrkill:
        scrkill.write(_screenkill)
        print("{} is created.".format(directory))
    return directory

def aliasWrite():
    if bashrcExists:
        bash_aliases = os.path.join(home,".bash_aliases")
        aliases = os.path.join(home,".aliases")

        target=bash_aliases
        if os.path.exists(aliases):
            target=aliases
        scr=screenopen()
        scrkill=screenkill()
        with open(target,"a") as alias:
            alias.write('\nalias scr="{}"\nalias scrq="{}"'.format(scr,scrkill))
        
        print("Commands added to {}..".format(target))
        print("To apply changes, run: source ~/.bashrc")
    else:
        print("Exitting with status code:",2)
        exit()
screenrc="{}/.screenrc".format(home)

if not os.path.exists(screenrc):
    with open(screenrc, "w") as scrc:
        scrc.write(_screenrc)

bashrcExists()
aliasWrite()
os.system("chmod u+x .scripts/screenopen.sh .scripts/screenkill.sh")
print("Screen configuration is done.")
