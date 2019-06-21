#!/usr/bin/python3

from __future__ import print_function
import itertools
import platform
import argparse
import hashlib
import string

class Collisor:

    class bcolors:
        if platform.system() == 'Linux': # print colored only if the user is using a Linux OS
            
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
        else:
            HEADER = ''
            OKBLUE = ''
            OKGREEN = ''
            WARNING = ''
            FAIL = ''
            ENDC = ''
            BOLD = ''
            UNDERLINE = ''

    def __init__(self):
        self.collision = ''
        self.collision_hashed = ''
        self.VERSION = 'v0.1'
        self.found = False

    def welcome_message(self,bcolors=bcolors):
        print(r'''%s

            _     _    _           _____ _    _ 
           | |   | |  | |   /\    / ____| |  | | %s{by G4L1C %s}%s
  ___ _   _| |__ | |__| |  /  \  | (___ | |__| |
 / __| | | | '_ \|  __  | / /\ \  \___ \|  __  |
 \__ \ |_| | |_) | |  | |/ ____ \ ____) | |  | |
 |___/\__,_|_.__/|_|  |_/_/    \_\_____/|_|  |_|
 

        %s''' % (bcolors.OKGREEN,bcolors.ENDC,self.VERSION,bcolors.OKGREEN,bcolors.ENDC))


    def gen_word(self,char_list,lenght):
        for word in itertools.combinations(char_list,lenght):
            yield ''.join(word)


    def collise(self,hash_substring,starting_position,ending_position):
        _hash_substring = hash_substring
        _found = False
        _trial = 1
        _list_size = 1
        
        while _found == False and _list_size <=  16: # will try until reach a list of 16 characters long or finds the collision
            _gen = self.gen_word(string.printable,_list_size)
            
            for i in _gen:
                print(' %s[+] Number of trials:%s %s' % (b.OKGREEN,b.ENDC,_trial), end='\r')
                
                if (hashlib.md5(i.encode()).hexdigest())[starting_position:ending_position] == _hash_substring:
                    _found = True
                    self.found = True
                    self.collision = i
                    self.collision_hashed = hashlib.md5(i.encode()).hexdigest()
                    print("\r") # cleans the carraige return of the Number of Trials print message
                    break

                _trial += 1
            _list_size += 1
                      
        return self.collision

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Find a collision to a given MD5 substring.')
    parser.add_argument('--subHash', '-sh',help='Hash substring to be collised.', required = True)
    parser.add_argument('--sChar', '-sc', type=int, help='Starting posistion of the hash substring (start=0).', default=0)
    args = parser.parse_args()

    c = Collisor()
    c.welcome_message()
    b = c.bcolors

    if args.subHash:
        print(' %s[+] Started collision for:%s %s' % (b.OKGREEN,b.ENDC,args.subHash))

    if args.sChar:
        print(' %s[+] Starting hash substring position:%s %s' % (b.OKGREEN,b.ENDC,args.sChar))
    else:
        args.sChar = 0
        print(' %s[+] Starting hash substring position:%s 0' % (b.OKGREEN,b.ENDC))

    print(' %s[+] Substring lenght:%s %s' % (b.OKGREEN,b.ENDC,len(args.subHash)))
    
    c.collise(args.subHash,args.sChar,len(args.subHash))

    if c.found:
        print(' %s[+] Collision found:%s %s' % (b.OKBLUE,b.ENDC,c.collision))
        print(' %s[+] Hashed collision:%s %s' % (b.OKBLUE,b.ENDC,c.collision_hashed))
    else:
        print(' %s[+] Collision not found! Make sure the substring is not too long.%s' % (b.FAIL,b.ENDC))
