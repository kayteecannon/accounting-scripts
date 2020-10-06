"""Print out all the melons in our inventory."""


from melons import melons

def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for melon in melons:
    print_melon(melon, melons[melon]['seedless'], melons[melon]['price'])
