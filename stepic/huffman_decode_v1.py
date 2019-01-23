k, length = map(int, input().split(" "))
d = []
for i in range(k):
    local = {}
    letter, code = map(str, input().split(": "))
    local[letter] = code
    d.append(local)
encode = input()
print(d)


def decode(_dict, _code):
    for j in reversed(_dict):
        for item in j:
            _code = _code.replace(j[item], item)
            _dict.remove(j)
            if len(_dict) > 0:
                decode(_dict, _code)
            else:
                print(_code)
                return _code


decode(d, encode)





