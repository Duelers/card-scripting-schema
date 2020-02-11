import typing

in_play = "in_play"
hand = "hand"
graveyard = "graveyard"

Zone = typing.Union[
    typing.Literal[in_play],
    typing.Literal[hand],
    typing.Literal[graveyard],
]
