def match_positional_args(*args, **kwargs):
    keyword_values = set(kwargs.values())
    return sum(1 for arg in args if arg in keyword_values)


print(match_positional_args(1, 2, 3, 4, x=1, y=2, z=3, w=5))

