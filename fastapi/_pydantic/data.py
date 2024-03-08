from model import Creature
_creature :list[Creature]=[
    Creature(name="yeti",
    country="CN",
    area="Himalayas",
    des="Hirsute Himalayan",
    aka="Abominable Snowman"
    ),
    Creature(name="sasquatch",
    country="US",
    area="*",
    des="Yeti's Cousin Eddie",
    aka="Bigfoot")]


def get_creatures()->list[Creature]:
    return _creature