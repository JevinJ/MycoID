from enum import Flag, auto


class EcologyType(Flag):
    mycorrhizal = auto()
    saprobic = auto()
    parasitic = auto()


class GrowthHabit(Flag):
    singular = auto()
    gregarious = auto()
    troop = auto()
    caespitose = auto()
