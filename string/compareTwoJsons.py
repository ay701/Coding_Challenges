from collections import defaultdict
import json


class Solution:

    def __init__(self, json_1, json_2):
        self.json_1 = json_1
        self.json_2 = json_2
        self.elements = defaultdict(int)

    def compare_two_jsons(self):

        arr_1 = json.loads(self.json_1)
        arr_2 = json.loads(self.json_2)

        for element in arr_1:
            self.parse(element)

        for element in arr_2:
            self.parse(element)

        return [key for key, val in self.elements.iteritems() if val == 1]

    def parse(self, element):
        if type(element) is not list:
            self.elements[element] += 1
        else:
            for e in element:
                self.parse_list(e)


json_1 = '{ "name":"John", "age":30, "city":"New York"}'
json_2 = '{ "name":"John", "age":30, "city":"New York", "state":"New York State"}'

s = Solution(json_1, json_2)
print(s.compare_two_jsons())
