input = ["abhishek","hello","world"]

def reverse(input:list):
    return list(map(lambda x: x[::-1],input))

print(reverse(input=input))