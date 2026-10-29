# Sector map of Torvane's Mart, day 36 ~0600 (end of day 35). The Light's knowledge only. North up, schematic (not to scale).
import sys, math, random
out = sys.argv[1]
random.seed(31)
W, H = 1600, 1080

# --- the rock: an irregular elongated blob, long axis north-south
def blob(cx, cy, rx, ry, n=90, jitter=0.07, seed=0):
    rnd = random.Random(seed)
    pts = []
    offs = [rnd.uniform(-jitter, jitter) for _ in range(12)]
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1 + sum(offs[j] * math.sin((j + 2) * a + j) for j in range(12)) / 3
        # pinch the waist slightly
        k *= 1 - 0.06 * math.cos(2 * a) ** 2 * (1 if abs(math.sin(a)) < 0.5 else 0)
        pts.append((cx + rx * k * math.sin(a), cy - ry * k * math.cos(a)))
    return pts
rock = blob(800, 560, 360, 470, seed=4)
rock_d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in rock) + ' Z'

# stars
stars = ''.join(f'<circle cx="{random.uniform(0,W):.0f}" cy="{random.uniform(0,H):.0f}" r="{random.uniform(0.4,1.4):.1f}" fill="#fff" opacity="{random.uniform(0.15,0.6):.2f}"/>' for _ in range(260))

# craters / surface noise inside the rock (clipped)
surf = ''
for _ in range(70):
    x, y = random.uniform(460, 1140), random.uniform(110, 1010)
    r = random.uniform(6, 26)
    surf += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="#000" opacity="{random.uniform(0.12,0.25):.2f}"/><circle cx="{x-r*0.25:.0f}" cy="{y-r*0.25:.0f}" r="{r*0.8:.0f}" fill="none" stroke="#6a625a" stroke-opacity="0.25" stroke-width="1.5"/>'

# --- districts
# high side (north): domes, trade halls, the Spire
high = ''
for (x, y, r) in [(700, 215, 30), (905, 225, 26), (760, 270, 22), (860, 280, 20), (650, 280, 18), (950, 290, 16)]:
    high += f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#dome)" stroke="#9fb0bd" stroke-opacity="0.5" stroke-width="1.5"/>'
# the Spire: a tall tower seen from above (stepped octagon)
def octa(cx, cy, r):
    return ' '.join(f'{cx + r*math.cos(math.pi/8 + i*math.pi/4):.1f},{cy + r*math.sin(math.pi/8 + i*math.pi/4):.1f}' for i in range(8))
high += f'<polygon points="{octa(800,150,44)}" fill="#4a4f55" stroke="#c9d2d8" stroke-width="2.5"/>'
high += f'<polygon points="{octa(800,150,28)}" fill="#5f666d" stroke="#c9d2d8" stroke-width="1.5"/>'
high += f'<polygon points="{octa(800,150,12)}" fill="#e8d9a8"/>'
# the pad on its east flank
high += f'<circle cx="868" cy="170" r="20" fill="#2e3338" stroke="#c9d2d8" stroke-width="2"/><line x1="842" y1="162" x2="850" y2="165" stroke="#c9d2d8" stroke-width="5"/>'
# trade halls (long blocks)
for (x, y, w, h) in [(690, 205, 0, 0)]:
    pass
for (x, y, w, h, rot) in [(735, 205, 70, 18, -8), (830, 210, 60, 16, 6), (705, 240, 50, 14, 0), (880, 250, 46, 14, -4)]:
    high += f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" fill="#3a3530" stroke="#8a7e6e" stroke-opacity="0.7" stroke-width="1.2" transform="rotate({rot} {x} {y})"/>'

# central ridge: a darker spine with contour lines
ridge = ''
for k in range(5):
    w = 60 - k * 11
    ridge += f'<ellipse cx="800" cy="440" rx="{w}" ry="{120 - k*18}" fill="none" stroke="#7a7068" stroke-opacity="{0.18 + k*0.06:.2f}" stroke-width="1.5"/>'
