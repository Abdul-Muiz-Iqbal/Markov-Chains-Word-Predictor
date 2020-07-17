from string import *
from random import choices

def spReplace(source):
    new_txt = source
    for punc in punctuation:
        new_txt = new_txt.replace(punc, f" {punc}")
    return new_txt


def MarkovPredict(txt, times=0):
    word_map = {}
    i = 0
    txt = spReplace(txt.lower())
    for word in txt.split(" "):
        try:
            word_map[word].append(txt.split(" ")[i + 1])
        except KeyError:
            try:
                word_map[word] = [txt.split(" ")[i + 1]]
            except:
                pass
        except:
            pass
        i += 1
    print(word_map)
    try:
        next_word = choices(word_map[txt.split(" ")[-1]])[0]
    except:
        next_word = ''
    return next_word
