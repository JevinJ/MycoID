from database.mappings.tag import FungusTagMapping, Tag


FungusOdor = FungusTagMapping.new_mapping('FungusOdor', fungus_id_column='fungus.id')
class Odor(Tag): pass