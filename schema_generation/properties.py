from typing import Union, Literal

attack = 'attack'  # A unit's attack value.
max_health = 'max_health'
cur_health = 'cur_health'
Property = Union[
    Literal[attack],
    Literal[max_health],
    Literal[cur_health]
]  # A trait something has, such as a minion's attack or a card's cost.
