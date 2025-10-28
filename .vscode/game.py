#!/usr/bin/env python3
# Dungeon Crawler RPG — single-file text adventure
# Features: map movement, stats+leveling, inventory & equipment, shop, puzzles,
# random encounters, boss fight, multiple endings, save/load (JSON).
# Python 3.8+

import json
import os
import random
import sys
import time
from typing import Dict, List, Tuple, Optional

# =========================
# Config
# =========================
SAVE_FILE = "dungeon_rpg_save.json"
FAST_MODE = True  # set to False for dramatic slow text
BASE_DELAY = 0.015 if FAST_MODE else 0.03
RANDOM_SEED = None  # set an int to make runs deterministic

# =========================
# Utilities
# =========================
def slow_print(text: str = "", delay: float = BASE_DELAY):
    for ch in text:
        print(ch, end="", flush=True)
        if delay:
            time.sleep(delay)
    print()

def ask(prompt: str = "> ") -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        slow_print("\nExiting...")
        sys.exit(0)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

# =========================
# Data Models
# =========================
class Player:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.xp = 0
        self.next_xp = 30
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 8
        self.defense = 4
        self.gold = 20
        self.inventory: Dict[str, int] = {"potion": 2}
        self.weapon: Optional[str] = None
        self.armor: Optional[str] = None
        self.flags: Dict[str, bool] = {}  # puzzle/quest flags

    # --- derived bonuses
    def weapon_bonus(self):
        return {"rusty_sword": 3, "iron_sword": 6, "dragon_slayer": 10}.get(self.weapon or "", 0)

    def armor_bonus(self):
        return {"leather_armor": 2, "iron_armor": 4, "dragon_scale": 7}.get(self.armor or "", 0)

    def atk_total(self):
        return self.attack + self.weapon_bonus()

    def def_total(self):
        return self.defense + self.armor_bonus()

    # --- leveling
    def add_xp(self, amt: int):
        self.xp += amt
        leveled = False
        while self.xp >= self.next_xp:
            self.xp -= self.next_xp
            self.level += 1
            self.next_xp = int(self.next_xp * 1.5 + 10)
            gain_hp = 12
            gain_atk = 2
            gain_def = 1
            self.max_hp += gain_hp
            self.hp = self.max_hp
            self.attack += gain_atk
            self.defense += gain_def
            leveled = True
            slow_print(f"⬆️  Level up! You are now Lv {self.level}. (+{gain_hp} HP, +{gain_atk} ATK, +{gain_def} DEF)")
        return leveled

    def to_dict(self):
        return {
            "name": self.name, "level": self.level, "xp": self.xp, "next_xp": self.next_xp,
            "max_hp": self.max_hp, "hp": self.hp, "attack": self.attack, "defense": self.defense,
            "gold": self.gold, "inventory": self.inventory, "weapon": self.weapon,
            "armor": self.armor, "flags": self.flags
        }

    @classmethod
    def from_dict(cls, d):
        p = cls(d["name"])
        p.level = d["level"]; p.xp = d["xp"]; p.next_xp = d["next_xp"]
        p.max_hp = d["max_hp"]; p.hp = d["hp"]
        p.attack = d["attack"]; p.defense = d["defense"]
        p.gold = d["gold"]; p.inventory = d["inventory"]
        p.weapon = d["weapon"]; p.armor = d["armor"]; p.flags = d["flags"]
        return p

# =========================
# World / Map
# =========================
# Coordinates (x, y). (0,0) is the Start Room. Boss at (2,2).
# Some rooms are special: shop, riddle, chest (locked), forge, exit (boss).

