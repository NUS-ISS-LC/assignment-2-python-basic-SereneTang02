def find(s, n):
    index_map = {}
    for i, x in enumerate(s):
        complement = n - x
        if complement in index_map:
            return [index_map[complement], i]
        index_map[x] = i
    return []
    return None
