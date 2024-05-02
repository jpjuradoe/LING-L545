import sys, re, unicodedata

alphabet = '\n  aâàæǽêïèëïiïìîoeoôòœóuûùübcçdfghjklmnpqrstvwxyÿz,.,;()\\\'\*¡!"":¿?0123456789'

characters = {}

for line in sys.stdin:
	line = line.strip('\n')
	valid = True
	for char in line:
		if char.lower() not in alphabet:
			if char not in characters:
				characters[char] = 0
			characters[char] += 1
			valid = False
	if valid:
		print(line)

chfr = list(characters.items())
chfr.sort(key=lambda x:x[1], reverse=True)
for p, c in chfr:
	print(c, '\t', p, '\t', '%x' % ord(p), '\t', unicodedata.category(p), file=sys.stderr)
