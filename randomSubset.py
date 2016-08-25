import random
def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
            #print result
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result

print random_subset('fx421359d8',5)
