import sys, os
# Regenerates the animated SVGs in assets/. Run: python3 scripts/gen_svgs.py assets
OUT = sys.argv[1]
BG, BG2, LINE, TEXT, T2, T3, ACC, GOOD = '#0b0b0d','#111114','#25252b','#ede8dd','#9a958a','#645f56','#e9743b','#7fb069'
SERIF = "Fraunces, 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif"
MONO = "'JetBrains Mono', 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
EASE = 'cubic-bezier(0.23, 1, 0.32, 1)'
EASE_IO = 'cubic-bezier(0.77, 0, 0.175, 1)'
REDUCED = '@media (prefers-reduced-motion: reduce){*{animation:none !important}}'

def write(name, s):
    with open(os.path.join(OUT, name), 'w') as f: f.write(s)

# ───────────────────────── header ─────────────────────────
W, H = 1200, 420
boxes = [('INGEST',700,130),('RETRIEVE',850,130),('RERANK',1000,130),('AGENT',1000,250),('EVAL',850,250),('SHIP',700,250)]
hits = [0, 1.0, 2.0, 2.8, 3.8, 4.75]
box_svg = []
for i,(lbl,x,y) in enumerate(boxes):
    box_svg.append(f'''<g>
      <rect x="{x}" y="{y}" width="120" height="38" rx="4" fill="{BG2}" stroke="{LINE}"/>
      <rect class="hl" style="animation-delay:{hits[i]}s" x="{x}" y="{y}" width="120" height="38" rx="4" fill="rgba(233,116,59,.10)" stroke="{ACC}"/>
      <text x="{x+60}" y="{y+24}" text-anchor="middle" class="mono" font-size="12" letter-spacing="1.5" fill="{T2}">{lbl}</text>
    </g>''')
