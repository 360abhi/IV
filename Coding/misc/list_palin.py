input = ["pop","abhishek","nonoe","canac"]

def palin(input:list):
    return list(filter(lambda x: x == x[::-1],input))
    # return [s for s in input if s == s[::-1]]

print(palin(input=input))