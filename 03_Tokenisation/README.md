#instructions in the README.md in Markdown on how to use the program;
#brief description of its performance, with examples to support your findings


`MAXMATCH`

The MaxMatch algorithm is typically used in natural language processing for tokenization and word and sentence segmentation for languages that are written without spaces such as Chinese, Japanese and Thai. The MaxMatch program typically works by selecting the beginning of the string (e.g. a line), segmenting a string of characters after finding the longest possible words in a given dictionary. Ater finding the first word, it moves to the next segment of the string and repeats the process until the entire string is segmented. Then, the program outputs the segmented words.

For example, consider the data from Chinese, which is contained in a `.conllu` file (which follows the format of [CoNLL-U](https://universaldependencies.org/format.html#words-tokens-and-empty-nodes)),in a string such as "禁止在私人公司內表達宗教信仰的行為的限度是什麼?" and a dictionary including the words ["禁止", ",在", "私人", "公司", "內", "表達", "宗教", "信仰", "的", "行為", "的", "限度", "是", "什麼", "?"]. The MaxMatch program would start at the first character "禁" and check whether it matches any word in the dictionary. Since "禁" is not a word by itself, the program moves to the next character "禁止" which matches a word in the dictionary. The Maxmatch then selects "禁止" as the longest word and moves to the next characters until it reaches the end of the string. After p
processing the whole string, the output would be ["禁止 在 私人 公司 內 表達 宗教 信仰 的 行為 的 限  度 是 什麼 ?"].

It is important to notice that the MaxMatch program may not produce the expected/desired segmentation output when dealing with ambiguous words or words that are not in the given dictionary. After running the `evaluate.py`, for instance, this sentence gets a WER of 13.33%. Although the WER is low, the sentence is not segmented as expected: 
REF: 禁止 在 私人 公司 內 表達 宗教 信仰 的 行為 的 限度   是 什麼 ？
HYP: 禁止 在 私人 公司 內 表達 宗教 信仰 的 行為 的 限  度 是 什麼 ？

MAXMATCH PROGRAM:

```ruby
import sys

for sentence in open('original.test.txt', 'r'):
        def maxmatch(sentence, dictionary):
                if not sentence:
                        return []
                for c in range(len(sentence), 0, -1):
                        firstword = sentence[0:c+1]
                        reminder = sentence[c+1:len(sentence)]
                        if firstword in dictionary:
                                return [firstword] + maxmatch(reminder, dictionary)

                #if word not found, then word as one-character
                firstword = sentence[0]
                reminder = sentence[1:len(sentence)]
                return [firstword] + maxmatch(reminder, dictionary)

        with open('dictionary.txt', 'r') as file:
                dictionary = [line.strip() for line in file]
                print(' '.join(maxmatch(sentence, dictionary)), end='')

``` 
To run this algorithm, use `cat original.test.txt | python3 maxmatch.py`. Note that the `dictionary.txt` is already in the `maxmatch.py` program, so it does not need to be specified in the terminal.
