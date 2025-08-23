
def checkanagrams(string1,string2):
    str1dict = {}
    str2dict = {}

    for ch1,ch2 in zip(string1,string2):
        if len(string1) != len(string2):
            return False
        str1dict[ch1] = str1dict.get(ch1,0)+1
        str2dict[ch2] = str2dict.get(ch2,0)+1

    if str1dict == str2dict:
        return True
    return False
        


print(checkanagrams("ana","aan"))