PATH = 'M760 149 H1060 V269 H760'
header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Devansh Sharma. Co-Founder at LayeredAI, building production RAG, agents and LLMOps.">
  <style>
    .serif{{font-family:{SERIF}}} .mono{{font-family:{MONO}}}
    .rise{{animation:rise 1.1s {EASE} both}}
    @keyframes rise{{from{{transform:translateY(120px)}}to{{transform:translateY(0)}}}}
    .fade{{animation:fade .9s {EASE} both}}
    @keyframes fade{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
    .ring{{transform-box:fill-box;transform-origin:center;animation:ring 2.6s ease-out infinite}}
    @keyframes ring{{0%{{opacity:.6;transform:scale(1)}}70%,100%{{opacity:0;transform:scale(3.2)}}}}
    .hl{{opacity:0;animation:hl 4.8s linear infinite}}
    @keyframes hl{{0%{{opacity:0}}4%{{opacity:1}}22%{{opacity:0}}100%{{opacity:0}}}}
    .flow{{stroke-dasharray:3 9;animation:flow 1.2s linear infinite}}
    @keyframes flow{{to{{stroke-dashoffset:-12}}}}
    .caret{{animation:blink 1s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:0}}}}
    {REDUCED}
  </style>
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".035"/></pattern>
    <radialGradient id="glow" cx="88%" cy="100%" r="60%"><stop offset="0" stop-color="{ACC}" stop-opacity=".16"/><stop offset="1" stop-color="{ACC}" stop-opacity="0"/></radialGradient>
    <clipPath id="nameClip"><rect x="0" y="108" width="680" height="214"/></clipPath>
    <clipPath id="typeClip"><rect x="52" y="330" width="0" height="60"><animate attributeName="width" from="0" to="504" begin="1s" dur="2.2s" fill="freeze"/></rect></clipPath>
  </defs>
  <rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#glow)"/>
  <rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{LINE}"/>

  <g class="fade" style="animation-delay:.1s">
    <rect x="52" y="44" width="214" height="28" rx="14" fill="{BG2}" stroke="{LINE}"/>
    <circle class="ring" cx="70" cy="58" r="4" fill="{GOOD}"/>
    <circle cx="70" cy="58" r="4" fill="{GOOD}"/>
    <text x="84" y="62" class="mono" font-size="12" letter-spacing="1.5" fill="{T2}">SHIPPING · NEW YORK</text>
  </g>
  <g class="fade" style="animation-delay:.25s">
    <rect x="904" y="44" width="244" height="28" rx="14" fill="rgba(233,116,59,.08)" stroke="#3a2418"/>
    <rect x="916" y="51" width="38" height="14" rx="2" fill="{ACC}"/>
    <text x="935" y="62" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{BG}">NEW</text>
    <text x="964" y="62" class="mono" font-size="12" letter-spacing="1.2" fill="{TEXT}">PAPER · ARXIV 2609.12960</text>
  </g>

  <g clip-path="url(#nameClip)">
    <text class="serif rise" style="animation-delay:.15s" x="48" y="208" font-size="104" font-weight="400" letter-spacing="-3" fill="{TEXT}">Devansh</text>
    <text class="serif rise" style="animation-delay:.3s" x="48" y="306" font-size="104" font-style="italic" font-weight="400" letter-spacing="-3" fill="{ACC}">Sharma</text>
  </g>

  <g clip-path="url(#typeClip)">
    <text x="52" y="352" class="mono" font-size="15" fill="{TEXT}">Co-Founder @ LayeredAI · production RAG, agents, LLMOps</text>
    <text x="52" y="378" class="mono" font-size="13" fill="{T3}">New York · provider-agnostic · Python + GCP</text>
  </g>
  <rect class="caret" x="52" y="338" width="8" height="18" fill="{ACC}">
    <animate attributeName="x" from="52" to="556" begin="1s" dur="2.2s" fill="freeze"/>
  </rect>

  <g class="fade" style="animation-delay:.5s">
    <path d="{PATH}" fill="none" stroke="{LINE}" stroke-width="1.5"/>
    <path class="flow" d="{PATH}" fill="none" stroke="{ACC}" stroke-opacity=".55" stroke-width="1.5"/>
    {''.join(box_svg)}
    <circle r="5" fill="{ACC}"><animateMotion dur="4.8s" repeatCount="indefinite" path="{PATH}"/></circle>
    <circle r="11" fill="{ACC}" fill-opacity=".18"><animateMotion dur="4.8s" repeatCount="indefinite" path="{PATH}"/></circle>
    <text x="700" y="330" class="mono" font-size="11" letter-spacing="1.5" fill="{T3}">PRODUCTION PIPELINE · TRACED END TO END</text>
  </g>
</svg>'''
write('header.svg', header)

# ───────────────────────── cards ─────────────────────────
def card(name, label, kicker, title, lines, stack, visual, css):
    desc = ''.join(f'<text x="32" y="{132 + i*23}" class="sans" font-size="15" fill="{T2}">{l}</text>' for i,l in enumerate(lines))
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="300" viewBox="0 0 600 300" role="img" aria-label="{label}">
  <style>
    .serif{{font-family:{SERIF}}} .mono{{font-family:{MONO}}} .sans{{font-family:{SANS}}}
    {css}
    {REDUCED}
  </style>
  <defs><pattern id="g" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#fff" stroke-opacity=".03"/></pattern></defs>
  <rect x=".5" y=".5" width="599" height="299" rx="12" fill="{BG2}" stroke="{LINE}"/>
  <text x="32" y="48" class="mono" font-size="11.5" letter-spacing="1.4" fill="{ACC}">{kicker}</text>
  <text x="32" y="94" class="serif" font-size="32" fill="{TEXT}" letter-spacing="-.5">{title}</text>
  {desc}
  <text x="32" y="270" class="mono" font-size="11" letter-spacing="1.2" fill="{T3}">{stack}</text>
  <rect x="352" y="28" width="220" height="244" rx="8" fill="{BG}" stroke="{LINE}"/>
  <rect x="352" y="28" width="220" height="244" rx="8" fill="url(#g)"/>
  {visual}
</svg>'''
    write(name, s)

