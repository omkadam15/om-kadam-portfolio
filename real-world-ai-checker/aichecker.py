def evaluate_response(response):
    issues = []

    if len(response) < 10:
        issues.append("Too short - lacks detail")

    if "always" in response.lower():
        issues.append("Overgeneralization detected")

    if "maybe" in response.lower():
        issues.append("Uncertain language")

    if not issues:
        return "Good response"
    
    return f"Issues found: {', '.join(issues)}"


# Test cases
responses = [
    "Sorting always takes O(n log n)",
    "Maybe this works",
    "This is correct"
]

for r in responses:
    print(f"Response: {r}")
    print(evaluate_response(r))
    print("-" * 40)
