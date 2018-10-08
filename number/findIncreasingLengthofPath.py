'''
Chicory Interview Question
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example: 

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

The longest increasing path is [1, 2, 6, 9] with a length of 4.
'''


class Solution(object):

    def neighbours(self, x, y):
        candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        return [(x, y) for x, y in candidates if x in range(self.r_len) and y in range(self.c_len)]
            
    def longest_increasing_path(self, matrix):
        self.matrix = matrix
        self.r_len = len(matrix)
        self.c_len = len(matrix[0])
        max_length = 0

        for x, row in enumerate(matrix):
            for y, col in enumerate(row):
                cur_length = self.findLength(x, y)
                if cur_length > max_length:
                   max_length = cur_length
        
        return max_length

    def find_length(self, x, y):
        max_length = 1
        neighbours = self.neighbours(x, y)

        for neighbor in neighbours:
            
            current_length = 0
               
            if self.matrix[neighbor[0]][neighbor[1]] > self.matrix[x][y]:
                current_length += 1 
                current_length += self.find_length(neighbor[0], neighbor[1])
                    
            if current_length > max_length:
                max_length = current_length 
                           
        return max_length               


nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

nums = [
    [1],
    [2],
    [4],
    [2]
]

#s = Solution()
#print s.longestIncreasingPath(nums)
            
def main():
    import json 
    data = '[{"name":"test1", "expected":5, "data":[[1,2,3],[4,5,6],[7,8,9]]}, {"name":"test2", "expected":5, "data":[[1,2,1,2],[4,5,2,5],[1,8,1,8],[3,6,7,9]]},{"name":"test3","expected":2,"data":[[1,2,1,2],[2,1,2,1],[1,2,1,2],[2,1,2,1]]},{"name":"test4","expected":1,"data":[[1]]},{"name":"test5","expected":3,"data":[[1],[2],[4],[2]]},{"name":"test6","expected":3,"data":[[1,2,4,2]]},{"name":"test7","expected":1,"data":[[1,1],[1,1]]},{"name":"test8","expected":6,"data":[[1,2,1,9,6],[4,5,2,5,9],[1,8,1,7,6],[3,6,7,8,0],[3,6,7,9,2]]},{"name":"test9","expected":0,"data":[[]]},{"name":"test10","expected":3,"data":[[0,9,0,0,0,0,0,0,0,0],[9,1,8,0,0,0,0,0,0,0],[0,8,2,7,0,0,0,0,0,0],[0,0,7,3,6,0,0,0,0,0],[0,0,0,6,4,5,0,0,0,0],[0,0,0,0,5,5,4,0,0,0],[0,0,0,0,0,4,6,3,0,0],[0,0,0,0,0,0,3,7,2,0],[0,0,0,0,0,0,0,2,8,1],[0,0,0,0,0,0,0,0,1,9]]}]'
    tests = json.loads(data)
    
    for test in tests:    
        name = test['name']
        data = test['data']
        expected = test['expected']

        try:
            print "Running test case ({})".format(name)
            calculated = Solution().longest_increasing_path(data)
            assert(calculated == expected)
            print "\t-> Passed: ({} == {})".format(calculated, expected)

        except AssertionError:
            print "\t-> Failed: ({} == {})".format(calculated, expected)
            pass

        finally:
            print

main()