ridge += '<ellipse cx="800" cy="440" rx="58" ry="118" fill="#000" opacity="0.18"/>'
# the vox mast: lattice tower icon
ridge += '<g transform="translate(800 440)"><circle r="16" fill="#2a2e32" stroke="#c9d2d8" stroke-width="2"/><path d="M-9,-9 L9,9 M9,-9 L-9,9 M0,-13 L0,13 M-13,0 L13,0" stroke="#c9d2d8" stroke-width="1.6"/><circle r="4" fill="#ff5a4a"/></g>'
# the ridge road: switchbacks down the east face to the ring
ridge += '<path d="M812,452 L838,462 L826,474 L852,484 L840,496 L868,506 L888,516" fill="none" stroke="#b9a98f" stroke-width="2.5" stroke-dasharray="5 3" opacity="0.85"/>'
# the old maintenance stair, west face
ridge += '<path d="M788,452 L770,462 L782,472 L762,484" fill="none" stroke="#b9a98f" stroke-width="1.6" stroke-dasharray="2 3" opacity="0.6"/>'

# dock ring: a band across the waist with piers on both edges
ring = ''
ring += '<path d="M455,520 C600,505 1000,505 1145,520 L1150,600 C1000,616 600,616 450,600 Z" fill="url(#ringplate)" stroke="#9aa6ae" stroke-opacity="0.55" stroke-width="2"/>'
# piers off both edges
for y in range(526, 600, 13):
    ring += f'<rect x="{392 + (y % 3)*4}" y="{y}" width="{64 - (y % 2)*10}" height="5" fill="#6d757c"/>'
    ring += f'<rect x="{1146}" y="{y}" width="{60 + (y % 2)*12}" height="5" fill="#6d757c"/>'
# cranes on the east ring (Hookmen turf)
for (x, y) in [(1040, 528), (1080, 590), (1110, 540), (1015, 595), (1125, 580)]:
    ring += f'<g transform="translate({x} {y})"><rect x="-4" y="-4" width="8" height="8" fill="#c8a24a"/><line x1="0" y1="0" x2="22" y2="-14" stroke="#c8a24a" stroke-width="2.5"/><line x1="22" y1="-14" x2="22" y2="-4" stroke="#c8a24a" stroke-width="1"/></g>'
# buildings on the ring (small blocks)
for _ in range(60):
    x = random.uniform(470, 1130); y = random.uniform(522, 598)
    if abs(x - 905) < 70 and y > 560: continue
    ring += f'<rect x="{x:.0f}" y="{y:.0f}" width="{random.uniform(8,20):.0f}" height="{random.uniform(6,12):.0f}" fill="#2c2f33" stroke="#4a5056" stroke-width="0.8"/>'

# scrubber hall (underground: dashed outline) with valve house and gate
scrub = '<rect x="855" y="565" width="110" height="60" rx="10" fill="#1d6a6a" fill-opacity="0.22" stroke="#5ad1c8" stroke-width="2.5" stroke-dasharray="7 4"/>'
for k in range(4):
    scrub += f'<circle cx="{875 + k*24}" cy="595" r="8" fill="none" stroke="#5ad1c8" stroke-opacity="0.6" stroke-width="1.5"/>'
scrub += '<rect x="899" y="550" width="14" height="12" fill="#5ad1c8" stroke="#05070a" stroke-width="1.5"/>'  # north valve house
scrub += '<path d="M855,612 L832,622" stroke="#5ad1c8" stroke-width="3"/>'  # main gate ramp
# the Spire's air duct: from the hall north to the Spire (dashed)
scrub += '<path d="M906,550 C905,470 880,330 830,190" fill="none" stroke="#5ad1c8" stroke-width="3" opacity="0.85"/>'
scrub += '<path d="M906,550 C905,470 880,330 830,190" fill="none" stroke="#e8fffd" stroke-width="1.2" stroke-dasharray="2 10" opacity="0.9"/>'

# the tenement crash site
crash = '<g transform="translate(888 520)"><circle r="16" fill="url(#fire)"/><rect x="-6" y="-6" width="12" height="12" fill="#3a2a22" stroke="#ff8a3a" stroke-width="1.5"/></g>'

