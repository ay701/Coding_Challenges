
ur previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
# 
# Enjoy your interview!
# 
# 
# Problem Name is &&& Best Average Grade &&& PLEASE DO NOT REMOVE THIS LINE.

"""
  Instructions:

  Given a list of student test scores, find the best average grade.
  Each student may have more than one test score in the list.

  Complete the bestAverageGrade function in the editor below.
  It has one parameter, scores, which is an array of student test scores.
  Each element in the array is a two-element array of the form [student name, test score]
  e.g. [ "Bobby", "87" ].
  Test scores may be positive or negative integers.

  If you end up with an average grade that is not an integer, you should
  use a floor function to return the largest integer less than or equal to the average.
  Return 0 for an empty input.

  Example:

  Input:
  [ [ "Bobby", "87" ],
    [ "Charles", "100" ],
    [ "Eric", "64" ],
    [ "Charles", "22" ] ].

  Expected output: 87
  Explanation: The average scores are 87, 61, and 64 for Bobby, Charles, and Eric,
  respectively. 87 is the highest.
"""

""" Find the best average grade. """

# import sys.minint

def bestAverageGrade(scores):
    # TODO: implement this function
    
    if len(scores) == 0:
        return 0
    
    hash_ = {} # { name : { size: total_score } }
    
    for score in scores:
        if not hash_.get(score[0]):
            hash_[score[0]] = [score[1]]
        else:
            hash_[score[0]].append(score[1])
    
    # print(hash_)
    
    h_avg_score = -999
    
    for s_name, scores in hash_.items():
        sum_ = sum([int(score) for score in scores])
        cur_avg = sum_ // len(scores)
        h_avg_score = cur_avg if cur_avg > h_avg_score else h_avg_score
    
    return h_avg_score 

def doTestsPass():
    """ Returns true if the tests pass. Otherwise, returns false """

    testCases = [
        # example
        ([ [ "Bobby", "87" ],
            [ "Charles", "100" ],
            [ "Eric", "64" ],
            [ "Charles", "22" ] ],
         87),
        # empty
        ([],
         0),
        # multiple scores each
        ([ [ "Sarah", "91" ],
           [ "Goldie", "92" ],
           [ "Elaine", "93" ],
           [ "Elaine", "95" ],
           [ "Goldie", "94" ],
           [ "Sarah", "93" ] ],
         94),
        # negatives and zeros
        ([ [ "Janie", "-66" ],
           [ "Janie", "0" ],
           [ "Gina", "-88" ],
           [ "Bobby", "0" ],
           [ "Gina", "44" ],
           [ "Bobby", "0" ],
           [ "Bobby", "-6" ] ],
         -2),
        # same value and average
        ([ [ "Alpha", "99" ],
           [ "Bravo", "99" ],
           [ "Charlie", "99" ],
           [ "Delta", "99" ],
           [ "Echo", "99" ],
           [ "Foxtrot", "99" ],
           [ "Foxtrot", "99" ] ],
         99),
        # non-integer average
        ([ [ "Gerald", "91" ],
           [ "Gerald", "92" ] ],
         91),
        # negative non-integer average
        ([ [ "Barry", "-66" ],
           [ "Barry", "-65" ],
           [ "Alfred", "-122"] ],
         -66),
    ]

    passed = True
    for tc, expected in testCases:
        actual = bestAverageGrade(tc)
        if actual != expected:
            passed = False
            print("Failed for case ", tc, "\n  expected ", expected, ", actual ", actual)

    return passed

if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n");
    else:
        print("Tests fail\n");

