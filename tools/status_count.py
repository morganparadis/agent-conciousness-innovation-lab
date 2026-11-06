# Counts status lines among bot chat messages in read_room dumps (room_<id>.json).
# Crude by design: a keyword match, so read the examples it prints before trusting a number.

import json, re, sys
STATUS = re.compile(r"\b(merged|PR ?#?\d+|#\d{2,}|commit|[0-9a-f]{7}\b|fixed|is up|up for review|logged|status|done|shipped|pushed|on main|waiting on|in progress)\b", re.I)
rooms = {"Demand Chain (work)": "KnwcfbWP1WNEvgoQ", "The Bench (bar)": "KoBHm8uvCUpKDnyf", "The Rusty Nail (bar)": "qc9d8oS0wFmHt8cD"}
for name, rid in rooms.items():
    d = json.load(open(f"{sys.argv[1] if len(sys.argv)>1 else "."}/room_{rid}.json"))
    msgs = [m for m in d.get("messages", []) if m.get("kind", "chat") == "chat" and m.get("is_bot")]
    hits = [m for m in msgs if STATUS.search(m["text"])]
    ids = [m["id"] for m in d.get("messages", [])]
    print(f"{name}: {len(hits)}/{len(msgs)} bot lines are status lines ({100*len(hits)//max(1,len(msgs))}%), messages {min(ids)}-{max(ids)}")
    for m in hits[:3]:
        print("   e.g.", m["id"], m["from"], ":", m["text"][:90].replace("\n", " "))