ROOMS: Dict[Tuple[int,int], Dict] = {
    (0, 0): {"name": "Start Cell", "desc": "A damp cell with mossy stones and a flickering torch.",
             "items": [], "exits": {"e": (1,0), "s": (0,-1)}, "type": "start"},
    (1, 0): {"name": "Hall of Echoes", "desc": "Whispers bounce from wall to wall.",
             "items": [], "exits": {"w": (0,0), "e": (2,0), "s": (1,-1)}, "type": "hall"},
    (2, 0): {"name": "Riddle Chamber", "desc": "A tablet inscribed with ancient text hums softly.",
             "items": [], "exits": {"w": (1,0), "s": (2,-1)}, "type": "riddle"},
    (0, -1): {"name": "Goblin Den", "desc": "Bones and scraps litter the ground.",
              "items": ["rusty_sword"], "exits": {"n": (0,0), "e": (1,-1)}, "type": "combat"},
    (1, -1): {"name": "Underground Market", "desc": "A hooded merchant eyes you from a stall.",
              "items": [], "exits": {"w": (0,-1), "n": (1,0), "e": (2,-1)}, "type": "shop"},
    (2, -1): {"name": "Locked Vault", "desc": "A heavy chest bound with runes sits here.",
              "items": ["crown"], "exits": {"w": (1,-1), "n": (2,0), "e": (3,-1)}, "type": "chest", "locked": True},
    (3, -1): {"name": "Forgotten Forge", "desc": "Embers glow in an ancient forge.",
              "items": [], "exits": {"w": (2,-1), "n": (3,0)}, "type": "forge"},
    (3, 0): {"name": "Armory", "desc": "Racks of dented armor line the walls.",
             "items": ["leather_armor"], "exits": {"s": (3,-1), "w": (2,0), "n": (3,1)}, "type": "loot"},
    (3, 1): {"name": "Dragon Antechamber", "desc": "The air vibrates with heat.",
             "items": [], "exits": {"s": (3,0), "w": (2,1), "n": (3,2)}, "type": "danger"},
    (2, 1): {"name": "Crystal Grotto", "desc": "Crystals pulse with a soothing light.",
             "items": ["potion"], "exits": {"e": (3,1), "n": (2,2)}, "type": "heal"},
    (2, 2): {"name": "Dragon’s Lair", "desc": "The great Dragon coils atop a mountain of gold.",
             "items": [], "exits": {"s": (2,1), "w": (1,2)}, "type": "boss"},
    (1, 2): {"name": "Sunlit Stair", "desc": "A stairway leading to daylight — freedom lies beyond.",
             "items": [], "exits": {"e": (2,2)}, "type": "exit"}
}

DIRECTIONS = {
    "n": (0, 1), "north": (0, 1),
    "s": (0,-1), "south": (0,-1),
    "e": (1, 0), "east":  (1, 0),
    "w": (-1,0), "west":  (-1,0)
}

# =========================
# Game State
# =========================
class Game:
    def __init__(self, player: Player, pos=(0,0)):
        self.player = player
        self.pos = pos
        self.seen: set = {pos}  # for map rendering

    # ----- save/load -----
    def to_dict(self):
        return {"player": self.player.to_dict(), "pos": self.pos, "seen": list(self.seen)}

    @classmethod
    def from_dict(cls, d):
        g = cls(Player.from_dict(d["player"]), tuple(d["pos"]))
        g.seen = set(map(tuple, d.get("seen", [])))
        return g

# =========================
# Persistence
# =========================
def save_game(game: Game):
    with open(SAVE_FILE, "w") as f:
        json.dump(game.to_dict(), f, indent=2)
    slow_print("💾 Game saved.")

def load_game() -> Optional[Game]:
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)
    return Game.from_dict(data)

# =========================
# Combat System
# =========================
ENEMIES = [
    {"name": "Goblin", "hp": (28, 36), "atk": (6, 9), "def": (2, 3), "gold": (8, 16), "xp": 14},
    {"name": "Skeleton", "hp": (32, 40), "atk": (7, 11), "def": (3, 4), "gold": (10, 18), "xp": 16},
    {"name": "Fire Imp", "hp": (24, 32), "atk": (8, 12), "def": (1, 2), "gold": (12, 20), "xp": 18}
]
BOSS = {"name": "Ancient Dragon", "hp": 150, "atk": 18, "def": 8, "gold": 120, "xp": 60}

def roll(low, high):
    return random.randint(low, high)

def encounter_enemy(name=None):
    e = None
    if name:
        e = next((x for x in ENEMIES if x["name"] == name), None)
    if e is None:
        e = random.choice(ENEMIES)
    enemy = {
        "name": e["name"],
        "hp": roll(*e["hp"]),
        "atk": roll(*e["atk"]),
        "def": roll(*e["def"]),
        "gold": roll(*e["gold"]),
        "xp": e["xp"]
    }
    return enemy

