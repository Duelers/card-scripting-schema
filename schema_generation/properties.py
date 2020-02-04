from typing import Union, Literal

attack = 'attack'  # A unit's attack value.
Property = Union[
    Literal[attack]
]  # A trait something has, such as a minion's attack or a card's cost.