# low quay (south): dense warehouses, berths along the tip
low = ''
for _ in range(110):
    x = random.uniform(560, 1050); y = random.uniform(720, 990)
    # keep inside the rock roughly
    if (x - 800) ** 2 / 300 ** 2 + (y - 840) ** 2 / 175 ** 2 > 1: continue
    low += f'<rect x="{x:.0f}" y="{y:.0f}" width="{random.uniform(10,26):.0f}" height="{random.uniform(6,14):.0f}" fill="#2f2b27" stroke="#5a5048" stroke-width="0.8"/>'
# berth piers along the south tip, radiating from the rock's own outline
N_ = len(rock)
for i in range(N_):
    a = 2 * math.pi * i / N_
    if not (0.80 * math.pi <= a <= 1.20 * math.pi) or i % 2: continue
    x0, y0 = rock[i]
    dx, dy = x0 - 800, y0 - 560
    L = math.hypot(dx, dy)
    x1, y1 = x0 + dx / L * 34, y0 + dy / L * 34
    low += f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="#6d757c" stroke-width="5"/>'
# customs house: the gate between the dock ring and the Low Quay
low += '<rect x="772" y="672" width="56" height="30" fill="#4a3b2c" stroke="#e0b46a" stroke-width="2"/><rect x="792" y="664" width="16" height="46" fill="none" stroke="#e0b46a" stroke-width="1.2"/>'
# berth 31: Thask's bonded warehouse
low += '<rect x="800" y="868" width="50" height="26" fill="#3b2240" stroke="#c98bd6" stroke-width="2.5"/>'
# tug dock behind it
low += '<rect x="812" y="930" width="36" height="16" fill="#2a2e32" stroke="#9aa6ae" stroke-width="1.5"/><path d="M830,894 L830,930" stroke="#c98bd6" stroke-width="1.5" stroke-dasharray="3 3"/>'
# cannery at ~berth 44 (west side of the quay)
low += '<rect x="626" y="842" width="44" height="24" fill="#3d3322" stroke="#e0a050" stroke-width="2"/>'

# west ring: the chandler's (4 Tallow Boys tied) and Old Wick's ambush street
west = '<rect x="560" y="545" width="12" height="10" fill="#e0a050" stroke="#05070a" stroke-width="1"/>'
west += '<path d="M566,560 L700,558" stroke="#b9a98f" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.6"/>'
west += '<circle cx="640" cy="556" r="6" fill="none" stroke="#e0a050" stroke-width="2"/><path d="M636,556 l3,3 l6,-6" stroke="#e0a050" stroke-width="2" fill="none"/>'

# gang turf tints
turf = '<path d="M980,512 C1080,512 1140,518 1150,522 L1152,640 C1080,650 1010,648 980,640 Z" fill="#ff3b30" fill-opacity="0.10" stroke="#ff3b30" stroke-opacity="0.35" stroke-dasharray="6 4"/>'
turf += '<path d="M455,522 C520,512 600,510 690,510 L690,640 C640,700 620,780 610,880 C560,860 520,760 470,650 Z" fill="#ff9a30" fill-opacity="0.09" stroke="#ff9a30" stroke-opacity="0.35" stroke-dasharray="6 4"/>'

# the Bright Light off the rock to the north-east
ship = '<g transform="translate(372 563) rotate(180)"><path d="M-30,0 L22,-7 L34,0 L22,7 Z" fill="#c9d2d8" stroke="#05070a" stroke-width="1.5"/><path d="M-30,-2 L-38,-6 M-30,2 L-38,6" stroke="#9fd0ff" stroke-width="2"/></g>'
ship += ''

# --- markers and callouts
def badge(x, y, n, kind):
    col = {'done': '#5ec26a', 'open': '#f0b63c', 'urgent': '#ff4b3a'}[kind]
    ring_ = f'<circle cx="{x}" cy="{y}" r="22" fill="none" stroke="{col}" stroke-opacity="0.45" stroke-width="3"/>' if kind == 'urgent' else ''
    mark = '✓' if kind == 'done' else str(n)
    return ring_ + f'<circle cx="{x}" cy="{y}" r="14" fill="{col}" stroke="#05070a" stroke-width="2.5"/><text x="{x}" y="{y+5}" text-anchor="middle" class="bn">{mark}</text>'