# sanskrit-token: tokens relative to translation, 0..2.4 scale
tx, tw = 368, 188
rows = [('vs English','1.77–2.19×',1.77,2.19,ACC),('vs Hindi','1.33–1.35×',1.33,1.35,ACC),('32–64k vocab','1.03–1.14×',1.03,1.142,ACC),('128k vocab','0.983×',0.975,0.983,GOOD)]
v = [f'<text x="368" y="54" class="mono" font-size="9.5" letter-spacing="1.2" fill="{T3}">TOKENS VS TRANSLATION</text>']
px = tx + tw/2.4
for i,(lab,val,lo,hi,c) in enumerate(rows):
    y = 84 + i*46
    lw, hw = tw*lo/2.4, max(tw*hi/2.4, tw*lo/2.4 + 3)
    v.append(f'''<text x="368" y="{y}" class="mono" font-size="10" fill="{T2}">{lab}</text>
    <text x="556" y="{y}" text-anchor="end" class="mono" font-size="10" fill="{c}">{val}</text>
    <rect x="{tx}" y="{y+8}" width="{tw}" height="9" rx="2" fill="#1d1d22"/>
    <g class="grow" style="animation-delay:{i*0.15}s">
      <rect x="{tx}" y="{y+8}" width="{hw:.1f}" height="9" rx="2" fill="{c}" fill-opacity=".3"/>
      <rect x="{tx+lw:.1f}" y="{y+8}" width="{hw-lw:.1f}" height="9" fill="{c}"/>
    </g>''')
v.append(f'<line x1="{px:.1f}" y1="64" x2="{px:.1f}" y2="250" stroke="{T3}" stroke-dasharray="3 3"/><text x="{px+5:.1f}" y="258" class="mono" font-size="9" fill="{T3}">PARITY</text>')
card('card-sanskrit-token.svg', 'sanskrit-token: tokenization research, arXiv 2609.12960',
     'RESEARCH · ARXIV 2609.12960', 'sanskrit-token',
     ["Does Sanskrit's density survive", 'subword tokenization? Measured per', 'proposition against matched controls,', 'with a paper built from the results.'],
     'PYTHON · PYTORCH · SENTENCEPIECE', '\n'.join(v),
     f'.grow{{transform-box:fill-box;transform-origin:left center;animation:grow 7s {EASE_IO} infinite both}}'
     '@keyframes grow{0%{transform:scaleX(0)}22%{transform:scaleX(1)}86%{transform:scaleX(1);opacity:1}96%,100%{transform:scaleX(1);opacity:0}}')

# rain-padel: leaderboard where row 3 overtakes row 2
def row(y, name, pts_svg, extra=''):
    return f'''<rect x="364" y="{y}" width="196" height="34" rx="4" fill="{BG2}" stroke="{LINE}"/>{extra}
      <text x="412" y="{y+22}" class="serif" font-size="15" fill="{TEXT}">{name}</text>{pts_svg}'''
v = [f'''<text x="368" y="54" class="mono" font-size="9.5" letter-spacing="1.2" fill="{T3}">MEXICANO · ROUND 3</text>
  <circle class="ring" cx="530" cy="51" r="3.5" fill="{GOOD}"/><circle cx="530" cy="51" r="3.5" fill="{GOOD}"/>
  <text x="556" y="54" text-anchor="end" class="mono" font-size="9.5" fill="{GOOD}">LIVE</text>''']
