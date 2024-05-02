import sys, re

line = sys.stdin.readline()

while line:
        for word in line.strip().split(' '):
                if not word:
                        continue
                if word[-1] in '!?':
                        sys.stdout.write(word + '\n')
                elif word[-1] == '.':
                        word = word.strip('()')
                        if word in ['var.', 'subsp.', 'etc.', 'e.g.', 'ing.']:
                                sys.stdout.write(word + ' ')
                        elif re.match('[a-zA-z]\.', word):
                                sys.stdout.write(word + ' ')
                        else:
                                 sys.stdout.write(word + '\n')
                else:
                        sys.stdout.write(word + ' ')
        line = sys.stdin.readline()