COL = {'done': '#7fdc8a', 'open': '#f5c55a', 'urgent': '#ff6b5a'}
callouts = [
    # n, kind, marker xy, label side, label y, title, lines
    (1, 'done', (868, 170), 'R', 120, '1 · THE SPIRE: HELD', ['The gates held ~0245 (Moll: 20 left).', 'Venn\'s 17, the cannery children, prisoners.']),
    (2, 'done', (800, 440), 'R', 300, '2 · VOX MAST', ['DONE: saved. The outside line stays open.', 'Unguarded since ~1344 (militia sent home).']),
    (3, 'done', (906, 590), 'R', 470, '3 · SCRUBBER HALL (the air)', ['The swarm and its bell-man destroyed ~0216.', 'Dorrow\'s militia guard it.']),
    (6, 'done', (1080, 560), 'R', 680, '6 · CRANE YARD 6: TAKEN', ['~0414: Dagan Crale beaten one on one, alive.', '~0435: an elite Hookmen push broken.', 'Prisoners to the Spire; the hangar emptied.']),
    (4, 'done', (800, 687), 'L', 640, '4 · CUSTOMS HOUSE: TAKEN', ['~0234: the 6th\'s sergeant dead,', '3 of the 6th captured.', 'Venn\'s garrison freed.']),
    (5, 'done', (825, 881), 'L', 935, '5 · BERTH 31: THASK', ['DONE ~1553: Thask and Ilsabet in chains.', 'The girl safe. Ledgers, 10,000 Thrones.', 'The jars burned. In by the tug dock.']),
    (7, 'done', (648, 854), 'L', 800, '7 · CANNERY: TAKEN', ['~0423: Marl Tegg darted, alive.', 'Pell Rusk + 8 children freed.']),
]
marks = ''
labels = ''
for n, kind, (mx, my), side, ly, title, lines in callouts:
    marks += badge(mx, my, n, kind)
    c = COL[kind]
    if side == 'R':
        lx = 1245
        labels += f'<path d="M{mx+16},{my} L{lx-24},{ly+4} L{lx-8},{ly+4}" fill="none" stroke="{c}" stroke-opacity="0.55" stroke-width="1.4"/>'
        labels += f'<text x="{lx}" y="{ly+9}" class="lt" fill="{c}">{title}</text>'
        for i, t in enumerate(lines):
            labels += f'<text x="{lx}" y="{ly+30+i*18}" class="ls">{t}</text>'
    else:
        lx = 355
        labels += f'<path d="M{mx-16},{my} L{lx+24},{ly+4} L{lx+8},{ly+4}" fill="none" stroke="{c}" stroke-opacity="0.55" stroke-width="1.4"/>'
        labels += f'<text x="{lx}" y="{ly+9}" text-anchor="end" class="lt" fill="{c}">{title}</text>'
        for i, t in enumerate(lines):
            labels += f'<text x="{lx}" y="{ly+30+i*18}" text-anchor="end" class="ls">{t}</text>'

# smaller notes (left column, upper)
notes = ''
def note(mx, my, ly, title, lines, col):
    s = f'<path d="M{mx-8},{my} L{379},{ly+4} L{363},{ly+4}" fill="none" stroke="{col}" stroke-opacity="0.5" stroke-width="1.2"/>'
    s += f'<text x="355" y="{ly+9}" text-anchor="end" class="lt2" fill="{col}">{title}</text>'
    for i, t in enumerate(lines):
        s += f'<text x="355" y="{ly+28+i*17}" text-anchor="end" class="ls">{t}</text>'
    return s