pts = lambda y, p: f'<text x="548" y="{y+22}" text-anchor="end" class="mono" font-size="13" fill="{ACC}">{p}</text>'
v.append(f'<g>{row(68,"Aisha",pts(68,"64"))}</g>')
v.append(f'<g class="down">{row(112,"Omar",pts(112,"58"))}</g>')
dev_pts = f'<text class="old" x="548" y="{156+22}" text-anchor="end" font-size="13" fill="{ACC}" font-family="{MONO}">55</text><text class="new" x="548" y="{156+22}" text-anchor="end" font-size="13" fill="{ACC}" font-family="{MONO}">61</text>'
v.append(f'<g class="up">{row(156,"Dev",dev_pts, f"<rect class=\"flash\" x=\"364\" y=\"156\" width=\"196\" height=\"34\" rx=\"4\" fill=\"rgba(233,116,59,.12)\" stroke=\"{ACC}\"/>")}<text class="plus" x="508" y="{156+22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{GOOD}">+6</text></g>')
v.append(f'<g>{row(200,"Rina",pts(200,"49"))}</g>')
# rank numbers drawn on top so they stay put while rows move
v.append(''.join(f'<text x="378" y="{90+i*44}" class="mono" font-size="11" fill="{T3}">0{i+1}</text>' for i in range(4)))
card('card-rain-padel.svg', 'Rain Padel: social padel app with a live leaderboard',
     'LIVE APP · RAIN-PADEL.VERCEL.APP', 'Rain Padel',
     ['Runs a social padel night from one', 'phone. Americano, Mexicano, King of', 'the Court, with a live individual', 'leaderboard as the scores come in.'],
     'NEXT.JS · TYPESCRIPT · SUPABASE', '\n'.join(v),
     f'.ring{{transform-box:fill-box;transform-origin:center;animation:ring 2.4s ease-out infinite}}@keyframes ring{{0%{{opacity:.6;transform:scale(1)}}70%,100%{{opacity:0;transform:scale(3)}}}}'
     f'.up{{animation:up 6s {EASE_IO} infinite}}@keyframes up{{0%,40%{{transform:translateY(0)}}52%,88%{{transform:translateY(-44px)}}98%,100%{{transform:translateY(0)}}}}'
     f'.down{{animation:down 6s {EASE_IO} infinite}}@keyframes down{{0%,40%{{transform:translateY(0)}}52%,88%{{transform:translateY(44px)}}98%,100%{{transform:translateY(0)}}}}'
     '.old{animation:old 6s linear infinite}@keyframes old{0%,30%{opacity:1}34%,92%{opacity:0}96%,100%{opacity:1}}'
     '.new{animation:new 6s linear infinite}@keyframes new{0%,30%{opacity:0}34%,92%{opacity:1}96%,100%{opacity:0}}'
     '.flash{opacity:0;animation:flash 6s linear infinite}@keyframes flash{0%,28%{opacity:0}34%{opacity:1}60%,100%{opacity:0}}'
     f'.plus{{opacity:0;animation:plus 6s {EASE} infinite}}@keyframes plus{{0%,28%{{opacity:0;transform:translateY(6px)}}34%{{opacity:1;transform:translateY(0)}}50%,100%{{opacity:0;transform:translateY(-8px)}}}}')

# rag-chat: chunks feed an answer with citations
v = [f'<text x="368" y="54" class="mono" font-size="9.5" letter-spacing="1.2" fill="{T3}">RETRIEVE → ANSWER</text>']
for i,y in enumerate([70,130,190]):
    hot = i != 1
    v.append(f'''<rect x="366" y="{y}" width="74" height="46" rx="4" fill="{BG2}" stroke="{LINE}"/>
    {f'<rect class="hot" style="animation-delay:{i*0.25}s" x="366" y="{y}" width="74" height="46" rx="4" fill="rgba(233,116,59,.08)" stroke="{ACC}"/>' if hot else ''}
    <rect x="376" y="{y+12}" width="48" height="4" rx="2" fill="{T3}"/><rect x="376" y="{y+21}" width="54" height="4" rx="2" fill="#2e2e35"/><rect x="376" y="{y+30}" width="38" height="4" rx="2" fill="#2e2e35"/>
    {f'<text x="434" y="{y+40}" text-anchor="end" font-family="{MONO}" font-size="8" fill="{ACC}">{1 if i==0 else 2}</text>' if hot else ''}''')
    if hot:
        v.append(f'<path class="beam" style="animation-delay:{i*0.25}s" d="M440 {y+23} C 456 {y+23}, 452 140, 468 140" fill="none" stroke="{ACC}" stroke-width="1.2"/>')
