from models.explorer import Explorer


_explorers = [
    Explorer(id=1,
             name="Estevanico", 
             country="MA", 
             description="The first person of African descent to explore North America."),
    Explorer(id=2,
             name="Crispin Agnew", 
             country="GB-SCT", 
             description="The Scot explorer."),
]

def get_all() -> list[Explorer]:
    """ Return all explorers """
    return _explorers

def get_one(id: int) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == id:
            return _explorer
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorers list:
def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer

def delete(name: str) -> bool:
    """Delete an explorer; return None if it existed"""
    return None
