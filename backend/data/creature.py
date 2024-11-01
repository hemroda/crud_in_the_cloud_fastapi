from models.creature import Creature


_creatures = [
    Creature(name="Aigamuxa",
             aka="Bushmen",
             country="ZA",
             area="South Africa",
             description="The monster is said to have eyes on its feet, meaning that it cannot see the humans it preys upon as it hunts. In order to see, it must stand on its hands or head, or lie in the sand."),
    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch"),
    ]


def get_all() -> list[Creature]:
    """ Return all Creatures """
    return _creatures

def get_one(id: int) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == id:
            return _creature
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add an creature"""
    return creature

def modify(creature: Creature) -> Creature:
    """Partially modify an creature"""
    return creature

def replace(creature: Creature) -> Creature:
    """Completely replace an creature"""
    return creature

def delete(name: str) -> bool:
    """Delete an creature; return None if it existed"""
    return None