v.append(f'''<rect x="468" y="84" width="92" height="112" rx="6" fill="{BG2}" stroke="{LINE}"/>
  <text x="478" y="100" font-family="{MONO}" font-size="8.5" letter-spacing="1" fill="{T3}">ANSWER</text>''')
for i,(w,d) in enumerate([(70,.9),(62,1.05),(72,1.2),(48,1.35),(66,1.5)]):
    v.append(f'<rect class="ln" style="animation-delay:{d}s" x="478" y="{110+i*11}" width="{w}" height="4" rx="2" fill="{T2}"/>')
v.append(f'''<g class="chip" style="animation-delay:1.7s"><rect x="478" y="168" width="22" height="16" rx="3" fill="rgba(233,116,59,.14)" stroke="{ACC}"/><text x="489" y="180" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{ACC}">1</text></g>
  <g class="chip" style="animation-delay:1.85s"><rect x="504" y="168" width="22" height="16" rx="3" fill="rgba(233,116,59,.14)" stroke="{ACC}"/><text x="515" y="180" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{ACC}">2</text></g>
  <text x="368" y="258" font-family="{MONO}" font-size="9" fill="{T3}">2 OF 3 CHUNKS CITED</text>''')
card('card-rag-chat.svg', 'rag-chat: document chat with inline citations',
     'RAG · SOURCE-GROUNDED CHAT', 'rag-chat',
     ['Upload documents, ask questions,', 'get answers with inline citations.', 'Background ingestion, vector search,', 'and every claim tied to a source.'],
     'NEXT.JS · FASTAPI · CHROMA · POSTGRES', '\n'.join(v),
     '.hot{opacity:0;animation:hot 5s linear infinite}@keyframes hot{0%,8%{opacity:0}14%,80%{opacity:1}90%,100%{opacity:0}}'
     '.beam{stroke-dasharray:60;stroke-dashoffset:60;animation:beam 5s ease-out infinite}@keyframes beam{0%,10%{stroke-dashoffset:60}22%,80%{stroke-dashoffset:0;opacity:1}90%,100%{stroke-dashoffset:0;opacity:0}}'
     f'.ln{{transform-box:fill-box;transform-origin:left center;animation:ln 5s {EASE} infinite both}}@keyframes ln{{0%,10%{{transform:scaleX(0)}}18%,82%{{transform:scaleX(1);opacity:1}}92%,100%{{transform:scaleX(1);opacity:0}}}}'
     f'.chip{{transform-box:fill-box;transform-origin:center;animation:chip 5s {EASE} infinite both}}@keyframes chip{{0%,14%{{opacity:0;transform:scale(.8)}}20%,82%{{opacity:1;transform:scale(1)}}92%,100%{{opacity:0}}}}')

# reviewbot-swarm: four agent lanes into a validator gate
lanes = [('SECURITY',72),('PERF',112),('STYLE',152),('TESTS',192)]
v = [f'<text x="368" y="54" class="mono" font-size="9.5" letter-spacing="1.2" fill="{T3}">PARALLEL AGENTS → GATE</text>']
for i,(lab,y) in enumerate(lanes):
    p = f'M424 {y} C 452 {y}, 448 132, 478 132'
    v.append(f'''<rect x="364" y="{y-11}" width="58" height="22" rx="3" fill="{BG2}" stroke="{LINE}"/>
    <text x="393" y="{y+3.5}" text-anchor="middle" font-family="{MONO}" font-size="8.5" letter-spacing=".6" fill="{T2}">{lab}</text>
    <path d="{p}" fill="none" stroke="{LINE}" stroke-width="1.2"/>
    <circle r="3.5" fill="{GOOD if i!=2 else T3}" opacity="0">
      <animateMotion dur="3.2s" begin="{i*0.35}s" repeatCount="indefinite" path="{p}" keyPoints="0;1;1" keyTimes="0;.5;1" calcMode="linear"/>
      <animate attributeName="opacity" dur="3.2s" begin="{i*0.35}s" repeatCount="indefinite" values="0;1;1;0;0" keyTimes="0;.08;.46;.52;1"/>
    </circle>''')
