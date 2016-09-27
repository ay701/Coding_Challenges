def buildSubsequences(s):
    
    output = []
    tmpOutput = []

    for i, c in enumerate(s):
        # Loop through all characters
        for j in range(i, len(s)):
        # Build the output string
            tmpstr = ''
            for k in range(i, j+1):
                tmpstr += s[k]

            output.append(tmpstr)

            if j-i>1:
            	tmpOutput = buildSubsequences(s[i]+s[i+2:j+1])

    return tmpOutput + list(set(output) - set(tmpOutput))

print buildSubsequences('ab')
print buildSubsequences('abc')