def keyPadCombinations(input):
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    input = str(input)
    ret = ['']
    for char in input:
        letters = digit_map.get(char, '')
        ret = [prefix+letter for prefix in ret for letter in letters]
    return ret

print keyPadCombinations("234")