v.append(f'''<rect x="478" y="104" width="44" height="56" rx="4" fill="rgba(233,116,59,.08)" stroke="{ACC}"/>
  <rect class="gate" x="478" y="104" width="44" height="56" rx="4" fill="none" stroke="{ACC}" stroke-width="2"/>
  <text x="500" y="136" text-anchor="middle" font-family="{MONO}" font-size="8.5" fill="{ACC}">GATE</text>
  <path d="M522 132 H556" stroke="{LINE}" stroke-width="1.2"/>
  <circle r="3.5" fill="{ACC}"><animateMotion dur="1.6s" repeatCount="indefinite" path="M522 132 H556"/></circle>
  <rect x="528" y="176" width="36" height="22" rx="3" fill="{BG2}" stroke="{LINE}"/>
  <text x="546" y="191" text-anchor="middle" font-family="{MONO}" font-size="8.5" fill="{T2}">PR</text>
  <path d="M556 132 V176" stroke="{LINE}" stroke-width="1.2" stroke-dasharray="2 3"/>
  <text x="368" y="236" font-family="{MONO}" font-size="9" fill="{T3}">WEAK FINDINGS DROPPED</text>
  <text x="368" y="252" font-family="{MONO}" font-size="9" fill="{T3}">BEFORE ANYTHING IS POSTED</text>''')
card('card-reviewbot-swarm.svg', 'reviewbot-swarm: multi-agent pull request reviewer',
     'MULTI-AGENT · PR REVIEW', 'reviewbot-swarm',
     ['Security, performance, style and', 'test agents review a PR in parallel.', 'A validator gate drops weak findings', 'before anything gets posted.'],
     'TYPESCRIPT · ANTHROPIC · GITHUB API', '\n'.join(v),
     '.gate{transform-box:fill-box;transform-origin:center;animation:gate 1.6s ease-out infinite}@keyframes gate{0%{opacity:.8;transform:scale(1)}100%{opacity:0;transform:scale(1.35)}}')

# schedulerAI: day timeline with a moving "now" line and a recovery ring
import math
v = [f'<text x="368" y="54" class="mono" font-size="9.5" letter-spacing="1.2" fill="{T3}">TODAY · 82% RECOVERY</text>']
r, cx, cy = 20, 532, 76
circ = 2*math.pi*r
v.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1d1d22" stroke-width="5"/>'
         f'<circle class="ring82" cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GOOD}" stroke-width="5" stroke-linecap="round" '
         f'stroke-dasharray="{circ:.1f}" stroke-dashoffset="{circ*0.18:.1f}" transform="rotate(-90 {cx} {cy})"/>'
         f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{GOOD}">82</text>')
blocks = [('9:00','Deep work · planner',96,ACC),('11:00','Reviews UI',64,ACC),('1:30','Gym · upper body',52,GOOD),('3:30','Weekly review',70,T2),('5:30','Reading',40,T2)]
for i,(t,lab,w,c) in enumerate(blocks):
    y = 112 + i*28
    v.append(f'<text x="366" y="{y+12}" font-family="{MONO}" font-size="9" fill="{T3}">{t}</text>'
             f'<rect x="400" y="{y}" width="156" height="18" rx="3" fill="{BG2}" stroke="{LINE}"/>'
             f'<rect class="fill" style="animation-delay:{i*0.55:.2f}s" x="400" y="{y}" width="{w}" height="18" rx="3" fill="{c}" fill-opacity=".22"/>'
             f'<text x="406" y="{y+12.5}" font-family="{SANS}" font-size="10" fill="{TEXT}">{lab}</text>')
v.append(f'<g class="now"><line x1="396" y1="106" x2="560" y2="106" stroke="{ACC}" stroke-width="1.2"/><circle cx="396" cy="106" r="3" fill="{ACC}"/></g>'
         f'<text x="368" y="262" font-family="{MONO}" font-size="9" fill="{T3}">WHOOP · CALENDAR · GOALS → BRIEF</text>')
