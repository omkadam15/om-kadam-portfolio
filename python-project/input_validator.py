def validate_input(value):
    if value is None:
        return "Invalid: None value"

    if not isinstance(value, (int, float)):
        return "Invalid: Not a number"

    if value < 0:
        return "Invalid: Negative value not allowed"

    return "Valid input"

test_values = [10, -5, None, "abc"]

for val in test_values:
    print(f"Input: {val} → {validate_input(val)}")
