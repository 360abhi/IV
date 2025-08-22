input = "abcdeeeeef"

def flat(input:str):
    freq = 1
    output = ""
    for i in range(len(input)-1):
        if not input:
            return
        if input[i] == input[i+1]:
            freq +=1
        else:
            output += f"{input[i]}{freq}"
            freq = 1
    output += f"{input[len(input)-1]}{freq}"
    return output


print(flat(input=input))
    