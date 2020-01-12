from database.mappings.tag import FungusTagMapping, Tag


FungusTaste = FungusTagMapping.new_mapping('FungusTaste', fungus_id_column='fungus.id')
class Taste(Tag): pass
