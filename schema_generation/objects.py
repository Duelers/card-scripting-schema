import typing

import pydantic

import card_types
import players
from base import BaseModel

import zones

this = "this"


class ChooseCards(BaseModel):
    name: typing.Literal['choose_cards']
    from_zones: typing.List[zones.Zone] = [zones.in_play]
    type: card_types.CardType = card_types.minion
    owner: typing.Optional[players.Player] = None
    choose_at_least: typing.Optional[int] = 1
    choose_at_most: typing.Optional[int] = 1


class AllCards(BaseModel):
    name: typing.Literal['all_cards']
    from_zones: typing.List[zones.Zone] = [zones.in_play]
    type: card_types.CardType = card_types.minion
    owner: typing.Optional[players.Player] = None


Object = typing.Union[
    typing.Literal[this],
    ChooseCards,
    AllCards
]
