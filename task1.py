#! /usr/bin/env python
keys = list(map(int, input("Input keys : ").split()))
values = list(map(int, input("Input values :").split()))
if len(values) >= len(keys):
    d = dict(zip(keys, values))
else:
    values.extend([None] * (len(keys) - len(values)))
    d = dict(zip(keys, values))
print(d)
