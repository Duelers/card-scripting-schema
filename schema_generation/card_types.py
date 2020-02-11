import typing

minion = "minion"
general = "general"
# unit = "unit" #includes minions and generals

CardType = typing.Union[
    typing.Literal[minion],
    typing.Literal[general]
]