card('card-schedulerai.svg', 'SchedulerAI: a daily time ledger with an AI morning brief',
     'LIVE APP · PRIVATE BETA', 'SchedulerAI',
     ['A daily ledger for where the time', 'went. Timer, goals, calendar and', 'WHOOP recovery become an AI', 'morning brief and a plan.'],
     'NEXT.JS · PRISMA · NEXTAUTH · LLM', '\n'.join(v),
     f'.ring82{{animation:ring82 6s {EASE_IO} infinite both}}@keyframes ring82{{0%,8%{{stroke-dashoffset:{circ:.1f}}}35%,88%{{stroke-dashoffset:{circ*0.18:.1f}}}100%{{stroke-dashoffset:{circ:.1f}}}}}'
     f'.fill{{transform-box:fill-box;transform-origin:left center;animation:fill 6s {EASE} infinite both}}@keyframes fill{{0%,4%{{transform:scaleX(0)}}16%,88%{{transform:scaleX(1);opacity:1}}98%,100%{{transform:scaleX(1);opacity:0}}}}'
     '.now{animation:now 6s linear infinite}@keyframes now{0%{transform:translateY(0)}88%{transform:translateY(140px);opacity:1}96%,100%{transform:translateY(140px);opacity:0}}')

# paperbot: a proposal with estimate vs market and a pulsing approve button
pb = [
  f'<text x="368" y="54" class="mono" font-size="9.5" letter-spacing="1.2" fill="{T3}">MORNING QUEUE · PAPER</text>',
  f'<rect x="366" y="66" width="34" height="16" rx="3" fill="rgba(127,176,105,.14)" stroke="{GOOD}"/>',
  f'<text x="383" y="78" text-anchor="middle" font-family="{MONO}" font-size="9" fill="{GOOD}">YES</text>',
  f'<text x="366" y="102" font-family="{SERIF}" font-size="13" fill="{TEXT}">Will the central bank</text>',
  f'<text x="366" y="119" font-family="{SERIF}" font-size="13" fill="{TEXT}">hold rates next meeting?</text>',
  f'<text x="366" y="144" font-family="{MONO}" font-size="9" fill="{T2}">PAPERBOT</text><text x="556" y="144" text-anchor="end" font-family="{MONO}" font-size="10" fill="{ACC}">68%</text>',
  f'<rect x="366" y="150" width="190" height="8" rx="2" fill="#1d1d22"/>',
  f'<rect class="est" x="366" y="150" width="{190*0.68:.1f}" height="8" rx="2" fill="{ACC}"/>',
  f'<text x="366" y="176" font-family="{MONO}" font-size="9" fill="{T2}">MARKET</text><text x="556" y="176" text-anchor="end" font-family="{MONO}" font-size="10" fill="{T2}">56%</text>',
  f'<rect x="366" y="182" width="190" height="8" rx="2" fill="#1d1d22"/>',
  f'<rect class="mkt" x="366" y="182" width="{190*0.56:.1f}" height="8" rx="2" fill="{T2}"/>',
  f'<text class="edge" x="366" y="210" font-family="{MONO}" font-size="9" fill="{GOOD}">+12 PT EDGE · MAX LOSS $20</text>',
  f'<rect x="366" y="224" width="112" height="28" rx="4" fill="{ACC}"/>',
  f'<rect class="pulse" x="366" y="224" width="112" height="28" rx="4" fill="none" stroke="{ACC}" stroke-width="2"/>',
  f'<text x="422" y="242" text-anchor="middle" font-family="{MONO}" font-size="9.5" font-weight="700" fill="{BG}">APPROVE</text>',
  f'<rect x="486" y="224" width="70" height="28" rx="4" fill="{BG2}" stroke="{LINE}"/>',
  f'<text x="521" y="242" text-anchor="middle" font-family="{MONO}" font-size="9.5" fill="{T2}">PASS</text>',
]
card('card-paperbot.svg', 'Paperbot: an AI copilot for prediction-market paper trading',
     'LIVE APP · AI TRADING COPILOT', 'Paperbot',
     ['Researches Polymarket overnight', 'with live web search, forms its own', 'probability, Kelly-sizes paper bets,', 'and waits for a human yes or no.'],
     'NEXT.JS · SUPABASE · CLAUDE · SEARCH', '\n'.join(pb),
     f'.est,.mkt{{transform-box:fill-box;transform-origin:left center;animation:bar 6s {EASE_IO} infinite both}}.mkt{{animation-delay:.2s}}'
     '@keyframes bar{0%,6%{transform:scaleX(0)}28%,88%{transform:scaleX(1);opacity:1}98%,100%{transform:scaleX(1);opacity:0}}'
     '.edge{animation:edge 6s ease infinite both}@keyframes edge{0%,30%{opacity:0}40%,88%{opacity:1}98%,100%{opacity:0}}'
     '.pulse{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}@keyframes pulse{0%{opacity:.8;transform:scale(1)}100%{opacity:0;transform:scale(1.18,1.5)}}')

