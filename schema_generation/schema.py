from pydantic import BaseModel

from schema_generation import properties, effects, events


class TriggeredEffect(BaseModel):
    trigger: events.Event
    effect: effects.Effect

    class Config:
        arbitrary_types_allowed = True


if __name__ == '__main__':
    primus_fist_etb = TriggeredEffect(
        trigger=events.Summon(),
        effect=effects.ChangeProperty(
            property=properties.attack,
            operator='+',
            by_value=2
        )
    )

    print(TriggeredEffect.schema_json(indent=4))

    print('')

    primus_fist_test_json_4 = {
        "trigger": "summon",
        "effect": {
            "name": "change_property",
            "property_owner": {
                "name": "choose_cards",
                "from": "in_play",
                "type": "minion"
            },
            "property": "attack",
            "operator": "+",
            "change_by": 2,
            "until": {
                "name": "end_of_#_turns",
                "num_turns": 2
            }
        }
    }

    """Primus Fist Card Abilities
        Real
            Trigger = Summon
            Effect
                Change Property
                    Property Owner =
                        Choose Cards
                            From =
                                In Play
                    Property =
                        "Power"
                    Operator = 
                        "+"
                    Change Value = 
                        2
                    Until
                        End of # turns"""
