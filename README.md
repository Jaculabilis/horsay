# horsay
```
~$ horsay --help
usage: horsay [-h] [-u] [-w MAX_WIDTH] [-b BREAK_AT]

Displays input straight from the horse's mouth.

optional arguments:
  -h, --help            show this help message and exit
  -u, --unicode         Use fancier lines for the text bubble
  -w MAX_WIDTH, --max-width MAX_WIDTH
                        Maximum width of output (default: 80)
  -b BREAK_AT, --break-at BREAK_AT
                        String of characters to break words at (default: space
                        and -)

~$ horsay
Hello, world!
     ./|,,/|   
    <   o o)   +---------------+
   <\ (    | --| Hello, world! |
  <\\  |\  |   +---------------+
 <\\\  |(__)   
<\\\\  |       
~$ echo "Hello, pipe!" | horsay
     ./|,,/|   
    <   o o)   +--------------+
   <\ (    | --| Hello, pipe! |
  <\\  |\  |   +--------------+
 <\\\  |(__)   
<\\\\  |       
~$ echo "Hello, fancy box!" | horsay -u
     ./|,,/|   
    <   o o)   ╭───────────────────╮
   <\ (    | ──┤ Hello, fancy box! │
  <\\  |\  |   ╰───────────────────╯
 <\\\  |(__)   
<\\\\  |       
```
