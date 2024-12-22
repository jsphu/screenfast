# Fast screen tools.
## scr
Usage: scr [session-name]

[session-name]; returns randomized 2 letter name and attaches to new session if not specified. Or simply attaches to existing session.

Fast screen command for screen -S [session-name] or screen -r [session-name]etc.

## scrq
Usage: scrq [session-name]

Terminates given session-name.

## .screenrc configurations.

If you got already .screenrc it won't touch it.
New: Bottom indicator text which tells your currently screen session name.

## How to install.
1. Open your terminal. \<ctrl+alt+T\> (default)
2. Clone repository. `git clone https://github.com/jsphu/screenfast`
3. Change directory to 'screenfast'. `cd ./screenfast`
4. Run python file. `python3 install.py`
5. And you are done.