# ───────────────────────── stack marquee ─────────────────────────
items = ['Claude 5.5','GPT','Gemini','Llama','Qwen','DeepSeek','Anthropic SDK','MCP','LangChain','PyTorch','Transformers','Python','TypeScript','Next.js','FastAPI','Supabase','Postgres','Prisma','Chroma','Vercel','BigQuery','Cloud Run','Docker','Kubernetes','Sentry']
CW, GAP = 13.25, 64
x = 0; parts = []
for it in items:
    parts.append((x, it)); x += len(it)*CW + GAP
period = round(x)
def run(off):
    out = []
    for px_, it in parts:
        out.append(f'<text x="{off+px_:.0f}" y="53" font-family="{MONO}" font-size="22" fill="{T2}">{it}</text>')
        dx = off + px_ + len(it)*CW + GAP/2
        out.append(f'<rect x="{dx-4.5:.1f}" y="41" width="9" height="9" fill="{ACC}" transform="rotate(45 {dx:.1f} 45.5)"/>')
    return ''.join(out)
marquee = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="90" viewBox="0 0 1200 90" role="img" aria-label="Stack: {', '.join(items)}">
  <style>.track{{animation:m {period/38:.1f}s linear infinite}}@keyframes m{{to{{transform:translateX(-{period}px)}}}}{REDUCED}</style>
  <defs>
    <linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".08" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <mask id="mk"><rect width="1200" height="90" fill="url(#fade)"/></mask>
  </defs>
  <rect x=".5" y=".5" width="1199" height="89" rx="12" fill="{BG}" stroke="{LINE}"/>
  <g mask="url(#mk)"><g class="track">{run(24)}{run(24+period)}{run(24+2*period)}</g></g>
</svg>'''
write('stack.svg', marquee)

# ───────────────────────── footer ─────────────────────────
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="210" viewBox="0 0 1200 210" role="img" aria-label="If you're shipping AI into production, let's build it properly.">
  <style>
    .u{{stroke-dasharray:420;stroke-dashoffset:420;animation:u 5s {EASE_IO} infinite}}
    @keyframes u{{0%,10%{{stroke-dashoffset:420}}40%,85%{{stroke-dashoffset:0;opacity:1}}95%,100%{{stroke-dashoffset:0;opacity:0}}}}
    {REDUCED}
  </style>
  <rect x=".5" y=".5" width="1199" height="209" rx="14" fill="{BG}" stroke="{LINE}"/>
  <text x="600" y="86" text-anchor="middle" font-family="{SERIF}" font-size="40" fill="{TEXT}" letter-spacing="-.5">If you're shipping AI into production,</text>
  <text x="600" y="136" text-anchor="middle" font-family="{SERIF}" font-size="40" font-style="italic" fill="{ACC}" letter-spacing="-.5">let's build it properly.</text>
  <path class="u" d="M410 152 C 520 160, 690 146, 790 152" fill="none" stroke="{ACC}" stroke-width="2" stroke-linecap="round"/>
  <text x="600" y="186" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="1.6" fill="{T3}">SHARMADEVANSH436@GMAIL.COM · NEW YORK</text>
</svg>'''
write('footer.svg', footer)
print('ok', period)
