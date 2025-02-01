def deep_find(data, key):
    results = []

    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                results.append(v)
            elif isinstance(v, (dict, list)):
                results.extend(deep_find(v, key))

    elif isinstance(data, list):
        for item in data:
            results.extend(deep_find(item, key))

    return results