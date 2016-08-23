# JPMorgan
# Camel Case

def camelCaseConverter(input):

    output = ""
    capital = False

    if len(input)<=1:
        return input

    for i in range(len(input)-1):

        first = input[i]
        second = input[i+1]

        if ord(first) in range(65,91) and ord(second) in range(65,91):
           output += first
           capital = True
        elif ord(first) in range(97,122) and ord(second) in range(65,91):
           output += first+"_"
           capital = False
        elif ord(first) in range(65,91) and ord(second) in range(97,122) and capital:
           output += "_"+first
           capital = False
        else:
           output += first

    return output+input[-1:]

print camelCaseConverter("JPMorganHelloWorD")