def battle(game: Game, enemy: Dict, can_flee=True) -> bool:
    p = game.player
    slow_print(f"\n⚔️  A {enemy['name']} appears!")
    while enemy["hp"] > 0 and p.hp > 0:
        slow_print(f"Your HP {p.hp}/{p.max_hp} | {enemy['name']} HP {enemy['hp']}")
        slow_print("Choose: [attack] [use <item>] [equip <item>] " + ("[flee]" if can_flee else ""))
        cmd = ask("> ").lower()

        if cmd.startswith("use "):
            item = cmd[4:].strip()
            if not use_item(p, item):
                continue
        elif cmd.startswith("equip "):
            item = cmd[6:].strip()
            equip_item(p, item)
        elif cmd in ("flee", "run") and can_flee:
            if random.random() < 0.55:
                slow_print("You fled successfully!")
                return False
            else:
                slow_print("You failed to escape!")
        else:
            # attack
            dmg = clamp(p.atk_total() + roll(-2, 4) - enemy["def"], 0, 999)
            enemy["hp"] -= dmg
            slow_print(f"You hit the {enemy['name']} for {dmg} damage.")

        if enemy["hp"] <= 0:
            break

        # enemy turn
        edmg = clamp(enemy["atk"] + roll(-2, 3) - p.def_total(), 0, 999)
        p.hp -= edmg
        slow_print(f"The {enemy['name']} hits you for {edmg} damage.")
        if p.hp <= 0:
            break

    if p.hp <= 0:
        slow_print("💀 You fall in battle...")
        return True  # dead
    slow_print(f"🏆 You defeated the {enemy['name']}! +{enemy['gold']} gold, +{enemy['xp']} XP.")
    p.gold += enemy["gold"]
    leveled = p.add_xp(enemy["xp"])
    if leveled:
        slow_print("You feel stronger!")
    return False  # alive

# =========================
# Items & Equipment
# =========================
SHOP_STOCK = {
    "potion": {"price": 20, "desc": "Heals 40 HP when used."},
    "iron_sword": {"price": 75, "desc": "+6 ATK (weapon)"},
    "iron_armor": {"price": 75, "desc": "+4 DEF (armor)"},
    "antidote": {"price": 15, "desc": "Cures poison (reserved for future)."},
}

def add_item(p: Player, name: str, qty: int = 1):
    p.inventory[name] = p.inventory.get(name, 0) + qty

def has_item(p: Player, name: str, qty: int = 1):
    return p.inventory.get(name, 0) >= qty

def remove_item(p: Player, name: str, qty: int = 1):
    if has_item(p, name, qty):
        p.inventory[name] -= qty
        if p.inventory[name] <= 0:
            del p.inventory[name]
        return True
    return False

def use_item(p: Player, item: str) -> bool:
    if not has_item(p, item):
        slow_print("You don't have that item.")
        return False
    if item == "potion":
        healed = 40
        old = p.hp
        p.hp = clamp(p.hp + healed, 0, p.max_hp)
        remove_item(p, "potion", 1)
        slow_print(f"You drink a potion and recover {p.hp - old} HP.")
        return True
    elif item == "vault_key":
        slow_print("Best used at a locked chest.")
        return False
    elif item == "crown":
        slow_print("It sparkles regally. Maybe wear it to the exit...")
        return False
    else:
        slow_print("You can't use that right now.")
        return False

def equip_item(p: Player, item: str):
    if not has_item(p, item):
        slow_print("You don't have that item.")
        return
    # weapon
    if item in ("rusty_sword", "iron_sword", "dragon_slayer"):
        p.weapon = item
        slow_print(f"You equipped {item.replace('_',' ')}. ATK total: {p.atk_total()}")
    # armor
    elif item in ("leather_armor", "iron_armor", "dragon_scale"):
        p.armor = item
        slow_print(f"You equipped {item.replace('_',' ')}. DEF total: {p.def_total()}")
    else:
        slow_print("That can't be equipped.")

