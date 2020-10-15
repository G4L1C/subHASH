# subHASH
Finds a collision for a given MD5 substring

Usage:
```
usage: foo.py [-h] --subHash SUBHASH [--sChar SCHAR]

Find a collision to a given MD5 substring.

optional arguments:
  -h, --help            show this help message and exit
  --subHash SUBHASH, -sh SUBHASH
                        Hash substring to be collised.
  --sChar SCHAR, -sc SCHAR
                        Starting posistion of the hash substring (start=0).
```

Example:
```
C:\Example> python ./subHash.py -sh 7abc -sc 0

           _     _    _           _____ _    _
          | |   | |  | |   /\    / ____| |  | | %s{by G4L1C %s}%s
 ___ _   _| |__ | |__| |  /  \  | (___ | |__| |
/ __| | | | '_ \|  __  | / /\ \  \___ \|  __  |
\__ \ |_| | |_) | |  | |/ ____ \ ____) | |  | |
|___/\__,_|_.__/|_|  |_/_/    \_\_____/|_|  |_|


[+] Started collision for: 7abc
[+] Starting hash substring position: 0
[+] Substring length: 4
[+] Number of trials: 28720
[+] Collision found: f@\
[+] Hashed collision: 7abcc787cf941b558da76936877074da
```
