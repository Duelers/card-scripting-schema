import typing

import pydantic

from card_models import card_types
from card_models import factions
from card_models import base
from card_models import abilities as _abilities
from card_models import effects as _effects


class CardModel(base.BaseModel):
    name: str
    faction: factions.Faction = factions.neutral


class Castable(pydantic.BaseModel):
    cost: pydantic.conint(ge=0)


class Unit(CardModel):
    attack: pydantic.conint(ge=0)
    max_health: pydantic.conint(ge=0)

    current_health: typing.Optional[int] = None
    # Can technically be negative at times. Relevant when taking damage and then healing in response.
    # None while off the board. Set to max_health when etb.


class GeneralCard(Unit):
    type: typing.Literal[card_types.general] = card_types.general


class MinionCard(Unit, Castable):
    type: typing.Literal[card_types.minion] = card_types.minion
    tribes: typing.List[str] = []
    abilities: typing.Union[
        _abilities.Ability,
        typing.List[_abilities.Ability]
    ]


class SpellCard(CardModel, Castable):
    type: typing.Literal[card_types.spell] = card_types.spell
    effects: typing.Union[
        _effects.Effect,
        typing.List[_effects.Effect]
    ]


class ArtifactCard(CardModel, Castable):
    type: typing.Literal[card_types.artifact] = card_types.artifact
    abilities: typing.Union[
        _abilities.Ability,
        typing.List[_abilities.Ability]
    ]


Card = typing.Union[SpellCard, MinionCard, ArtifactCard]


class CardRoot(base.BaseModel):
    __root__: typing.Union[Card]
