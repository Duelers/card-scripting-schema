import typing

import card_types
import generals
import players
import base

import zones

this = "this"
trigger = "trigger"  # The event which causes a triggered effect


class CardSelectionModel(base.BaseModel):
    from_zones: typing.Union[
        zones.Zone,
        typing.List[zones.Zone]
    ] = zones.in_play
    types: typing.Union[
        card_types.CardType,
        typing.List[card_types.CardType]
    ] = card_types.minion
    owner: typing.Optional[players.Player] = None


class ChooseCards(CardSelectionModel):
    name: typing.Literal['choose_cards']
    choose_at_least: typing.Optional[int] = 1
    choose_at_most: typing.Optional[int] = 1


class AllCards(CardSelectionModel):
    name: typing.Literal['all_cards']
    from_zones: typing.Union[
        zones.Zone,
        typing.List[zones.Zone]
    ] = zones.in_play
    types: typing.Union[
        card_types.CardType,
        typing.List[card_types.CardType]
    ] = card_types.minion
    owner: typing.Optional[players.Player] = None


class GetVarObject(base.BaseModel):
    name: typing.Literal['get_var_object']
    var: str


Object = typing.Union[
    typing.Literal[this],
    typing.Literal[trigger],
    ChooseCards,
    AllCards,
    GetVarObject,
    generals.Generals
]
