import json

# Open the JSON file saved from REST API
with open('response.json', 'r') as f:
    # Load JSON data
    data = json.load(f)

# Filter for "id" subset
subset = [d for d in data if 'id' in d]

# Count "id" in subset
count = len(subset)

# Print count
print(f"[Projects]: {count}")