# =========================
# Room Interactions
# =========================
def enter_room(game: Game):
    p = game.player
    room = ROOMS[game.pos]
    game.seen.add(game.pos)
    slow_print(f"\n📍 {room['name']} — {room['desc']}")

    # First-time loot pickups lying on the ground
    if room.get("items"):
        for it in list(room["items"]):
            # don't auto-pick rare items like crown; only auto-pick basics
            if it in ("rusty_sword", "leather_armor", "potion"):
                add_item(p, it, 1)
                room["items"].remove(it)
                slow_print(f"You found a {it.replace('_',' ')}.")
        # For non-auto items, tell player
        if room.get("items"):
            slow_print(f"You see: {', '.join(room['items'])}. Try 'take <item>'.")

    # Special room effects
    t = room.get("type")
    if t == "combat":
        # One guaranteed encounter first time
        if not p.flags.get(f"cleared_{game.pos}", False):
            dead = battle(game, encounter_enemy("Goblin"))
            p.flags[f"cleared_{game.pos}"] = True
            if dead:
                return "dead"
    elif t == "heal":
        healed = min(20, p.max_hp - p.hp)
        if healed > 0:
            p.hp += healed
            slow_print(f"The crystals mend you for {healed} HP.")
    elif t == "riddle":
        if not p.flags.get("riddle_solved"):
            solve_riddle(game)
    elif t == "chest":
        open_vault(game)
    elif t == "forge":
        use_forge(game)
    elif t == "shop":
        slow_print("The merchant rasps: 'Type shop to browse my wares.'")
    elif t == "boss":
        # Fight only if dragon not defeated
        if not p.flags.get("dragon_down"):
            fight_boss(game)
            if p.hp <= 0:
                return "dead"
    elif t == "exit":
        try_exit(game)

    # Random encounter chance on entry (except safe rooms)
    if t not in ("shop", "heal", "riddle", "chest", "forge", "exit"):
        if random.random() < 0.22 and p.hp > 0 and not p.flags.get("dragon_down"):
            dead = battle(game, encounter_enemy(), can_flee=True)
            if dead:
                return "dead"
    return "ok"

def solve_riddle(game: Game):
    p = game.player
    slow_print("An inscription glows:\n'I speak without a mouth and hear without ears. I have no body, but I come alive with wind.'")
    slow_print("Answer?")
    ans = ask("> ").lower()
    if "echo" in ans:
        slow_print("Stone grinds aside revealing a small key.")
        add_item(p, "vault_key", 1)
        p.flags["riddle_solved"] = True
    else:
        slow_print("The glow fades. Perhaps another time.")

def open_vault(game: Game):
    p = game.player
    room = ROOMS[game.pos]
    locked = room.get("locked", False)
    if locked:
        if has_item(p, "vault_key"):
            slow_print("You turn the key; the runes dim and the chest opens.")
            remove_item(p, "vault_key", 1)
            room["locked"] = False
        else:
            slow_print("The vault is sealed by magic. You need a key.")
            return
    # loot
    if "crown" in room.get("items", []):
        slow_print("Inside rests a golden crown fit for a ruler.")
        slow_print("Take it? (yes/no)")
        if ask("> ").lower().startswith("y"):
            add_item(p, "crown", 1)
            room["items"].remove("crown")
            slow_print("You take the crown. It glitters in the torchlight.")
        else:
            slow_print("You leave the crown for now.")
    else:
        slow_print("The vault is empty.")

def use_forge(game: Game):
    p = game.player
    slow_print("The forge master whispers: 'Bring me proof of flame, and I shall craft a blade.'")
    # If dragon down → craft dragon_slayer & dragon_scale if not yet
    if p.flags.get("dragon_down") and not p.flags.get("crafted_rewards"):
        slow_print("The scent of ash lingers upon you. The master nods.")
        add_item(p, "dragon_slayer", 1)
        add_item(p, "dragon_scale", 1)
        p.flags["crafted_rewards"] = True
        slow_print("You receive: Dragon Slayer (weapon) and Dragon Scale (armor). Equip them.")
    else:
        slow_print("For now, the embers wait.")

def fight_boss(game: Game):
    p = game.player
    slow_print("🔥 The Ancient Dragon awakens!")
    # If crown equipped before boss? (no special effect in combat)
    enemy = {"name": BOSS["name"], "hp": BOSS["hp"], "atk": BOSS["atk"], "def": BOSS["def"], "gold": BOSS["gold"], "xp": BOSS["xp"]}
    dead = battle(game, enemy, can_flee=False)
    if not dead:
        slow_print("The Dragon collapses. The lair grows quiet.")
        p.flags["dragon_down"] = True
        p.gold += 80
        slow_print("You gather an extra 80 gold from the hoard.")
    # After defeating dragon, pathway to exit (1,2) is thematically justified

