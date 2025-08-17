# Reverse each string from a string/array
input_string = "Hello world this is a string"

def reverse(input_string:str) -> str:
    if len(input_string) == 0:
        return ""
    rev = input_string.split(" ")
    reverse_list = []
    for word in rev:
        revword = ""
        for i in range(len(word)-1,-1,-1):
            revword += word[i]
        reverse_list.append(revword.lower())

    rev_string = " ".join(reverse_list)
    return rev_string

print(reverse(input_string))
