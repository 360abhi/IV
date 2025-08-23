from collections import defaultdict
input = ["eat","tea","tan","ate","nat","bat"]

def groupanagrams(input:list):
    anagrams = defaultdict(list)

    for word in input:
        key = ''.join(sorted(word)) # here key is sorted word
        anagrams[key].append(word)

    return anagrams.values()

print(groupanagrams(input))

    