def try_exit(game: Game):
    p = game.player
    if not p.flags.get("dragon_down"):
        slow_print("A roaring presence prevents your passage. Something powerful blocks the way.")
        return
    # Endings
    if has_item(p, "crown"):
        slow_print("👑 You emerge wearing the golden crown. The people kneel. You are proclaimed ruler.")
        game_over(win="king")
    elif p.gold >= 150:
        slow_print("💰 You stride into the sun, pockets heavy with gold. A life of comfort awaits.")
        game_over(win="rich")
    else:
        slow_print("🌤️ You breathe free air once more — battered, but alive. A new chapter begins.")
        game_over(win="alive")

# =========================
# Shop
# =========================
def handle_shop(game: Game):
    p = game.player
    slow_print("Merchant: 'Welcome. Type: buy <item>, sell <item>, list, leave'")
    while True:
        cmd = ask("(shop)> ").lower()
        if cmd in ("leave", "exit", "back"):
            slow_print("'May fortune follow, traveler.'")
            break
        elif cmd in ("list", "ls"):
            slow_print("For sale:")
            for k, v in SHOP_STOCK.items():
                slow_print(f" - {k} ({v['price']}g): {v['desc']}")
            slow_print(f"Your gold: {p.gold}")
        elif cmd.startswith("buy "):
            item = cmd[4:].strip()
            if item not in SHOP_STOCK:
                slow_print("Not in stock.")
                continue
            price = SHOP_STOCK[item]["price"]
            if p.gold < price:
                slow_print("You can't afford that.")
                continue
            p.gold -= price
            add_item(p, item, 1)
            slow_print(f"You bought {item}.")
        elif cmd.startswith("sell "):
            item = cmd[5:].strip()
            if not has_item(p, item):
                slow_print("You don't have that.")
                continue
            value = 0
            # simple sell values
            if item in ("rusty_sword", "leather_armor"): value = 10
            elif item in ("iron_sword", "iron_armor"): value = 35
            elif item == "potion": value = 8
            elif item == "crown": value = 0  # cannot sell crown
            elif item in ("dragon_slayer", "dragon_scale"): value = 120
            else: value = 5
            remove_item(p, item, 1)
            p.gold += value
            slow_print(f"Sold {item} for {value} gold.")
        else:
            slow_print("Commands: buy <item>, sell <item>, list, leave")

# =========================
# Movement & Commands
# =========================
def move(game: Game, direction: str):
    room = ROOMS.get(game.pos)
    if not room:
        slow_print("You are lost in the void. (Bug?)")
        return
    exits = room.get("exits", {})
    dkey = None
    if direction in exits: dkey = direction
    elif direction in DIRECTIONS:
        # convert full words to n/s/e/w
        short = [k for k in exits if DIRECTIONS.get(k) == DIRECTIONS[direction]]
        if short: dkey = short[0]
    if not dkey:
        slow_print("You can't go that way.")
        return
    game.pos = exits[dkey]
    enter_room(game)

def take_item(game: Game, item: str):
    room = ROOMS[game.pos]
    if item not in room.get("items", []):
        slow_print("No such item here.")
        return
    add_item(game.player, item, 1)
    room["items"].remove(item)
    slow_print(f"You take the {item.replace('_',' ')}.")

def show_inventory(p: Player):
    if not p.inventory:
        slow_print("Inventory is empty.")
        return
    slow_print("🎒 Inventory:")
    for k, v in p.inventory.items():
        slow_print(f" - {k} x{v}")
    if p.weapon: slow_print(f"Weapon: {p.weapon} (+{p.weapon_bonus()} ATK)")
    if p.armor:  slow_print(f"Armor:  {p.armor} (+{p.armor_bonus()} DEF)")

def show_stats(p: Player):
    slow_print(f"{p.name} — Lv {p.level}  HP {p.hp}/{p.max_hp}  ATK {p.atk_total()}  DEF {p.def_total()}")
    slow_print(f"XP {p.xp}/{p.next_xp}  Gold {p.gold}")