notes += note(640, 556, 420, 'OLD WICK TAKEN ✓', ['Tallow Boys boss, captured in this street.'], '#7fdc8a')
notes += note(566, 550, 490, 'CHANDLER\'S: 4 TALLOW BOYS', ['Picked up by Sgt Dorrow\'s militia ~1344.'], '#7fdc8a')
crash_lbl = '<text x="858" y="506" text-anchor="end" class="dn2" fill="#ff9a5a">crash site · tenement</text>'
crash_lbl += '<circle cx="372" cy="563" r="40" fill="none" stroke="#4fa3ff" stroke-width="2.5"/>'
crash_lbl += ''
import random as _r
_r.seed(7)
for _ in range(14):
    crash_lbl += f'<circle cx="{_r.uniform(560,620):.0f}" cy="{_r.uniform(690,722):.0f}" r="3" fill="#9ad04a" stroke="#05070a" stroke-width="0.8"/>'
crash_lbl += '<text x="590" y="742" text-anchor="middle" class="dn2" fill="#b6e070">~14 poxwalkers, scattered (no herder)</text>'
crash_lbl += '<g transform="translate(830 938)"><path d="M-7,-7 l14,14 M7,-7 l-14,14" stroke="#7fdc8a" stroke-width="2.5"/></g><text x="868" y="975" class="dn2" fill="#7fdc8a">5 of the 6th dead</text>'
notes += crash_lbl

# district names
dist = ''
dist += '<text x="800" y="320" text-anchor="middle" class="dn">HIGH SIDE</text>'
dist += '<text x="800" y="338" text-anchor="middle" class="dn2">trade halls · shuttered through the rising</text>'
dist += '<text x="560" y="632" text-anchor="middle" class="dn" fill="#ffb060">TALLOW BOYS</text>'
dist += '<text x="560" y="648" text-anchor="middle" class="dn2">rendering yards</text><text x="560" y="686" text-anchor="middle" class="dn2" fill="#ffb060">broken: Wick, Tegg taken</text>'
dist += '<text x="1065" y="634" text-anchor="middle" class="dn" fill="#ff7a6a">HOOKMEN</text>'
dist += '<text x="1065" y="650" text-anchor="middle" class="dn2">the cranes</text><text x="1065" y="666" text-anchor="middle" class="dn2" fill="#ff7a6a">broken: Crale taken</text>'
dist += '<text x="720" y="618" text-anchor="middle" class="dn">DOCK RING</text>'
dist += '<text x="800" y="760" text-anchor="middle" class="dn">LOW QUAY</text>'
dist += '<text x="800" y="776" text-anchor="middle" class="dn2">docks · canneries · bunk stacks</text>'
dist += '<text x="868" y="958" class="dn2">tug dock</text>'
dist += '<text x="330" y="619" text-anchor="middle" class="lt2" fill="#4fa3ff">THE BRIGHT LIGHT · BERTH 12</text><text x="330" y="635" text-anchor="middle" class="dn2" fill="#4fa3ff">docked ~0745 · THE LIGHT IS HERE</text>'
dist += '<text x="892" y="560" text-anchor="end" class="dn2" fill="#8fe8e0">air on ~1409 · valve house</text>'
dist += '<text x="740" y="478" class="dn2">west stair</text>'
dist += '<text x="852" y="455" class="dn2">ridge road</text>'

