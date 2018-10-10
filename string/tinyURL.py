# https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/
# We need database to save the long url, and return record id
# Use record id to generate the short url
# Short url only allows to use A-Z, a-z, 0-9


def tiny_url(record_id):

    short_url = ""
    map_st = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    n = len(map_st)

    while record_id > 0:
        k = record_id % n
        short_url += map_st[k]
        record_id /= n

    short_url.reverse()

    return short_url


def short_url_to_id(short_url):

    id = 0

    for s in short_url:
        if s >= 'a' and s <= 'z':
            id = id*62 + s - a

        if s >= 'A' and s <= 'Z':
            id = id*62 + s - a + 26

        if s >= 'a' and s <= 'z':
            id = id*62 + s - a + 52

    return id


