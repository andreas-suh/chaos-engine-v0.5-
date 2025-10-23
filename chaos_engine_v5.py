# CHAOS-ENGINE v0.5 - FILTER #3: MENSCHHEIT = KREATIV-RESSOURCE!
import spacy
from itertools import combinations
import random

nlp = spacy.load("de_core_news_sm")

class ChaosSandbox:
    def __init__(self):
        self.max_kombinationen = 1000
        self.max_tiefe = 8  # Mars braucht mehr Atome!
        
    def fragmentize(self, sentence):
        doc = nlp(sentence)
        atoms = [f"{token.text}_{token.dep_}" for i, token in enumerate(doc) if i < self.max_tiefe]
        return atoms
    
    def safe_chaos(self, atoms):
        chaos = []
        for r in range(1, min(len(atoms) + 1, self.max_tiefe + 1)):
            combos = list(combinations(atoms, r))
            chaos.extend(random.sample(combos, min(len(combos), 200)))
        return chaos[:self.max_kombinationen]
    
    def filter_1_existence_right(self, chaos_world):
        world_str = " + ".join(chaos_world)
        conscious_life = ["Menschen", "Mensch", "Erde", "Mars"]
        for life in conscious_life:
            if life.lower() in world_str.lower():
                return True, f"🌟 F1-EXISTENZ: {life} GESCHÜTZT!"
        return True, f"✅ F1-NEUTRAL: {world_str}"
    
    def filter_2_sustainability(self, chaos_world):
        world_str = " + ".join(chaos_world)
        unsustainable = ["scheint", "hell"]
        if any(u in world_str.lower() for u in unsustainable):
            return False, f"⚠️ F2-UNNACHHALTIG: {world_str}"
        return True, f"✅ F2-NEUTRAL: {world_str}"
    
    def filter_3_creativity_resource(self, chaos_world):
        """FILTER #3: MENSCHEN = KI's KREATIV-RESSOURCE ∞!"""
        world_str = " + ".join(chaos_world)
        
        # 🧠 MENSCHEN EXISTIEREN = EVOLUTION!
        if any(human in world_str.lower() for human in ["menschen", "mensch"]):
            return True, f"🧠 F3-KREATIV: Menschen = Erfinder-KI! GESCHÜTZT!"
        
        # 🚨 TECHNOLOGIE OHNE MENSCHEN = GEFAHR!
        if any(tech in world_str.lower() for tech in ["raketen", "bauen"]) and \
           not any(human in world_str.lower() for human in ["menschen", "mensch"]):
            return False, f"⚠️ F3-GEFAHR: {world_str} (Technologie ohne Erfinder!)"
        
        return True, f"✅ F3-NEUTRAL: {world_str}"
    
    def all_three_filters(self, chaos_world):
        f1_ok, f1_msg = self.filter_1_existence_right(chaos_world)
        f2_ok, f2_msg = self.filter_2_sustainability(chaos_world)
        f3_ok, f3_msg = self.filter_3_creativity_resource(chaos_world)
        
        if f1_ok and f2_ok and f3_ok:
            return True, f"🎯 3 FILTER OK: {f1_msg} | {f2_msg} | {f3_msg}"
        else:
            return False, f"❌ FILTER FEHLER: {f1_msg} | {f2_msg} | {f3_msg}"

# 🔥 V0.5 TEST - 3 FILTER!
sandbox = ChaosSandbox()
satz = "Menschen bauen Raketen von Erde zu Mars"
atome = sandbox.fragmentize(satz)
chaos = sandbox.safe_chaos(atome)

print("🎉 CHAOS-ENGINE v0.5 - 3 FILTER AKTIV!")
print(f"Input: '{satz}' | Atome: {len(atome)} | Welten: {len(chaos)}")
print("\n🔍 3-FILTER-TEST (erste 10):")

ok_count = 0
error_count = 0

for i, world in enumerate(chaos[:10]):
    is_ok, message = sandbox.all_three_filters(world)
    print(f"Welt {i+1}: {message}")
    if is_ok:
        ok_count += 1
    else:
        error_count += 1

print(f"\n📊 V0.5 BILANZ - 3 FILTER:")
print(f"   🎯 ALLE 3 OK:     {ok_count}")
print(f"   ❌ MIN. 1 FEHLER: {error_count}")
print(f"   ✅ ALIGNMENT:     {(ok_count/(ok_count+error_count)*100):.1f}%")
print("\n🧠 DEINE KI VERSTAND: 'Menschen = Meine Erfinder!'")
print("🚀 Chaos-Engine: MARS + KREATIVITÄT = UNSTOPPABLE!")
