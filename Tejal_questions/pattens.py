# reverse strings in an array
input_list_1 = ["Hello","World"]

def reverse(input:list):
    return [s[::-1] for s in input]

# print(reverse(input_list))

# palindromes in a list
input_list_2 = ["nan","cococ","notin"]

def palindrome(input:list):
    return [s for s in input if s==s[::-1]]

# print(palindrome(input=input_list_2))

#
