
```ruby
import sys
#sentence = 'wecanonlyseethem'
#dictionary = ['we', 'can', 'canon', 'only', 'see']

#for sentence in sys.stdin: #open text
for sentence in open('original.test.txt', 'r'):
        def maxmatch(sentence, dictionary): #function maxmatch returns word sequence W                if not sentence:
                        return [] #empty list
                for c in range(len(sentence), 0, -1): #downto 1
                        firstword = sentence[0:c+1]
                        reminder = sentence[c+1:len(sentence)]
                        if firstword in dictionary:
                                return [firstword] + maxmatch(reminder, dictionary)

                #if word not found, then word as one-character
                firstword = sentence[0]
                reminder = sentence[1:len(sentence)]
#               return [firstword] + ([] if not reminder else maxmatch(reminder, dict>                return [firstword] + maxmatch(reminder, dictionary)

        with open('dictionary.txt', 'r') as file:
                dictionary = [line.strip() for line in file]
#               result = maxmatch(sentence, dictionary)
                print(' '.join(maxmatch(sentence, dictionary)), end='')

```
