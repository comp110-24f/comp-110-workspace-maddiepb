"""Examples of dictionaru syntax with Ice Cream Shop order tallies"""

# dict literals are curly brackets
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,  # comma at end is not required, but handy to have trailing comma
    # good for reformatting, and for when adding new entries
}

# sub notation adds values
ice_cream["mint"] = 3

# remove items with pop
ice_cream.pop("strawberry")

# test if key is in a dict
print("vanilla" in ice_cream)

# for...in... iterates over values in dict using the key
for flavor in ice_cream:
    count: int = ice_cream[flavor]
    print(f"{flavor}: {count}")
