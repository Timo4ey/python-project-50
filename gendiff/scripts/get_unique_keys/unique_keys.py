def getting_unique_keys(*args: dict) -> list:
    output = []
    filtered = list(filter(lambda x: not isinstance(x,
                                                    type | None | int), args))
    [output.append(j) for d in filtered for j in d]
    output = set(output)
    output = list(output)
    output.sort()
    return output
