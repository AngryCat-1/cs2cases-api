class Case():
    name = "CaseDefault"
    chance_white = 0
    chance_blue = 80
    chance_fiolet = 16
    chance_pink = 3.2
    chance_red = 0.64
    chance_gold = 0.26

    chance_startrack = 10

    drops = []
class Skin():
    name = "SkinDefault"
    rare = "blue"
    float = 1
    pattern = 0
    stattrack = False
    stattrack_can_be = True

class SkinBlueTec9(Skin):
    name = "Blue Tec9"
    rare = "blue"
class SkinBlueAK74(Skin):
    name = "Blue Ak74"
    rare = "blue"
class SkinBlueP90(Skin):
    name = "Blue P90"
    rare = "blue"
class SkinBlueAWP(Skin):
    name = "Blue AWP"
    rare = "blue"

class SkinFioletTec9(Skin):
    name = "Fiolet Tec9"
    rare = "fiolet"
class SkinFioletAK74(Skin):
    name = "Fiolet Ak74"
    rare = "fiolet"
class SkinFioletP90(Skin):
    name = "Fiolet P90"
    rare = "fiolet"
class SkinFioletAWP(Skin):
    name = "Fiolet AWP"
    rare = "fiolet"

class SkinPinkTec9(Skin):
    name = "Pink Tec9"
    rare = "pink"
class SkinPinkAK74(Skin):
    name = "Pink Ak74"
    rare = "pink"
class SkinPinkP90(Skin):
    name = "Pink P90"
    rare = "pink"
class SkinPinkAWP(Skin):
    name = "Pink AWP"
    rare = "pink"

class SkinRedTec9(Skin):
    name = "Red Tec9"
    rare = "red"
class SkinRedAK74(Skin):
    name = "Red Ak74"
    rare = "red"
class SkinRedP90(Skin):
    name = "Red P90"
    rare = "red"
class SkinRedAWP(Skin):
    name = "Red AWP"
    rare = "red"

class SkinGoldKnifeKerambit(Skin):
    name = "Gold Knife Kerambit"
    rare = "gold"
class SkinGoldKnifeButterfly(Skin):
    name = "Gold Knife Butterfly"
    rare = "gold"
class SkinGoldSportGloves(Skin):
    name = "Gold Sport Gloves"
    rare = "gold"
    stattrack_can_be = False
class SkinGoldDriverGloves(Skin):
    name = "Gold Driver Gloves"
    rare = "gold"
    stattrack_can_be = False


class CaseDangerZone(Case):
    name = "CaseDangerZone"
    drops = [SkinBlueTec9, SkinFioletAK74, SkinPinkP90, SkinRedAWP, SkinGoldKnifeKerambit]

class CaseCSGO(Case):
    name = "CaseCSGO"
    drops = [SkinBlueAK74, SkinFioletP90, SkinPinkAWP, SkinRedTec9, SkinGoldKnifeButterfly]

class CaseCS16(Case):
    name = "CaseCS16"
    drops = [SkinBlueP90, SkinFioletAWP, SkinPinkTec9, SkinRedAK74, SkinGoldSportGloves]

class CaseKilovat(Case):
    name = "CaseCS16"
    drops = [SkinBlueAWP, SkinFioletTec9, SkinPinkAK74, SkinPinkAK74, SkinRedP90, SkinGoldDriverGloves]



