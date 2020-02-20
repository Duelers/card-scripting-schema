import dataclasses
import typing

import inflection
import pydantic

import objects
import properties


@dataclasses.dataclass
class ObjectType:
    type: str
    object: typing.Type
    property: typing.Type


UnitType = ObjectType(type='unit',
                      object=objects.Unit,
                      property=properties.UnitProperty)

MinionType = ObjectType(type='minion',
                        object=objects.Minion,
                        property=properties.MinionProperty)

SpellType = ObjectType(type='spell',
                       object=objects.Spell,
                       property=properties.SpellProperty)

ArtifactType = ObjectType(type='artifact',
                          object=objects.Artifact,
                          property=properties.ArtifactProperty)

"""
any
    unit
        minion
        general
    spell
    artifact
    ability
    effect
    event


"""


def make_typed_model(obj_type: ObjectType, name: str, **keys):
    snake_name = inflection.underscore((name))
    model = pydantic.create_model(
        model_name=name,
        name=(typing.Literal[snake_name], ...),
        type=(typing.Literal[obj_type.type], obj_type.type),
        **keys,
    )
    return model