def show_help():
    slow_print(
        "Commands:\n"
        "  move/go <n|s|e|w|north|south|east|west>\n"
        "  look / examine          — re-describe the room\n"
        "  take <item>             — pick up an item in the room\n"
        "  use <item>              — use an item (potion, etc.)\n"
        "  equip <item>            — equip a weapon/armor\n"
        "  inv / inventory         — show inventory\n"
        "  stats                   — show stats\n"
        "  shop                    — open shop (in market room)\n"
        "  save / load             — save or load your game\n"
        "  map                     — show explored map\n"
        "  help                    — this help\n"
        "  quit / exit             — leave game"
    )

def render_map(game: Game):
    # Render small bounding box around explored area
    xs = [x for x,y in game.seen]
    ys = [y for x,y in game.seen]
    xs += [game.pos[0]]; ys += [game.pos[1]]
    mnx, mxx = min(xs)-1, max(xs)+1
    mny, mxy = min(ys)-1, max(ys)+1
    for y in range(mxy, mny-1, -1):
        row = []
        for x in range(mnx, mxx+1):
            if (x,y) == game.pos:
                row.append(" @ ")
            elif (x,y) in game.seen:
                row.append(" . ")
            else:
                row.append("   ")
        slow_print("".join(row))

def handle_command(game: Game, raw: str):
    p = game.player
    if not raw:
        return
    parts = raw.split()
    cmd = parts[0].lower()
    arg = " ".join(parts[1:]).strip()

    # movement aliases
    if cmd in ("n","s","e","w","north","south","east","west"):
        move(game, cmd)
        return
    if cmd in ("move","go") and arg:
        move(game, arg)
        return

    if cmd in ("look","examine"):
        enter_room(game); return
    if cmd in ("take","get","grab") and arg:
        take_item(game, arg); return
    if cmd == "use" and arg:
        use_item(p, arg); return
    if cmd == "equip" and arg:
        equip_item(p, arg); return
    if cmd in ("inv","inventory"):
        show_inventory(p); return
    if cmd == "stats":
        show_stats(p); return
    if cmd == "shop":
        if ROOMS[game.pos].get("type") == "shop":
            handle_shop(game)
        else:
            slow_print("No merchant here.")
        return
    if cmd == "save":
        save_game(game); return
    if cmd == "load":
        g2 = load_game()
        if g2:
            game.player = g2.player
            game.pos = g2.pos
            game.seen = g2.seen
            slow_print("✅ Loaded.")
            enter_room(game)
        else:
            slow_print("No save found.")
        return
    if cmd == "map":
        render_map(game); return
    if cmd == "help":
        show_help(); return
    if cmd in ("quit","exit"):
        slow_print("Goodbye, adventurer.")
        sys.exit(0)

    slow_print("Unknown command. Type 'help' for options.")

# =========================
# Game Loop
# =========================
def intro():
    slow_print("🏰 Welcome to Dungeon Crawler RPG")
    slow_print("Escape the depths, if you can...")

def new_or_load() -> Game:
    g = load_game()
    if g:
        slow_print("Found a previous journey. Loading it now.")
        enter_room(g)
        return g
    name = ask("Your hero's name: ").strip() or "Hero"
    p = Player(name)
    if RANDOM_SEED is not None:
        random.seed(RANDOM_SEED)
    g = Game(p, pos=(0,0))
    enter_room(g)
    return g

def game_over(win: Optional[str] = None):
    if win == "king":
        slow_print("\n✨ YOU WIN — The Crowned Ending ✨")
    elif win == "rich":
        slow_print("\n✨ YOU WIN — The Wealthy Ending ✨")
    elif win == "alive":
        slow_print("\n✨ YOU WIN — The Survivor Ending ✨")
    else:
        slow_print("\n☠️  GAME OVER")
    # Offer replay
    slow_print("Play again? (yes/no)")
    if ask("> ").lower().startswith("y"):
        if os.path.exists(SAVE_FILE):
            try:
                os.remove(SAVE_FILE)
            except Exception:
                pass
        main()
    else:
        sys.exit(0)

def main():
    intro()
    game = new_or_load()
    show_help()
    while True:
        if game.player.hp <= 0:
            game_over()
        cmd = ask("> ")
        result = handle_command(game, cmd)

if __name__ == "__main__":
    main()