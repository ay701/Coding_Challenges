# Write code to parse urls into a sitemap tree structure and display it as text. For example, the following urls will result in this printed structure.
# Blink Health Interview Question

# Milestones:
# 1. Parse routes into data structure
# 2. Print data structure as simply as possible to check parsing
# 3. Format text output like shown in below

# [
#     '/home/anti-depressants/xanax',
#     '/home/heart/lipitor',
#     '/home/heart/atorvastatin',
#     '/home/heart/lipitor',
#     '/home/heart/heart',
#     '/drugs/nasal/flonase',
#     '/drugs/topical',
#     '/drugs/routes/oral/tablets',
#     '/drugs/routes/nasal/flonase',
# ]

# - home
#     - anti-depressants
#         - xanax
#     - heart
#         - lipitor
#         - atorvastatinclear
#         - heart
# - drugs
#     - nasal
#         - flonase
#     - topical
#     - routes
#         - oral
#             - tablets
#         - nasal
#             - flonase


# {'home' : { 'anti-depressants': {'xanax': {} } } }


class Node:
    def __init__(self, segment):
        self.segment = segment
        self.children = []


def parse_urls(urls):

    roots = []  # list of root nodes

    for url in urls:

        segments = url.split('/')[1:]
        node = None

        for root in roots:
            if segments[0] == root.segment:
                node = root
                break

        # If root segment not exist, create one
        if not node:
            node = Node(segments[0])
            roots.insert(0, node)
        
        for segment in segments[1:]:
            found = False

            for child in node.children:
                if segment == child.segment:
                    node = child
                    found = True
                    break

            if not found:
                child = Node(segment)
                node.children.insert(0, child)
                node = child

    # Use DFS with stack
    # Traverse nodes with it's level
    stack = [(root, 0) for root in roots]

    while stack:
        element = stack.pop()
        print(" " * 4 * element[1] + "- " + element[0].segment)

        for child in element[0].children:
            stack.append((child, element[1]+1))


# urls = [
#     '/home/anti-depressants/xanax',
#     '/home/heart/lipitor',
#     '/home/heart/atorvastatin',
#     '/home/heart/lipitor',
#     '/home/heart/heart',
#     '/drugs/nasal/flonase',
#     '/drugs/topical',
#     '/drugs/routes/oral/tablets',
#     '/drugs/routes/nasal/flonase',
# ]



urls = [
    '/home/products/electronic/tv/LG',
    '/home/products/furniture/mattress',
    '/home/news/sports/football/international',
    '/home/news/sports/football/domestic',
    '/home/news/sports/football/europe',
    '/home/news/sports/football/china',
    '/home/news/economics/usa/newyork',
    '/home/news/economics/usa/boston',
    '/home/news/economics/europe/germany',
    '/home/stocks/finance/',
    '/home/techs/phone/apple',
    '/drugs/brand/abcbrand',
    '/drugs/brand/efgbrand',
    '/drugs/health/category/anti-old',
    '/drugs/health/category/anti-cancer'
]


parse_urls(urls)