# Vashti's Rock: a small Free Trader asteroid ~8 km off the Mart (player's idea, day 34)
vr = blob(200, 250, 46, 34, n=40, jitter=0.12, seed=11)
vr_d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in vr) + ' Z'
dist += f'<path d="{vr_d}" fill="#5a524b" stroke="#a8946a" stroke-width="2"/>'
dist += '<rect x="184" y="240" width="32" height="18" rx="2" fill="#2d2a27" stroke="#d9b45a" stroke-width="1.5"/>'
dist += '<path d="M250,258 L470,320" stroke="#d9b45a" stroke-width="1.2" stroke-dasharray="3 6" opacity="0.6"/>'
dist += '<text x="200" y="310" text-anchor="middle" class="lt2" fill="#d9b45a">VASHTI\'S ROCK</text>'
dist += '<text x="200" y="327" text-anchor="middle" class="dn2">Mag Vashti\'s Void Exchange · ~8 km off</text>'
dist += '<text x="200" y="343" text-anchor="middle" class="dn2">her own guns · the rising never reached it</text>'
# compass and scale note
dist += '<g transform="translate(1530 990)"><path d="M0,-30 L8,0 L0,-6 L-8,0 Z" fill="#c9d2d8"/><text y="-36" text-anchor="middle" class="dn2">N</text></g>'
dist += '<text x="1580" y="1060" text-anchor="end" class="dn2">schematic, not to scale · Spire to mast ~1.5 km · mast to scrubber hall ~500 m</text>'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
  <style>
    .tt{{font:700 30px 'Cinzel', serif; letter-spacing:4px; fill:#e8e0cf}}
    .st{{font:500 13px 'IBM Plex Mono', monospace; letter-spacing:2px; fill:#a89f90}}
    .lt{{font:700 16px 'IBM Plex Mono', monospace; letter-spacing:1px; paint-order:stroke; stroke:#05070a; stroke-width:4px}}
    .lt2{{font:700 13px 'IBM Plex Mono', monospace; letter-spacing:1px; paint-order:stroke; stroke:#05070a; stroke-width:4px}}
    .ls{{font:500 12.5px 'IBM Plex Mono', monospace; fill:#cfd6db; paint-order:stroke; stroke:#05070a; stroke-width:3px}}
    .dn{{font:700 13px 'IBM Plex Mono', monospace; letter-spacing:4px; fill:#d8d0c0; paint-order:stroke; stroke:#05070a; stroke-width:4px}}
    .dn2{{font:500 11px 'IBM Plex Mono', monospace; letter-spacing:1px; fill:#a8a090; paint-order:stroke; stroke:#05070a; stroke-width:3px}}
    .bn{{font:700 15px 'IBM Plex Mono', monospace; fill:#05070a}}
  </style>
  <radialGradient id="rockfill" cx="45%" cy="40%" r="70%"><stop offset="0" stop-color="#4a433c"/><stop offset="0.7" stop-color="#2e2924"/><stop offset="1" stop-color="#1c1916"/></radialGradient>
  <radialGradient id="dome"><stop offset="0" stop-color="#9fd0ff" stop-opacity="0.35"/><stop offset="1" stop-color="#2a3a48" stop-opacity="0.8"/></radialGradient>
  <radialGradient id="fire"><stop offset="0" stop-color="#ffb04a" stop-opacity="0.95"/><stop offset="0.5" stop-color="#ff5a1a" stop-opacity="0.5"/><stop offset="1" stop-color="#ff3a00" stop-opacity="0"/></radialGradient>
  <pattern id="ringplate" width="22" height="22" patternUnits="userSpaceOnUse"><rect width="22" height="22" fill="#3b4045"/><rect x="1" y="1" width="20" height="20" fill="#42484e" stroke="#2d3135" stroke-width="1.5"/></pattern>
  <clipPath id="rc"><path d="{rock_d}"/></clipPath>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.10 0"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="#06070a"/>
{stars}
<path d="{rock_d}" fill="#000" opacity="0.6" transform="translate(10 14)"/>
<path d="{rock_d}" fill="url(#rockfill)" stroke="#7a7068" stroke-width="2.5"/>
<g clip-path="url(#rc)">{surf}{turf}</g>
{ring}{ridge}{high}{low}{west}{scrub}{crash}{ship}{dist}
{marks}{labels}{notes}
<text x="24" y="50" class="tt">TORVANE'S MART</text>
<text x="26" y="74" class="st">DAY 36 · ~0600 · WHAT THE LIGHT KNOWS</text>
<text x="26" y="100" class="lt2" fill="#ff6b5a">THE MOEBIAN 6TH ARE BEHIND IT ALL</text>
<text x="26" y="117" class="ls">a rotted Guard regiment · the jars, the girl, the plan</text>
<text x="26" y="134" class="ls">~0445: all seven done. Thask, Crale, Wick, Tegg taken.</text>
<rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.6"/>
</svg>'''
html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=IBM+Plex+Mono:wght@500;700&display=block"><style>html,body{{margin:0;background:#000}}svg{{display:block}}</style></head><body>{svg}</body></html>'''
open(out, 'w').write(html)
