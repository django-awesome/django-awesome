def uniquify(value, seen_values):
    """Adds value to seen_values set and ensures it is unique"""
    id = 1
    new_value = value
    while new_value in seen_values:
        new_value = f"{value}{id}"
        id += 1
    seen_values.add(new_value)
    return new_value
