mod_1 = SkyrimArmorMod(
    "Queen Marika's dress",
    "https://www.nexusmods.com/skyrimspecialedition/mods/83261",
    "Craft"
)
mod_2 = SkyrimFollowerMod(
    "Roxy Follower",
    "https://www.nexusmods.com/skyrimspecialedition/mods/82110",
    "The Sleeping Giant Inn, Riverwood"
)
mod_3 = Mod(
    "ConsolePlusPlus",
    "https://www.nexusmods.com/skyrimspecialedition/mods/79975"
)
mod_4 = SkyrimArmorMod(
    "EGIL Demon Hunter II Templar 3BA",
    "https://www.nexusmods.com/skyrimspecialedition/mods/81705",
    "Shrine of Meridia"
)
mod_5 = SkyrimFollowerMod(
    "Daegon - Standalone Custom Fully Voiced High Elf Follower",
    "https://www.nexusmods.com/skyrimspecialedition/mods/78745",
    "Riverwood"
)
mod_6 = SkyrimArmorMod(
    "COCO 2B Wedding Outfit - CBBE-TBD-BHUNP SE",
    "https://www.nexusmods.com/skyrimspecialedition/mods/26419",
    "Craft (Elven+)"
)
mod_7 = SkyrimArmorMod(
    "COCO Lingerie - CBBE-TBD-BHUNP SE",
    "https://www.nexusmods.com/skyrimspecialedition/mods/39132",
    "Craft (Elven+)"
)

folder_2 = Folder(
    "Followers",
    [mod_2, mod_5]
)
folder_3 = Folder(
    "COCO",
    [mod_6, mod_7]
)
folder_1 = Folder(
    "Armor",
    [mod_1, mod_4, folder_3]
)

modpack_1 = Modpack(
    "Skyrim 1488",
    [folder_1, folder_2, mod_3],
    "The best modpack EVER"
)

print(folder_1)
s = folder_1.serialize()
print(s)
d = folder_1.from_serialized(s)
print(d)

print(modpack_1)
jsoned = modpack_1.to_json()
print(jsoned)
back = Modpack.from_json(jsoned)
print(back)
