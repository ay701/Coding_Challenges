f = open(os.environ['OUTPUT_PATH'], 'w')
    

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()

