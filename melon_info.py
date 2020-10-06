"""Print out all the melons in our inventory."""


from melons import melons

def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon, attributes in melons.items():
        print(melon)

        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

        print("\n")

print_all_melons(melons)