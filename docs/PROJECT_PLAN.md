# Viking Ship Navigation Game — Detailed Project Plan

**Project:** Learning game about Viking navigation between known landmarks
**Repository:** `viking-ship-navigation-game` (own code licensed Apache-2.0)
**Status:** Draft v1.2 — for review
**Target engine:** Unreal Engine 5 (UE 5.4+, exact version pinned at G0)
**External controller:** Scratch 3 program (steering-oar input)

### Document control

| Version | Change |
|---|---|
| v1.0 | Initial plan |
| v1.1 | Review round 1: scale/time-compression decision (D1), tides & currents, tutorial scenario S0, failure states, non-goals, team & roles, platform/repo infrastructure, data licensing, Scratch editor risk (D2), telemetry realism (D3), privacy note, gate exit criteria, decision register, glossary, reference corrections |
| v1.2 | Review round 2: **resolved the scale/time arithmetic contradiction** between O2 and §3.5 — measured all leg distances (§2.2, §3.2) and replaced the single 20× clock with a quantified model: ship 1:1, per-scenario geography scale k ∈ [8,32], real-time simulation clock plus player time-warp ≤ 8×; scenario redefined as one *leg* (12–25 min), routes become campaigns with harbour interludes; both scale deviations quantified with a scale-independent identification-range rule; new core systems — waiting for a fair wind (§3.6), the landmark navigation loop and "no charts" principle (§3.7), scenario definition-of-done (§3.8); sail polar split into luffing angle vs. best-VMG angle (§4.4); Scratch section corrected to a bidirectional, versioned protocol with cached-reporter constraint, port map, first-run bridge check (§6.2, Appendix B); landmark-visibility vs. culling technical pitfall (§7.2); classroom operations (§7.5); difficulty matrix with concrete parameters (§7.6); Apache-2.0 vs. marketplace-asset licensing conflict (§7.3); critical path (§9.3); gate owners and timeboxes (§9.2); golden-run regression, headless smoke and seamark-visibility tests (§11); decisions D7–D11; Appendices B–F |

**How to review:** the decisions that most need reviewer input are **§3.5 (scale model)**,
**§3.6 (waiting for fair wind)**, **§1.3 (scope)**, **§12 (decision register)** and
**§13 (open questions)**. A reviewer checklist is in Appendix F.

---

## 1. Vision and Objectives

### 1.1 Educational vision

The player experiences what a Viking helmsman (*styrimaðr*) experienced: sailing a real historical
route using **only the landmarks they can see, the wind they feel, and a side-mounted steering
oar (*stjórn*)**. No modern instruments, no GPS, no charts, no compass rose in the HUD beyond what
a Viking would plausibly have had. The game teaches:

1. The geography of the major Viking-age (c. 793–1066 AD) sea routes.
2. How landmark-based coastal navigation (piloting between known seamarks) works.
3. How a square-sail vessel interacts with the wind — why Vikings **waited for a fair wind**
   (*bíða byrjar*), tacked laboriously, or took to the oars.
4. The physical skill of steering with a quarter-mounted steering oar rather than a stern rudder.

### 1.2 Measurable objectives

| # | Objective | Success criterion |
|---|-----------|-------------------|
| O1 | Identify and document the most common Viking sea routes | Research documents with ≥ 6 routes researched and 4–6 selected, each with sources, landmarks, distances, prevailing-wind and tidal data |
| O2 | One playable UE scenario per route leg | ≥ 4 scenarios shipped; each scenario = one leg of 12–25 min at the agreed scale (D1); each route is a campaign of 3–5 legs with harbour interludes |
| O3 | Historically plausible wind and tide model | Per-scenario wind/tide derived from documented data; reviewers sign off at G4 |
| O4 | Physically plausible sail + steering-oar simulation | Sail polar validated against reconstruction data; two documented numbers — luffing angle and best-VMG angle (§4.4); leeway and asymmetric rudder forces modeled; G3 review passed |
| O5 | Scratch program controls the steering oar | Rudder angle set in Scratch reaches UE within 100 ms end-to-end; telemetry reporters return cached values without blocking |
| O6 | Learning outcomes assessed | Aligned assessment (Appendix E): pre/post quiz per scenario; ≥ 70% of playtesters improve their score; player-drawn sketch map exported as a teacher-assessable artifact |
| O7 | Runs on classroom hardware | 60 fps @ 1080p on GTX 1060-class; playable at low settings on an Intel-iGPU laptop (verified at G2b and pre-release) |

### 1.3 Scope and non-goals (v1.0 release)

**In scope:** single-player sailing and navigation on documented Viking routes; historically
informed wind, sea and tide; Scratch-based steering-oar control; harbour/waiting decisions;
briefings, debriefs, quizzes and a player sketch map; desktop PC.

**Explicit non-goals** (do not let these creep in):

- No combat, raiding or boarding mechanics.
- No multiplayer or per-oarsman crew AI (crew is a single energy/supplies abstraction).
- No VR in v1.0 (physics and camera kept VR-friendly; revisit post-release).
- No free roaming between scenarios (a free-sail sandbox *per scenario* is in scope).
- No mobile/console ports; no accounts, no online services, no analytics.
- No river navigation (the *Austrvegr* river legs are covered in briefings/debriefs only).

### 1.4 Historical framing and sensitivity

Raiding routes (S1) are presented factually, without glorifying violence: briefings state the
historical reality, foreground that these were also trade, settlement and exploration routes, and
avoid casualty counts or "score" derived from violence. All player scoring comes from navigation
quality (Appendix D). Text is reviewed at G1 for accuracy and tone. This matters for school
adoption and for the historian sign-off.

---

## 2. Phase 1 — Historical Research (the sea routes)

**Goal:** produce `docs/research/` material that is accurate and citable before any level art is
made. All route content (coastlines, landmarks, distances, sailing directions) must trace back to
this research.

**Scope note (v1.2):** at 0.5 FTE, fully researching 6 routes in 3–4 weeks is optimistic. Plan:
**full research depth on the 4 selected scenarios (S0–S3) in Phase 1**; S5 and S6 get summary
research now and full research just before their build in Phase 6.

### 2.1 Method

- Primary sources: sagas (*Egil's saga*, *Eiríks saga rauða*, *Grœnlendinga saga*, *Óláfs saga
  helga* — the last contains sailing directions from Norway to Greenland and Iceland), Ottar's and
  Wulfstan's accounts to King Alfred (c. 890), Adam of Bremen. Note explicitly in `navigation.md`
  that **Vikings had no charts and no written sailing directions** — route knowledge was oral
  (this drives §3.7).
- Secondary scholarship: Roesdahl (*The Vikings*), Graham-Campbell (*The Viking World*), Englert &
  Trakadas (eds.) on the Baltic, Crumlin-Pedersen on shipbuilding, work on the Uunartoq
  sun-compass fragment (its function is **debated** — treat as optional aid, not established fact).
- Nautical data: modern pilot charts (US NGA / UK Admiralty) for prevailing wind roses by season,
  cross-checked against ERA5 seasonal wind statistics; used as a proxy for the Medieval Climate
  Anomaly (c. 950–1250) with an explicit caveat that medieval warming may have shifted patterns.
  In-game framing: "plausible", not "exact".
- Tide data: published tidal-stream atlases and tide tables for the North Sea, Norwegian coast,
  Limfjord/Skagerrak and Baltic (Baltic tides are negligible — itself a teaching contrast).
- Reconstruction sailing data: sea trials and voyage logs of the Viking Ship Museum Roskilde
  reconstructions — *Ottar* (Skuldelev 1 knarr) and *Sea Stallion from Glendalough* (Skuldelev 2
  longship, incl. the 2007–08 Roskilde–Dublin voyage) — plus the *Viking* (1893) and *Snorri*
  (1997) voyages. These supply the numbers for speed, leeway and closeness-to-wind (§4.4).

### 2.2 Candidate routes (research list)

1. **The North Sea route** — western Norway (Rogaland) → Shetland → Orkney → Hebrides → Ireland
   (Dublin, founded c. 841). Classic summer corridor, mostly coastal after landfall on Shetland.
2. **The Limfjord transit route** — through the Limfjord across northern Jutland (open to the
   North Sea in the Viking age), avoiding the dangerous sail around Skagen; links the North Sea to
   the Kattegat. Related hub: Hedeby (Haithabu) on the Schlei, with the overland portage to the
   Treene/Eider system.
3. **The North Atlantic settlement route** — Norway (Bergen area) → Shetland/Faroes → Iceland
   (Breiðafjörður) → Greenland (Eiriksfjord). Governed by the **westerlies**: outbound legs run
   with the wind, homeward legs fight it — historically why return voyages ran more southerly.
4. **The Vinland extension** — Greenland → Vinland (L'Anse aux Meadows, c. 1000). Fog, icebergs,
   Labrador Current.
5. **The Baltic trade route** — Hedeby/Birka → Gotland (Visby) → Gulf of Finland → the
   *Austrvegr* river systems toward Novgorod (Holmgarðr) and Miklagarðr. Open-water legs only.
6. **The Norwegian "North Way"** — Bergen → Lofoten → (Ottar's voyage to the White Sea).
   Fjord piloting par excellence.

**Measured leg distances (great-circle, v1.2 — used for the scale model in §3.5):**
Bergen→Shetland 358 km; Shetland→Faroes 366 km; Faroes→SE Iceland 491 km; SE Iceland→Breiðafjörður
378 km; **route total ≈ 1,593 km via Shetland/Faroes** (direct Bergen→Breiðafjörður 1,512 km).
At a realistic 6 kn knarr cruise that is ~144 h of pure sailing — historically 1–3 weeks including
weather delays. This is the arithmetic that forces the scale/time decisions in §3.5.

### 2.3 Deliverables of Phase 1

- `docs/research/routes.md` — per route: map reference, harbours, seamarks visible from sea
  (mountain profiles, islands, headlands, cairns), leg distances and bearings, season, notes.
- `docs/research/wind.md` — wind roses per route per season (pilot charts + ERA5), sources, MCA
  caveat, and per-scenario recommended variability.
- `docs/research/tides.md` — tidal regimes, stream strengths/directions at scenario waypoints,
  historical notes on Viking tidal knowledge (harbour tides, waiting for the fair tide).
- `docs/research/ships.md` — knarr vs longship vs karvi; sail area, displacement, hull lines,
  steering-oar geometry (quarter mount, tiller, leverage); sources for every number.
- `docs/research/navigation.md` — landmark piloting: leading marks, transits, hand bearings
  (*fingrar*), sounding, swell and bird behaviour, the sun-compass debate, latitude by sun height;
  how each maps to an in-game mechanic (§3.7).

**Review gate G1:** historian/qualified reviewer signs off the research documents before scenario
construction begins (exit criteria §9.2).

---

## 3. Phase 2 — Scenario Design

### 3.1 Route selection criteria

- Variety of navigation style (open-sea dead reckoning vs fjord piloting vs archipelago transit).
- Variety of wind/tide regime (following westerlies, headwinds, sheltered reaches, tide gates).
- Feasibility of terrain generation at the chosen scale (D1) within the session-length target (O2).

### 3.2 Proposed scenario slate

Each scenario is **one leg** of a route; a route is a **campaign** of legs chained by harbour
interludes (§3.6). Subject to G1 review.

| # | Scenario (leg) | Ship | Navigation lesson | Wind/tide challenge | Real leg length |
|---|---|---|---|---|---|
Leg lengths are measured great-circle distances (v1.2, verified by computation), with the
resulting in-game length and session time at the proposed scale (§3.5):

| # | Scenario (leg) | Ship | Navigation lesson | Wind/tide challenge | Real leg | In-game @ k | Session |
|---|---|---|---|---|---|---|---|
| S0 | **Tutorial: home waters** (fictionalized sheltered fjord circuit, Roskilde-fjord-like) | Karvi | Steering-oar asymmetry, reading the pennant, first transit, lookout bearings | Gentle steady breeze; safe water | ~25 km circuit | 3.1 km @ k=8 | **17 min @1×** |
| S1 | **Rogaland (Stavanger) → Shetland (Lerwick)** (first leg of the Ireland route) | Longship | Open-sea departure, dead reckoning with swell, making an island landfall | SW winds fair and foul; tide races off headlands | 409 km | 12.8 km @ k=32 | **17 min @4×** |
| S2 | **Limfjord transit** (Thyborøn → Aalborg) | Knarr (cargo) | Narrow-channel piloting, transits, shallow water, using the tide | Local sea breezes; tidal streams through the narrows | 111 km | 3.5 km @ k=32 | **19 min @1×** |
| S3 | **Bergen → Shetland** (first leg of the Iceland route) | Knarr | Running before the westerlies; latitude sailing; landfall by swell and birds | Prevailing westerlies — the core "wind vs. sail" lesson; North Atlantic swell | 358 km | 11.2 km @ k=32 | **15 min @4×** |
| S4 | **Vinland legs** (stretch/cut candidate; saga route Greenland → Helluland → Markland → Vinland) | Knarr | Fog, icebergs, landfall by bird flight and swell | Cold northerlies; fog visibility; Labrador Current | 530–1,001 km per saga leg (~2,140 km total) | 17–31 km @ k=32 | 11–21 min @8×; 22–42 min @4× (see cut note) |
| S5 | **Birka → Visby (Gotland)** (Baltic) | Longship (trade) | Archipelago piloting between islands | Moderate shifty Baltic winds; negligible tide (contrast with S2) | 194 km | 6.1 km @ k=32 | **16 min @2×** |
| S6 | **The North Way** (Molde → Kristiansund coastal hop) | Karvi | Fjord piloting, transits, headland rounding | Katabatic and channel-accelerated winds; strong tidal streams in sounds | 50 km | 3.1 km @ k=16 | **17 min @1×** |

**Note on S4:** at k=32 the saga legs run 11–21 min at the maximum 8× warp (22–42 min at the 4×
warp used by S1/S3; per-leg numbers from `tools/route_geometry.py`). Fitting the target therefore
requires sustaining maximum warp for the entire session, but time-warp auto-reverts to 1× on
steering-oar input and hazard proximity (§3.5) — and the S4 legs are full of fog and ice hazards
— so realistic session times run well over the 25-min target, and each leg needs its own
fog/ice content. If S4 is kept, it must be re-scoped as a shorter coastal leg (e.g. Markland
landfall only) rather than an ocean crossing. This is the arithmetic reason S4 is first on the
cut list (§10).

### 3.3 Common scenario structure

1. **Briefing:** the historical situation; the route given as an **oral description** a Viking
   would know ("sail west until the mountain with the saddle profile bears north of you…") — no
   chart, no bearings list (§3.7); crew, supplies, tide state, season.
2. **Voyage planning decision:** wait for a fair wind or sail now (§3.6).
3. **Departure:** clear the harbour mouth using landmarks and, where relevant, the fair tide.
4. **Legs within the scenario:** 1–3 sub-legs, each defined by a seamark pair (transit) the player
   must find and hold; historically real hazards (reefs, shoals, lee shores, tide races, ice).
5. **Weather events:** scripted wind shifts from the research wind-rose (a backing wind before
   the Shetland landfall forces the player off the rhumb line — as it did historically).
6. **Failure and recovery (learning loop, not punishment):**
   - Grounding → hull damage; kedging off or waiting for a rising tide.
   - Dismasting in a squall (sail kept up in too much wind) → continue under oars.
   - Swamping/capsize or wrecking on a lee shore → voyage failed.
   - Every failure triggers a debrief explaining what historically happened to crews in that
     situation, then instant retry. Failure is a teaching moment.
7. **Landfall:** judged by proximity to the historical landing place, hull damage, supplies,
   elapsed time and crew energy.
8. **Debrief:** the real history of that crossing; score (Appendix D); replay of the sailed track
   overlaid on the real route; the player's sketch map (§3.7) saved as an artifact; post-scenario
   quiz.

### 3.4 Terrain and environment

- Real elevation/bathymetry (GEBCO + Copernicus/SRTM) imported as heightmaps and resampled to the
  scenario scale (D1); coastlines matched to modern data with documented per-scenario notes where
  coastlines materially changed (Limfjord's western opening, Schlei/Hedeby).
- Distinctive seamarks modeled individually (mountain profiles, headland cairns/*hörgr*).
- Period-correct where affordable: no modern lighthouses, buildings, buoys or shipping.
- Water: UE Water plugin ocean + custom Gerstner wave field, sized per scenario from research
  (North Atlantic swell vs Baltic chop — different significant wave heights and periods).

### 3.5 World scale and time — the critical design decision (D1)

**The problem, stated with numbers (§2.2):** real legs are 25–600 km at ~6 kn. A 358 km leg takes
32 h of sailing. UE cannot hold 1:1 route geometry, and O2 targets 12–25 min sessions. Something
must give, and it must give in a *quantified, documented* way.

**Options assessed:**

| Option | Pros | Cons | Verdict |
|---|---|---|---|
| A. Scale geography down; ship stays 1:1 | Continuous sailing; **waves and ship physics stay 1:1 and physical** (literature polar applies directly); one level per leg | Landmarks are small in absolute terms; ship looks large relative to terrain | **Proposed default** |
| B. Waypoint-linked 1:1 sub-levels | Real geometry, real physics | Breaks continuity — you lose your transit at every load; high content cost | Rejected for a navigation game |
| C. Full 1:1 with World Partition streaming | Maximum realism | Enormous cost; days of sailing per session | Infeasible |
| D. True Froude model (scale ship *and* world) | Physically self-consistent | Ship speed scales √s → legs get *longer*; polar must be re-derived; a 1.5 m ship is unplayable onboard | Rejected |

**Proposed scale model (to be prototyped in Phase 3 and confirmed at G3):**

- **Ship: 1:1.** Real length, real sail area, real speed, real waves (height and period).
  Consequence: all sail/hull/rudder coefficients can be taken directly from the literature and
  reconstruction trials — no re-derivation, and the accuracy claims in §4 stay honest.
- **Geography: uniform 1:k** (horizontal *and* vertical, so angular silhouettes of seamarks are
  preserved and the horizon formula stays self-consistent).
- **k is per-scenario, clamped to [8, 32]**, chosen so the leg sails in **12–25 min at 1×** where
  possible (sheltered legs: k = 8–16; open-water legs: k = 32 plus warp). Per-scenario k is
  recorded in the scenario design doc and the `ScenarioDefinition` asset (Appendix C). A single
  global k would feel more consistent across scenarios but forces either 60-minute open-water legs
  or toy-sized sheltered legs; the clamp keeps the variation within a tolerable range.
- **Time: two clocks.**
  - *Simulation clock* — always real time. Ship motion, sail response, gusts, waves, steering-oar
    rate limit. Nothing here is ever accelerated, so physics stays stable and the feel stays right.
  - *Voyage clock* — drives weather patterns, tide phase, sun position, supplies. Runs at the
    player-controlled **time-warp** factor (1× / 2× / 4× / 8×, D7).
- **Time-warp behaviour:** uniform fast-forward of everything (ship, waves, wind) capped at 8×;
  auto-reverts to 1× on any steering-oar input, on hazard proximity, or on entering a channel
  (a "warping" indicator is always on screen). This is the standard sailing-sim compromise; its
  visual acceptability is an explicit G3 review item.
- **Leg-length rule:** prefer legs that sail in ≤ 25 min at 1× (sheltered/coastal scenarios need no
  warp at all); use warp only for long open-water legs.

**Worked example (S3, Bergen → Shetland, 358 km real, k = 32):**

| Quantity | Real world | In game (k=32) | Notes |
|---|---|---|---|
| Leg distance | 358 km | 11.2 km | One UE level; World Partition streaming |
| Sailing time @ 6 kn (11.1 km/h) | 32.2 h | 60 min @1× → **15 min @4×** | Meets O2 |
| 1,000 m seamark peak | 1,000 m | 31 m | Angular silhouette preserved by uniform scaling |
| Horizon distance to that peak from a 5 m eye | 130.5 km | 30.2 km | See deviation 2 below (both include +8% refraction) |
| S2 Limfjord leg, 111 km real | 111 km | 3.5 km → **19 min @1×** | No warp needed |
| S0 tutorial circuit, 25 km real | 25 km | 3.1 km @ k=8 → **17 min @1×** | No warp needed |

**Two quantified deviations this introduces — both must be documented in `docs/design/physics.md`
and compensated by design, not hidden:**

1. **The ship looks large relative to terrain, and this gets worse as k grows.** With geography at
   1:k and the ship at 1:1, a 24 m knarr sails past a 1,000 m peak rendered as 1000/k metres
   (62 m at k=16, 31 m at k=32). This is in direct tension with the session-length target: larger
   k shortens legs but increases the "toy-ness". Mitigation: accept it (onboard views, physics and
   seamark *angles* all remain correct, which is what the lessons depend on) and evaluate it
   visually at G3 with k ∈ {8,16,32} side by side; if unacceptable, either lengthen sessions with
   more warp at a smaller k, or scale the ship by s ∈ [0.5, 1] with Froude re-derivation of speeds
   (cost: the polar must be re-validated, and legs get longer). Tunable constants `WorldScaleK`
   and `ShipScaleS` centralize this so the choice is a data change, not a refactor.
2. **Seamarks become visible over a *larger fraction* of each leg than in reality.** Under uniform
   scaling, distances shrink by k but horizon distances shrink only by √k. Real: the 1,000 m peak
   is usable for 130.5/358 ≈ 36% of the S3 leg. In game at k=32 with a 1:1 eye height it would be
   30.2/11.2 ≈ 270% — visible for the whole leg, which destroys the progressive-landfall lesson.
   **Mitigation (required, not optional):** an explicit per-landmark **identification range**
   defined *as a fraction of leg length*, which makes it scale-independent and self-tuning:

   > `IdentRange = (real horizon distance to mark ÷ real leg length) × in-game leg length`,
   > then capped by the scenario's weather/haze visibility.

   Worked values for S3 (real leg 358 km, in-game 11.2 km at k=32, 5 m eye height):

   | Seamark class | Real height | Real horizon distance | Fraction of leg | In-game ident. range |
   |---|---|---|---|---|
   | Major peak | 1,000 m | 130.5 km | 36.5% | **4.1 km** |
   | Island / skerry group | 200 m | 63.1 km | 17.7% | **2.0 km** |
   | Headland / low profile | 50 m | 35.9 km | 10.0% | **1.1 km** |
   | Cairn / *hörgr*, small skerry | 3 m | 15.3 km | 4.3% | **0.48 km** |

   All values include standard atmospheric refraction (+8%, per the horizon formula in §7.2 and
   `docs/research/navigation.md`) and are generated by `tools/route_geometry.py --ident S3` —
   regenerate from the tool, do not hand-edit.

   Haze, rain and fog (all historically accurate) are the realism knobs on top of these ranges.
   The sighting system (§3.7) uses them, `tools/` computes them per scenario from the heightmap
   and leg geometry, and the automated seamark-visibility test (§11) enforces them.

**Deliverable per scenario:** one-page design doc (`docs/scenarios/S0..S6.md`) + blockout level.

**Review gate G2a:** design docs reviewed; blockouts playable with grey-box terrain.

### 3.6 Harbour, supplies and waiting for a fair wind (core system)

Historically the most consequential Viking navigation decision was **whether to sail at all today**
— sagas repeatedly record crews waiting days or weeks for a favourable wind (*bíða byrjar*). This
must be a real mechanic, not flavour:

- **Harbour state:** ship moored; time passes on the voyage clock at high warp (default 8×, up to
  "wait until the wind is fair" one-click); crew energy and hull repairs restore; **supplies
  drain**.
- **Supplies:** a single abstraction (fresh water, food, trade goods) sized per scenario from
  `ships.md` capacity data. Sailing in foul weather costs supplies while making little progress;
  waiting costs supplies while making none. Running out is a failure state with a historical
  debrief.
- **Weather forecast (period-authentic):** no forecast is given. The player reads the sky, swell
  direction, cloud types and barometric *feel* cues (a "the air feels heavy" crew line) — the same
  evidence a Viking had. Instructor mode shows the actual wind-rose probabilities from `wind.md`.
- **Decision scoring (Appendix D):** sailing into a foul wind and being driven onto a lee shore
  scores worse than waiting two days and crossing cleanly. This is the single most important
  lesson the game can teach about Viking seamanship, and it is measured.

### 3.7 The landmark navigation loop (core system)

Design principle: **Vikings had no charts and no written sailing directions.** Therefore the game
provides no chart, no plotted route, no bearing list and no GPS-style position readout. Instead:

1. **Oral route description** in the briefing (a short saga-style text, readable aloud; audio
   narration included).
2. **Lookout (*útkik*):** the player stations a crew member in the bows / climbs the mast; this
   raises eye height and thus horizon distance (§3.5), and yields spoken reports ("land fine on the
   starboard bow, two fingers above the water"). Reports are the only position information.
3. **Hand bearings (*fingrar*):** aiming at a seamark, the player reads its height in "fingers"
   above the horizon — an authentic, coarse angular measure that also teaches *why* bearing rate of
   change reveals range.
4. **Transits / leading marks:** two marks held in line to stay in a channel; the game highlights
   the alignment only after the player has found it (discovery, not hand-holding).
5. **Lead line:** sounding depth over the keel, matching the bathymetry — essential in S2/S6
   shallow-water legs; also gives bottom-character flavour ("grey sand").
6. **Player sketch map (the game's only "chart"):** the player may plot what they believe they have
   seen on a deliberately crude vellum sketch — marks, rough bearings, their own track. Exported
   with the debrief as a teacher-assessable artifact (O6) and compared against the true track.
7. **Sun-compass (optional, D9):** the Uunartoq-type disc as an *optional* aid, offered with an
   explicit in-game note that its function is debated by scholars. Default off for S0–S2, available
   in S3/S4.
8. **Sun/stars:** sun altitude gives rough latitude on clear days (taught in S3); star recognition
   for night sailing (difficulty option, D4).

### 3.8 Scenario definition of done (content checklist)

A scenario is complete when all of the following are verified:

- [ ] Terrain at scenario scale imported; coastline matches research within documented tolerance
- [ ] All seamarks from `routes.md` present, modeled, and passing the visibility test (§11)
- [ ] No anachronisms (visual audit checklist signed by the reviewer)
- [ ] Weather script + tide model match `wind.md` / `tides.md`
- [ ] Harbour/waiting loop functional with supplies tuned to the leg length
- [ ] All failure states reachable, recoverable or debriefed, with historical text
- [ ] Briefing (oral route description), debrief (real history) and 4–6 quiz items authored,
      mapped to the scenario's learning objectives (Appendix E)
- [ ] Telemetry recording + deterministic replay verified (seed → same result)
- [ ] 60 fps @ 1080p on target spec; low-settings path verified (O7)
- [ ] Playtested by ≥ 3 people from the target audience; top issues triaged
- [ ] Localized strings present for launch languages (D6)

---

## 4. Phase 3 — The Ship

### 4.1 The vessel

- **A single square sail** of wool (*vaðmál*) on a yard that can be raised/lowered (also used to
  reef) and slightly braced across the mast — historically limited to roughly ±15–20° from square.
- **A large steering oar (side-rudder)** on the **starboard quarter** — hence *stjórnborði*
  ("steering-board side", starboard) vs. *bakborði* (port, the side the helmsman had his back to).
  It pivots on a withy/pin; the helmsman works a tiller. **This is the player's only steering
  control, and it is driven from Scratch (§6).**
- **Oars** as a low-speed fallback: rowing speed is crew-power-limited (well below hull speed) and
  drains crew energy, which also drains when baling, kedging or sailing through storms.

### 4.2 Ship physics model

UE's Chaos vehicle framework is not suitable for a sailing vessel; we implement a custom rigid-body
simulation:

- **Buoyancy:** sample-based hull buoyancy (8–16 points below the waterline) → realistic pitch/roll
  from waves and cargo.
- **Sail forces:** aerodynamic surface with a polar derived from published square-sail aerodynamics
  and reconstruction sea-trial data (§4.4). Behaviours that must be right:
  - Best on a **run or broad reach**; poor close-hauled.
  - Drive collapses inside the **luffing angle** (§4.4).
  - Power depends on trim: yard height (reefing), brace angle, sheet position.
  - Lift + drag decomposition → drive force and heeling moment.
- **Hull hydrodynamics:** directional drag polar; lateral resistance (a knarr's deeper hull resists
  leeway better than a longship's); realistic speed limits per hull form.
- **Leeway:** 5–15° to leeward close-hauled — the player must aim upwind of the mark. Core
  teaching point; also the reason the *best-VMG* angle (§4.4) matters more than the luffing angle.
- **Steering-oar physics:** blade lift ∝ angle of attack to local flow → **yaw moment** (long lever
  arm, but mounted on one side only), small roll and a speed penalty when hard over. The off-centre
  mount means a centred oar still imparts slight yaw — helmsmen compensated with slight weather
  helm. We model this asymmetry because it is historically real and pedagogically useful (the
  player discovers that "rudder amidships" does not mean "goes straight").
- **Windage** of hull, mast, rigging and shields-on-rails.
- **Apparent wind** computed per physics tick from ship velocity and true wind; sail forces always
  use apparent wind. A wool pennant on the yard shows apparent-wind angle, exactly as Vikings used
  such telltales.
- **Scale note (D1):** because the ship stays 1:1, no coefficient re-scaling is needed; `WorldScaleK`
  affects only geography and the visibility model (§3.5).

### 4.3 Sail/rudder interactions that must be simulated correctly

| Real behaviour | In-game model |
|---|---|
| Steering oar loses authority at low speed | Rudder effectiveness ∝ flow speed²; slow ship = sluggish oar, must row |
| Heeling lifts the blade partly out of the water | Blade submergence vs. heel angle → reduced authority when heeled |
| Tacking a square-rigger is hard; Vikings often **wore ship** (gybed) | Both supported; tacking too close stalls the ship; wearing costs ground to leeward |
| Sail luffing warns you're too close to the wind | Cloth/shader-driven luff + collapse of drive force + audible luff crack |
| Accidental gybe running dead downwind in a swell | Yard can slam across if wind catches the wrong side; risk scales with sea state |
| Over-canvassed in a squall | Heel beyond ~35° → broaching/water aboard → possible dismasting (§3.3) |

### 4.4 The sail polar: two numbers, not one (v1.2 correction)

v1.1 asserted a single "60° off the apparent wind" floor. That conflates two distinct, both
important quantities, and understates what replica trials suggest. The model must expose both:

- **Luffing angle (θ_luff):** the angle off the **true** wind inside which the sail shivers and
  drive collapses to ~zero. Replica and published data suggest square sails can hold roughly
  **50–60° off the true wind** in favourable conditions, worse in a seaway. **Design default:
  55° ± 5°, to be fixed by the G3 validation, not asserted now.**
- **Best-VMG angle (θ_vmg):** the course that maximizes velocity made good *to windward*. This is
  operationally 10–15° wider than θ_luff. Sailing at θ_luff feels heroic and goes nowhere — the
  exact mistake learners make, and the exact lesson the game should teach.
- All angles are defined against **true** wind in the spec and displayed against **apparent** wind
  in the HUD/instructor mode, with the distinction documented (a classic source of error).
- **G3 validation procedure:** automated sweep of true-wind angle 0–360° in 1° steps at three wind
  speeds; record drive force, heel, leeway; extract θ_luff (drive = 0) and θ_vmg (max upwind VMG);
  compare the resulting polar and leeway table against the reconstruction reference table in
  `ships.md` within a stated tolerance; an experienced sailor or maritime historian reviews feel.
- **Assessment hook (Appendix E):** a quiz item and a telemetry KPI both check whether the player
  sails at θ_vmg rather than pinching at θ_luff.

**Deliverables:** `docs/design/physics.md` (equations, coefficients, sources, the two scale
deviations from §3.5), `AVikingShip` + `SailComponent`, `SteeringOarComponent`,
`BuoyancyComponent`, and an instrumented sandbox map with CSV telemetry export.

---

## 5. Phase 4 — Wind, Currents and Sea State

### 5.1 Wind requirements

- **Historically accurate prevailing directions** per scenario from `docs/research/wind.md`.
  Example: S3 (Bergen→Iceland) is dominated by **westerlies** — historically exactly why the
  settlement route worked.
- Wind has **direction, speed, gustiness and spatial structure**: channel acceleration between
  islands, coastal sea breezes, wind shadow in the lee of mountains and icecaps, katabatic
  drainage winds in fjords at dawn.
- **Deterministic and seedable** so a given "day" is reproducible for testing, replays and
  classroom comparison ("same weather, different helmsmen").
- **Readable without instruments:** sail set and luffing, pennant direction, wave amplitude and
  whitecaps, foam streaks, rigging hum and wave slap. No numeric wind readout in normal play;
  instructor mode shows vectors.

### 5.2 Wind implementation

- `WindSubsystem::GetTrueWindAtLocation(FVector)` — blends the scenario prevailing wind with
  spatial modifiers (orographic shading, channel jets) and temporal modifiers (seeded analytic
  noise gust field; scripted shifts from the weather script).
- Weather scripts key moments to scenario progress (a backing wind before the Shetland landfall;
  a fog bank off Vinland) via data tables. The weather clock runs on the voyage clock (time-warp,
  D7); sail and gust response always run on the simulation clock.
- Sails, pennants, particles, audio and sea state all read from this one subsystem — exactly one
  source of truth for wind.

### 5.3 Currents and tides

- `CurrentSubsystem::GetCurrentAtLocation(FVector, FDateTime)`:
  - **Tidal streams:** per-scenario harmonic model — a small constituent set (M2 + S2 is sufficient
    at this fidelity) fitted to `docs/research/tides.md`, giving ebb/flood direction and strength
    along channels (critical for S2 and S6; near-zero in the Baltic S5, itself a teaching point).
  - **Major currents:** slowly varying fields where they matter (Norwegian Coastal Current in S6,
    Labrador Current in S4, North Atlantic Drift in S3).
- Currents affect the over-ground track (water track vs. ground track shown in instructor mode
  only), grounding depth via tide height, and harbour approaches — catching the fair tide is a
  real planning decision in the briefing.

**Review gate G4:** per-scenario wind and tide tables checked against the research docs;
instructor-mode debug view demonstrated.

---

## 6. Phase 5 — Scratch Steering-Oar Controller

### 6.1 Concept

The steering-oar position is **not** controlled by keyboard/mouse in the standard setup: it is
driven by a **program written in Scratch**, acting as the crew member working the oar. This serves
the learning goal (players write logic — "if we are drifting toward the lee shore, put the oar
over") and lets the game be used in coding classes.

### 6.2 Architecture (Scratch ⇄ Bridge ⇄ Unreal)

```
        rudder commands (POST /cmd, 10 Hz)              UDP 127.0.0.1:9870
┌───────────────┐ ───────────────────────────► ┌──────────────┐ ──────────────► ┌───────────────┐
│  Scratch 3    │      HTTP 127.0.0.1:9871     │ Local bridge │                 │ Unreal Engine │
│  (TurboWarp,  │ ◄─────────────────────────── │ Node.js LTS  │ ◄────────────── │ 5 (C++ subsys)│
│  custom ext.) │   GET /state (poll, cached)  │ or Python    │  UDP :9872      │               │
└───────────────┘                              └──────────────┘                 └───────────────┘
   30 fps script loop                          CORS on, bound to                 non-blocking recv
                                               127.0.0.1 ONLY                    in Tick → oar
```

- **Scratch editor (D2, week-1 spike):** the official scratch.mit.edu editor does **not** load
  arbitrary custom extensions from a URL. Options in preference order: (a) **TurboWarp** desktop
  (Scratch-compatible, loads custom extensions by URL, classroom-friendly); (b) self-hosted
  `scratch-gui` fork with the extension built in; (c) companion-app model (Scratch Link-style) if
  extension loading fails. The bridge protocol is identical for all three. TurboWarp version is
  pinned in `docs/integration/scratch-bridge.md`.
- **Scratch-side blocks:**
  - `set rudder to ⟨angle⟩°` (−45°…+45°, port/starboard) — the primary control
  - `set sail height ⟨0-100⟩`, `brace the yard ⟨angle⟩` (stretch goal)
  - Sensing reporters exposing **only what a Viking crew could sense** (D3):
    `heading`, `pennant angle`, `speed through water`, `depth under keel`,
    `bearing to ⟨visible seamark⟩` (only marks inside their identification range, §3.5),
    `bridge connected?`
- **Implementation constraint that shapes the design (v1.2):** Scratch reporter blocks are
  **synchronous** — they cannot await a network call. Therefore the extension must poll the bridge
  on a background interval (default 10 Hz) and reporters must return the **latest cached value**
  plus an `age (ms)` reporter so student programs can detect stale data. This is specified in
  Appendix B, not left to implementation.
- **Bridge:** ~150-line local service. HTTP for Scratch (CORS enabled, bound to **127.0.0.1 only**
  — no network exposure), forwarding commands as UDP to UE and buffering UE telemetry for Scratch
  polling. Shipped as a one-click executable/script. Single Scratch client assumed; a second
  client is rejected with a clear error.
- **Unreal side:** `ScratchBridgeSubsystem` using `FSocket` (UDP, non-blocking receive in Tick),
  applying the latest rudder angle at the physics tick with smoothing (rate limit ~30°/s, matching
  how fast a helmsman can move a heavy oar) and a deadband. Out-of-range values are clamped and
  logged. A **500 ms heartbeat timeout** → oar goes amidships + on-screen warning (simulating a
  slipped steering oar — historically on-theme and a safe failure mode).
- **Protocol versioning:** every message carries `v`; on connect the bridge and UE exchange a
  handshake with versions and capabilities and refuse to run on mismatch (prevents silent
  classroom breakage when versions drift). Full schemas in Appendix B.
- **First-run check:** the game's main menu shows bridge status (Detected / Not detected), the port,
  a one-line setup instruction and a "Test oar" button that wiggles the oar when Scratch sends a
  command. Classrooms must never have to debug this blind.
- **Latency budget:** Scratch HTTP round trip 50–100 ms typical; bridge→UE UDP < 5 ms. O5 requires
  < 100 ms end-to-end, verified by a timestamped echo test in the sandbox map.
- **Fallback:** keyboard control (arrow keys) behind `--solo` for development and classrooms without
  Scratch; oar behaviour is identical regardless of input source.
- **Two-crew mode (stretch, D10):** a genuinely strong classroom activity — one student helms from
  Scratch on a second machine, another navigates in UE. Requires the bridge to bind to LAN with an
  explicit `--lan` opt-in flag, documented firewall rules, and a clear warning that this exposes
  the port on the local network. Off by default; localhost-only is the shipped default.
- **Privacy by design:** no accounts, no analytics, no outbound traffic; all telemetry stays on
  localhost and in local save files — safe for classroom use with minors (GDPR) with no
  data-processing agreement required.

### 6.3 Example Scratch programs (deliverables, teaching material)

1. `rudder-hold-course.sb3` — proportional control: rudder ∝ (target heading − ship heading).
2. `rudder-avoid-lee-shore.sb3` — if pennant angle + seamark bearings show drift toward shore,
   steer upwind.
3. `rudder-hold-transit.sb3` — keep two seamarks in line (uses the bearing reporters).
4. Open exercise: program the harbour-mouth approach.

**Deliverables:** `scratch/` (extension source, bridge service, example `.sb3` files) and
`docs/integration/scratch-bridge.md` (protocol, schemas, setup, troubleshooting).

**Review gate G5:** D2 validated by a working spike; latency and heartbeat tests pass; example
programs run by a non-developer on a clean machine.

---

## 7. Phase 6 — Unreal Engine Technical Architecture

### 7.1 Project layout

- UE 5.4+ (exact version pinned at G0, recorded in README), C++ core (physics, wind, currents,
  bridge) + Blueprint level scripting and UI.
- Modules: `GameCore` (ship, sail, oar, buoyancy), `Weather` (wind, currents, sea state),
  `Bridge` (UDP/Scratch), `Learning` (scenario state machine, briefing/debrief, quiz, sketch map,
  telemetry, scoring).
- Data-driven scenarios: each level driven by a `ScenarioDefinition` data asset (schema in
  Appendix C) so new scenarios are content work, not code.

### 7.2 Key systems

| System | Approach |
|---|---|
| Ocean/waves | UE Water plugin + custom Gerstner wave component; height/period per scenario from research; wave animation always on the simulation clock |
| Ship simulation | Custom rigid body + buoyancy samplers (§4.2) |
| Wind | `WindSubsystem` (§5.2) — single source of truth |
| Currents/tides | `CurrentSubsystem` (§5.3) |
| Seamark sighting | Identification range from the §3.5 fraction-of-leg rule, capped by weather visibility. Horizon: d(km) ≈ 3.57·(√h_eye + √h_mark), heights in metres; +~8% for standard refraction. Lookout/mast climb raises h_eye; ranges computed per scenario by `tools/` |
| **Long-range visibility vs. culling** | **Known UE pitfall:** distant-object culling, HLOD and draw-distance settings will silently hide seamarks at 5–9 km, breaking the core mechanic. Mitigation: landmark actors exempt from distance culling, forced HLOD representation at range, per-scenario automated visibility test (§11) run in CI |
| Time-warp | Voyage clock at 1×/2×/4×/8× (D7); physics substepping; auto-revert to 1× on oar input or hazard proximity; on-screen indicator |
| Night/day | Full cycle; night sailing much harder — most Vikings anchored or lay to. Per-scenario rule option (D4) |
| Audio | Rigging hum, wave slap, sail-luff crack, hull creaks mixed as the **primary** wind and stress cues; music only in menus/briefings. All audio cues have visual equivalents |
| Camera & comfort | **Seasickness options are mandatory for a rolling-ship game:** stabilized horizon camera, roll/pitch damping slider, no forced head-bob, FOV control, optional "calm sea" accessibility mode |
| Save/replay | Full telemetry per run; deterministic replay from seed; export run report (CSV/JSON) |
| Localization | All UI/narrative text in localization tables from day 1 — **no hard-coded strings**; EN/ES/DA initially (D6); audio narration for briefings; dyslexia-friendly font option; target reading age recorded per string |
| Accessibility | Instructor mode (vectors, exact telemetry, HUD); colour-blind-safe palette; subtitles; remappable keyboard fallback |

### 7.3 Content pipeline and licensing

1. Route research → waypoints + seamark list.
2. Elevation/bathymetry tiles → `tools/` resample-to-scale → UE landscape.
   - **Data licensing:** GEBCO (CC BY 4.0 — attribution), Copernicus DEM (free, attribution),
     SRTM (public domain), ERA5 (Copernicus licence). Attributions collected in
     `docs/ATTRIBUTION.md` and the credits screen from day one.
3. Seamark and ship models (Blender → UE).
4. Scenario data asset authoring + weather/tide script.
5. Playtest → tune wind, warp and identification ranges.

**⚠ Licensing conflict to resolve at G0 (v1.2):** this repo is **Apache-2.0**. Unreal Marketplace
and Quixel/Fab assets are generally **not redistributable** under an open-source licence and carry
their own EULAs. Options: (a) keep redistributable assets out of the public repo and document a
setup script that fetches them locally; (b) restrict the project to CC0/CC-BY assets and
engine-provided content only; (c) relicense the repo. **Recommendation: (b) for anything committed,
with (a) as an escape hatch** — this keeps the project genuinely open for schools.

### 7.4 Platform, repository and build infrastructure

- **Target platform:** Windows 10/11 desktop first (classroom reality); macOS/Linux verified but
  not primary. **Min spec:** 60 fps @ 1080p on GTX 1060-class; must boot and run at low settings
  on an Intel-iGPU laptop (O7). Confirmed at G0.
- **Repository layout:**
  ```
  ├── docs/      # this plan; research/, design/, integration/, scenarios/
  ├── ue/        # UE project (VikingNav.uproject); Content/ via Git LFS
  ├── scratch/   # extension, bridge service, example .sb3 programs
  ├── tools/     # heightmap import/resample, wind & tide data processing
  └── README.md
  ```
- **Git LFS** for `ue/Content/**`; standard UE `.gitignore`/`.gitattributes`. If asset volume
  outgrows LFS practicality, evaluate Perforce or a DVC-backed store at G0.
- **Tooling spike in Phase 1 week 1 (v1.2):** the heightmap → scaled-landscape pipeline is on the
  critical path (§9.3) and is the least-proven part of the content plan. Prototype it on one S3
  tile before committing the schedule.
- **UE licensing:** standard EULA; royalty-free under the $1 M threshold — expected free for an
  educational release, noted for the record.
- **Distribution:** itch.io / direct installer for schools (no Steam requirement in v1.0);
  packaging via UE's standard pipeline; CI packaging on tagged releases (GitHub Actions
  self-hosted runner with UE installed, or manual — decided at G0).

### 7.5 Classroom operations (v1.2, new)

Real classroom use imposes requirements that are cheap to design for early and expensive to add
later:

- **Session reset:** one-click "restart leg" and "reset scenario" (no menus to dig through);
  kiosk mode that boots straight into a chosen scenario.
- **Sequential students on one PC:** lightweight local session slots (no accounts) so a class can
  take turns; each run tagged with a student-chosen name.
- **Export:** per-run report (CSV/JSON) with telemetry, score breakdown (Appendix D), quiz answers
  and the player's sketch map (PNG) — the teacher's assessment artifacts (O6).
- **Teacher controls:** pause, freeze wind, reveal instructor overlay, set seed, force a specific
  weather script — for demonstrating a concept mid-lesson.
- **Lesson-length fit:** scenarios must fit a 45–60 min lesson including briefing and debrief;
  verified in playtesting (G6) against real lesson periods.
- **Offline & locked-down environments:** everything runs from local files; no admin rights beyond
  installing; no firewall prompts in default localhost mode.

### 7.6 Difficulty matrix (v1.2, new)

Difficulty changes **environmental variability and assistance, never physics constants** (§10
risk). Concrete defaults:

| Parameter | Apprentice | Helmsman (*styrimaðr*) | Master |
|---|---|---|---|
| Wind direction variability σ | ±5° | ±12° | ±20° |
| Gust magnitude | 0.8× | 1.0× | 1.3× |
| Tide stream strength | 0.7× | 1.0× | 1.2× |
| Seamark identification range | +30% (forgiving) | as tuned (§3.5) | −20% |
| Visibility/haze | clear | per research | per research + fog events |
| Oar rate limit | 45°/s | 30°/s | 22°/s |
| Hints | on demand, explicit | on demand, cryptic | none |
| Night sailing | off | optional | optional |
| Instructor overlay | allowed | allowed | off |

---

## 8. Team and Roles (assumptions)

Durations in §9 assume roughly **1.5–2 FTE**:

| Role | Allocation | Responsibility |
|---|---|---|
| Tech lead / UE programmer | 1.0 FTE | Physics, wind/tide, bridge, scale model, build infra |
| Designer / researcher | 0.5 FTE | Research docs, scenario design, quizzes, playtests |
| 3D artist | contract, Phases 2b/6 | Seamarks, ship, terrain dressing |
| Maritime historian advisor | external, G1/G3/G4 | Historical sign-off |
| Experienced sailor reviewer | external, G3 | Sail-polar and "feel" validation |
| Sound designer | contract, Phase 8 | Wind/sail/hull audio |
| Teacher liaison / playtest lead | part-time, Phase 7 | Classroom playtesting |

Solo-developer variant: roughly double all durations and cut to S0–S3.

---

## 9. Schedule and Milestones

### 9.1 Plan

| Phase | Work | Duration | Milestone / gate |
|---|---|---|---|
| 0 | Project setup, repo/LFS, UE version pin, licensing decision (§7.3), plan review | 1 wk | **G0** |
| 1 | Historical research (S0–S3 full depth; S5/S6 summary) + **terrain-pipeline tooling spike** | 3–4 wk | **G1** |
| 2a | Scenario design docs incl. S0, harbour/waiting loop, navigation loop | 2 wk (parallel with Phase 1 tail) | **G2a** |
| 3 | Ship physics sandbox + **scale model prototype (D1, k and warp)** + sail polar validation (§4.4) | 4 wk | **G3** |
| 4 | Wind, current/tide subsystems, sea states, time-warp | 2 wk (parallel with Phase 3 tail) | **G4** |
| 5 | Scratch editor spike (D2) → extension + bridge + examples + first-run check | 2 wk (parallel with 2b) | **G5** |
| 2b | **Vertical slice:** S0 + S3 blockout → art | 6 wk | **G2b: vertical slice playable** |
| 6 | Remaining scenarios + briefings/debriefs/quizzes/sketch map | 6 wk | Feature-complete |
| 7 | Playtesting (students/teachers), tuning | 3 wk | **G6** |
| 8 | Polish, audio, packaging, docs, classroom guide | 2 wk | **Release 1.0** |

Total ≈ 6 months. The **vertical slice** (S0 tutorial + S3 open-sea leg + Scratch oar) lands at
~3 months and is the first public deliverable.

### 9.2 Gates: owners, evidence and timeboxes

| Gate | Owner / sign-off | Required evidence | Slip limit |
|---|---|---|---|
| G0 | Project owner | Plan approved; decision-register defaults confirmed or amended; repo + LFS working; licensing route chosen (§7.3); UE version pinned; min-spec agreed | — |
| G1 | Maritime historian | All research docs cited; 4 scenarios selected; leg tables with distances/bearings/seamarks; wind + tide tables | 1 wk |
| G2a | Designer + reviewer | Every scenario has a design doc and a playable grey-box blockout; §3.8 checklist started | 1 wk |
| G2b | Project owner + teacher liaison | **Vertical slice** (S0 + S3) playable end-to-end with the Scratch oar; iGPU performance path verified (O7); first classroom-fit check against a real lesson period | 1 wk |
| G3 | Sailor + historian | Automated polar tests pass; θ_luff and θ_vmg recorded and compared to reference; **k and warp fixed**; both §3.5 deviations documented and mitigated; warp visual review signed | 1 wk |
| G4 | Historian + designer | Per-scenario wind/tide tables match research; instructor debug view demoed | 1 wk |
| G5 | Non-developer tester | D2 editor path works on a clean machine; latency + heartbeat test reports; example `.sb3` programs run unaided | 1 wk |
| G6 | Playtest lead + teacher | Playtest report with pre/post quiz data (O6) and KPIs (§11); top issues triaged | — |

Gate reviews are **booked two weeks in advance** (§10 risk on reviewer availability) and are
timeboxed: a gate that slips more than its limit escalates to a scope decision, not a silent delay.

### 9.3 Critical path and dependencies

```
G0 ─► Phase 1 research ─────────────┬─► Phase 2a design ─► Phase 2b vertical slice ─► Phase 6 ─► Phase 7 ─► 1.0
      (wind.md, tides.md, ships.md) │        ▲                     ▲   ▲
                                    │        │                     │   └── Scratch bridge (Phase 5)
      tools/ terrain spike ─────────┘        │                     └────── Wind/tide (Phase 4)
                                             └── Scale model k (Phase 3) ◄── Ship physics sandbox (Phase 3)
```

- **Longest chain:** research → scale model (k) → terrain at k → scenario art → playtest. The
  scale factor **k must be fixed at G3** before any terrain is built at final resolution; blockouts
  may proceed with provisional k because only geography rescales, not physics.
- **Parallel-safe:** Scratch bridge (Phase 5) depends only on the oar component interface, so it
  can proceed against a stub and is not on the critical path.
- **Highest-risk single item:** the terrain pipeline (`tools/`), hence the Phase 1 spike.

---

## 10. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| **Scale model (D1) feels wrong** — toy-like world, or legs too long even with warp | Whole game feel | Prototype k ∈ {8,16,32} in the Phase 3 sandbox using the §3.5 worked example; fix per-scenario k at G2a/G3; both deviations documented and mitigated (fraction-of-leg identification ranges, vertical-exaggeration knob D8) |
| **Seamarks culled at range by UE HLOD/draw distance** | Core navigation mechanic silently broken | Landmark actors exempt from distance culling; forced HLOD; automated per-scenario visibility test in CI (§11) |
| **Time-warp looks wrong** (waves too fast for their length) | Breaks immersion at 8× | Cap at 8×; switch to long-period swell representation while warping; explicit G3 visual review; auto-revert to 1× near anything interesting |
| **Official Scratch editor can't load custom extensions** | Phase 5 blocked | Week-1 TurboWarp spike (D2); fallbacks: self-hosted `scratch-gui` fork, companion app; keyboard fallback always works |
| **Scratch reporters can't await network data** | Student programs get stale/empty values | Extension polls bridge in background; reporters return cached values + `age (ms)`; specified in Appendix B, tested in G5 |
| Historical wind data for c. 800–1100 is uncertain (MCA) | Accuracy criticism | Pilot charts + ERA5 as base; assumption documented in `wind.md`; historian review; framed in-game as "plausible", not "exact" |
| **Research scope at 0.5 FTE** | Phase 1 overruns | Full depth only for S0–S3 in Phase 1; S5/S6 researched just before their build (§2) |
| Sail physics feels wrong or too hard | Frustration, no learning | Sandbox tuning; difficulty changes variability, never constants (§7.6); compare against reconstruction logs; θ_vmg taught explicitly (§4.4) |
| Scope explosion (7 scenarios × terrain) | Schedule slip | Vertical slice first; data-driven scenarios; **pre-agreed cut order: S4, then S6** (S0–S3 + S5 cover all lesson types) |
| UE Water plugin limits in large open ocean | Visual/technical issues | Custom Gerstner solution decoupled from the plugin; tested early on S3 |
| Terrain pipeline quality/licence gaps | Content rework, legal risk | Phase 1 tooling spike; licence check at pipeline start; `docs/ATTRIBUTION.md` from day one |
| **Apache-2.0 vs. marketplace asset EULAs** | Cannot legally publish the repo | G0 decision (§7.3): commit only CC0/CC-BY/engine content; fetch-script for anything non-redistributable |
| Scratch latency spikes | Control feel | UDP push (no TCP retransmit), smoothing, 100 ms budget enforced and soak-tested |
| Wind/sail/wave/pennant visuals drift apart | Player misreads wind | Single `WindSubsystem` source of truth; per-scenario visual QA checklist |
| Historian/sailor reviewer availability | Gate delays | Recruit at G0; async review; reviews booked 2 weeks ahead; gates timeboxed (§9.2) |
| Classroom hardware below min-spec | Adoption failure | Early iGPU performance test (Phase 2b); scalability settings; published min-spec (O7) |
| Artist contract dependency for seamark models | Phase 2b/6 slip | Grey-box seamarks are playable (silhouette is what matters); art pass is separable and last |
| Motion sickness from ship roll | Players quit | Mandatory camera/comfort options (§7.2); tested in playtesting |

---

## 11. Testing and Validation

- **Physics unit tests:** automated polar sweep — true-wind angle 0–360° in 1° steps at three wind
  speeds; assert drive collapses inside θ_luff; extract θ_luff and θ_vmg; leeway-vs-wind-angle
  table matches the reference from `ships.md` within tolerance; steering-oar asymmetry sign check
  (port and starboard turns differ, as on the real ship).
- **Determinism test:** fixed seed → identical telemetry hash across runs (replay integrity; also
  enables "same weather, different helmsmen" classroom comparisons).
- **Golden-run regression (v1.2):** a recorded oar-input trace per scenario produces a telemetry
  hash within tolerance across engine/physics versions — catches silent physics regressions.
- **Headless scenario smoke test (v1.2):** each scenario runs unattended (scripted oar input) for
  its full length in CI; asserts no crash, ship stays in bounds, all seamarks become identifiable
  at least once, and the leg completes.
- **Seamark visibility test (v1.2):** automated check that every seamark is renderable and
  identifiable at its target range from the deck and from the mast (§3.5 table) — guards against
  culling/HLOD regressions.
- **Scratch bridge tests:** 1-hour latency soak at 10 Hz (no packets beyond budget); heartbeat
  timeout behaviour (oar amidships + warning); protocol-version mismatch rejection; stale-data
  `age (ms)` reporter correctness.
- **Performance test:** 60 fps @ 1080p on GTX 1060-class; boots and is playable at low settings on
  an Intel-iGPU laptop. Run in Phase 2b and repeated before release (O7).
- **Playtesting protocol:** pre/post navigation quiz; observation checklist (did the player use the
  lookout? notice the pennant? understand leeway? sail at θ_vmg instead of pinching? wait for a
  fair wind? catch the tide?); think-aloud sessions; teacher review of classroom fit against real
  lesson periods.
- **Learning KPIs from telemetry (v1.2):** % of legs completed without hints; time to first
  successful transit; number of seamark sightings used per leg; mean course error vs. the intended
  transit; leeway-compensation behaviour (does the player aim upwind?); wait-vs-sail decisions and
  their outcomes. These feed the G6 report and O6.
- **Historical review:** G1, G3, G4 with domain reviewers; final sign-off before 1.0.

---

## 12. Design Decision Register

Defaults are **proposals** — confirm or amend at the noted gates.

| # | Decision | Proposed default | Confirm at |
|---|---|---|---|
| D1 | World scale & time model | Ship 1:1; geography uniform 1:k with **per-scenario k ∈ [8, 32]** (12–25 min at 1× where possible); simulation clock real-time; voyage clock via player time-warp; identification ranges as a fraction of leg length (§3.5) | G3 |
| D2 | Scratch editor path | TurboWarp desktop + custom extension by URL; spike in Phase 5 week 1 | G5 |
| D3 | Scratch telemetry realism | Only "Viking-sensible" reporters with realistic error; exact values behind the instructor flag | G5 |
| D4 | Night sailing | Day sailing by default; night as a difficulty option where voyages historically lay to | G2a |
| D5 | Rowing model | Crew-energy abstraction (no per-oar physics); drains on rowing/baling/kedging | G3 |
| D6 | Launch languages | EN + ES (project origin); DA strings prepared | G0 |
| D7 | Time-warp | 1×/2×/4×/8×, player-controlled; auto-revert to 1× on oar input or hazard proximity (§3.5) | G3 |
| D8 | Terrain vertical exaggeration | Uniform (none) by default; optional up to 1.5× only if seamarks read poorly at sea level | G3 |
| D9 | Sun-compass aid | Off in S0–S2; optional in S3/S4 with an explicit note that its function is debated | G2a |
| D10 | Two-crew LAN mode | Stretch goal; `--lan` opt-in; localhost-only by default | Post-1.0 |
| D11 | Asset licensing route | Commit only CC0/CC-BY/engine content (option b, §7.3); fetch-script for the rest | G0 |

---

## 13. Open Questions for the Reviewer

1. **Scenario cut:** confirm S0–S3 + S5, with S4 stretch and S6 optional?
2. **Audience:** general public, school classes (which age?), or university? Drives language,
   reading age, quiz depth and difficulty defaults.
3. **Scale model (§3.5):** approve per-scenario k ∈ [8, 32] with a 1:1 ship and time-warp up to 8×?
   Or prefer a single global k (more consistent feel, longer sessions), or shorter real legs
   chosen so no warp is ever needed?
4. **Session length (O2):** is 12–25 min per leg right, or must it fit a fixed lesson period
   (e.g. exactly 45 min including briefing/debrief)?
5. **Waiting for a fair wind (§3.6):** approve supplies + harbour waiting as a scored mechanic?
   Any concern it slows the game down for younger players?
6. **Sketch map (§3.7):** should the player-drawn sketch map be a graded artifact (teacher
   assessment) or purely a personal aid?
7. **Scratch:** is the program written *by the players* (teaching coding) or supplied by us as the
   canonical oar controller? The architecture supports both; the classroom guide differs.
8. **Scratch editor (D2):** any institutional constraints on TurboWarp or a self-hosted editor in
   target classrooms?
9. **Hardware:** what can we assume — dedicated GPU or iGPU-only (O7)?
10. **Licensing (D11):** keep the repo Apache-2.0 with CC0/CC-BY-only assets, or relicense?
11. **Distribution:** itch.io, direct installer, or a school IT image?
12. **Two-crew mode (D10):** worth pulling into 1.0 if the schedule allows?

---

## 14. Deliverables Summary

1. `docs/research/` — routes, wind, tides, ships, navigation (all cited).
2. `docs/design/` — physics spec (incl. §3.5 scale deviations and §4.4 polar), scenario design
   docs S0–S6, decision-register updates.
3. `docs/integration/scratch-bridge.md` — protocol, schemas, setup, troubleshooting.
4. `docs/ATTRIBUTION.md` — third-party data and asset attributions.
5. UE project (`ue/`) — 4–6 scenarios + tutorial; ship with sail + steering-oar simulation; wind,
   tide and time-warp systems; harbour/waiting loop; navigation loop (lookout, bearings, lead
   line, sketch map); briefing/debrief/quiz/scoring; telemetry and deterministic replay.
6. `scratch/` — custom extension, local bridge service, four example `.sb3` programs.
7. `tools/` — heightmap resample-to-scale and wind/tide data processing.
8. `README.md`, build/run instructions, classroom guide (§7.5), review reports per gate.

---

## 15. Reference List (starter set for Phase 1)

- Roesdahl, E. — *The Vikings* (Penguin, revised ed.)
- Graham-Campbell, J. — *The Viking World* (3rd ed., 2013)
- Englert, A. & Trakadas, A. (eds.) — *Wulfstan's Voyage: The Baltic Sea region in the early
  Viking age* (Viking Ship Museum Roskilde, 2009)
- Crumlin-Pedersen, O. — *Viking-Age Ships and Shipbuilding in Hedeby/Haithabu and Schleswig*
  (2002, 2012)
- Viking Ship Museum Roskilde — reconstruction sea-trial publications and voyage reports for
  *Ottar* (Skuldelev 1 knarr) and *Sea Stallion from Glendalough* (Skuldelev 2 longship,
  Roskilde–Dublin 2007–08)
- Magnusson, M. & Pálsson, H. (trans.) — *The Vinland Sagas* (Penguin)
- *Óláfs saga helga* sailing directions Norway–Greenland (in *Heimskringla*)
- Adam of Bremen — *History of the Archbishops of Hamburg-Bremen* (c. 1070)
- Ingstad, H. & Ingstad, A. S. — *The Viking Discovery of America* (2000)
- US NGA / UK Admiralty Pilot Charts, North Atlantic & Baltic; Copernicus ERA5 reanalysis
- Published tidal-stream atlases / tide tables: North Sea, Norwegian coast, Skagerrak–Kattegat,
  Baltic
- Lamb, H. H. — *Climate, History and the Modern World* (Medieval Climate Anomaly context)
- Seaver, K. — *The Frozen Echo* (Greenland navigation and abandonment)
- Scholarship on the Uunartoq sun-compass fragment (both pro and sceptical positions — the
  debate is cited, not resolved, in `navigation.md`)

---

## Appendix A — Glossary of Norse/Nautical Terms Used

| Term | Meaning |
|---|---|
| *styrimaðr* | Helmsman / ship's master |
| *stjórn* | The steering oar; also "steering" |
| *stjórnborði* | Starboard — "steering-board side" (the oar side) |
| *bakborði* | Port — the side the helmsman had his back to |
| *vaðmál* | Homespun wool cloth used for sails |
| *knarr* | Broader, deeper cargo vessel (ocean trader) |
| *karvi* | Small general-purpose ship |
| *snekkja* / *dreki* | Longship types (warships) |
| *byr* | A fair/favourable wind; *bíða byrjar* = to wait for a fair wind |
| *útkik* | Lookout (the bow watch); also the place from which one looks out |
| *fingrar* | "Fingers" — a coarse hand-based angular measure used for bearings/altitudes |
| *hafvilla* | Losing one's bearings at sea; being fog-bound or becalmed |
| *leið* | Route, course |
| *landnám* | "Land-taking" — settlement (e.g. of Iceland) |
| *Austrvegr* | "The eastern way" — the Baltic/Russian river route |
| *hörgr* | Cairn / stone marker (also used as a seamark) |
| transit / leading marks | Two marks kept in line to hold a safe course |
| wearing ship | Turning stern-through-wind (downwind turn) instead of tacking |
| kedging | Hauling the ship off a shoal with an anchor carried out by boat |
| VMG | Velocity made good — progress along a desired direction (here, to windward) |
| Froude similarity | Model-scale similarity for gravity-wave systems; lengths scale k, periods √k |

---

## Appendix B — Scratch Bridge Protocol (v0 draft)

All messages are JSON, UTF-8, `v` = protocol version (integer, starts at 1).

**B.0 Port map (all bound to 127.0.0.1 unless `--lan`, D10)**

| Port | Proto | Listener | Purpose |
|---|---|---|---|
| 9871 | HTTP | bridge | Scratch-facing API: `POST /cmd`, `GET /state`, `GET /health`; CORS enabled |
| 9870 | UDP | UE | bridge → UE: handshake and rudder/sail commands |
| 9872 | UDP | bridge | UE → bridge: telemetry and handshake ack |

All three ports are configurable via bridge flags (`--http-port`, `--ue-port`, `--telemetry-port`)
and displayed in the game's first-run check (§6.2), so a port conflict on a classroom machine can
be resolved without reading source.

**B.1 Handshake (bridge ⇄ UE, on bridge start and on UE start)**

```json
// bridge -> UE  (UDP :9870)
{"v":1,"type":"hello","role":"bridge","capabilities":["rudder","sail","telemetry"],"ts":1730000000123}
// UE -> bridge   (UDP :9872)
{"v":1,"type":"hello_ack","role":"ue","capabilities":["rudder","telemetry"],"scenario":"S3","ts":1730000000130}
```
On version or capability mismatch the bridge reports `bridge_error` to Scratch and the game shows
a non-blocking warning; the oar falls back to keyboard if `--solo`.

**B.2 Command: Scratch → bridge → UE**

```http
POST /cmd  HTTP/1.1   Content-Type: application/json
{"v":1,"type":"rudder","angle":-12.5,"seq":4821,"ts":1730000000123}
```
- `angle` clamped to [−45, +45]; negative = port. Out-of-range → clamped + `warn` in response.
- Optional: `{"v":1,"type":"sail","height":80,"brace":10,"seq":...}` (stretch, D-gated).
- `seq` monotonically increasing; UE ignores out-of-order/stale commands.
- Expected send rate 10 Hz (Scratch `forever` + `wait 0.1`).
- Response: `200 {"ok":true,"applied":true,"seq":4821,"age_ms":7}`.

**B.3 Telemetry: UE → bridge → Scratch**

```json
// UE -> bridge (UDP :9872), 10 Hz
{"v":1,"type":"state","ts":1730000000130,"scenario":"S3",
 "heading":271.4,"pennant_angle":-38.0,"speed_kn":5.8,"depth_m":41.2,
 "warp":4,"heartbeat":true,
 "marks":[{"id":"breidafjall","bearing":288.0,"range_km":7.1,"identifiable":true}]}
```
- `marks` contains **only** seamarks inside their identification range (§3.5) — the D3 realism
  constraint is enforced server-side in UE, not in Scratch.
- Bearing error ±5° and speed error ±10% are applied before transmission at non-instructor
  difficulty (§7.6).
- Bridge caches the latest state; Scratch `GET /state` returns it plus `age_ms` since receipt.
  Reporters are **cached and non-blocking** (§6.2).

**B.4 Heartbeat and failure modes**

| Condition | Behaviour |
|---|---|
| No telemetry for 500 ms | Bridge marks `stale`; Scratch `bridge connected?` → false |
| No command for 500 ms | UE eases oar to amidships, shows warning once |
| Malformed JSON / wrong `v` | Drop message, increment error counter, expose via `GET /health` |
| Bridge not running | Game first-run check shows setup instructions; `--solo` keyboard fallback |
| Two Scratch clients | Second client rejected with HTTP 409 and a clear message |

`GET /health` returns `{"ok":true,"ue":true,"clients":1,"errors":0,"uptime_s":1234}` for the
first-run check and for automated tests (§11).

---

## Appendix C — `ScenarioDefinition` Data Asset Schema

| Field | Type | Notes |
|---|---|---|
| `ScenarioId` | string | `S0`…`S6` |
| `TitleL10n`, `BriefingL10n`, `DebriefL10n` | text keys | Localization tables only (§7.2); narration audio keys |
| `RouteLeg` | struct | `FromHarbour`, `ToHarbour`, `RealDistanceKm`, `GameDistanceKm`, `WorldScaleK` |
| `ShipPreset` | enum | karvi / knarr / longship → hull + rig + sail-area params from `ships.md` |
| `Seamarks[]` | array | `Id`, `NameL10n`, `RealHeightM`, `ScaledHeightM`, `Class` (peak/island/headland/cairn), `RealHorizonKm`, `IdentRangeKm` (computed by `tools/` from the §3.5 fraction-of-leg rule), `Position`, `IsTransitPairWith` |
| `Hazards[]` | array | reefs, shoals (depth), tide races, ice fields, lee shores |
| `WindScript` | curve/table | prevailing dir+speed, σ variability, gust profile, keyed events (backing wind, squall, fog) |
| `TideModel` | struct | M2/S2 amplitude+phase per waypoint, datum, harbour tide gate |
| `Currents[]` | array | named current fields with direction/speed |
| `Harbour` | struct | mooring points, repair rate, supply capacity, default warp while waiting |
| `Supplies` | struct | start amount, drain rate per hour (voyage clock), failure threshold |
| `FailureStates[]` | array | grounding, dismasting, capsize, supplies exhausted → recovery or debrief + retry |
| `Quiz[]` | array | 4–6 items, each tagged to a learning objective (Appendix E) |
| `ScoringWeights` | struct | per Appendix D |
| `Seed` | int | deterministic weather/tide (§11) |
| `DifficultyOverrides` | map | per §7.6 |
| `NightRule` | enum | day-only / optional / required (D4) |

---

## Appendix D — Scoring Rubric

Score is **navigation quality only** — never violence (§1.4). Each scenario scores 0–100:

| Dimension | Weight | What is measured |
|---|---|---|
| Course accuracy | 25 | Mean cross-track error vs. the intended transit/rhumb; leeway compensated (aimed upwind?) |
| Seamark use | 20 | Sightings taken, transits identified and held, lookout used at the right moments |
| Wind judgement | 20 | Sail trim appropriate to the point of sail; sailed near θ_vmg rather than pinching at θ_luff; reefed in time |
| Voyage planning | 15 | Wait-vs-sail decision quality (§3.6); tide used where it matters; supplies intact |
| Helmsmanship | 10 | Smooth oar work (no hunting/over-correcting); recovered from stalls and broaches |
| Arrival condition | 10 | Hull damage, crew energy, elapsed time vs. par |

Modifiers: hints used (−2 each at Helmsman difficulty), retries (recorded, not penalized — failure
is a teaching moment), failures with a good debrief read (no penalty). Full breakdown exported in
the run report (§7.5).

---

## Appendix E — Learning-Objective Alignment Matrix

Every objective has a mechanic that teaches it and an assessment that measures it — no objective
may exist without both.

| Objective | Taught by (mechanic) | Measured by |
|---|---|---|
| L1 Read wind direction without instruments | Pennant, sail luff, whitecaps, rigging audio (§5.1) | Quiz item; KPI: time to correct course after a wind shift |
| L2 Understand a square sail's limits | θ_luff / θ_vmg polar, luffing feedback (§4.4) | Quiz item; KPI: mean angle sailed off the wind vs. θ_vmg |
| L3 Compensate for leeway | Leeway model + transit drift (§4.2) | KPI: cross-track error; quiz item |
| L4 Use transits/leading marks | Transit discovery and holding (§3.7) | KPI: transits identified/held; scenario score |
| L5 Fix position by seamarks and bearings | Lookout, hand bearings, identification ranges (§3.5, §3.7) | Sketch-map artifact; quiz item |
| L6 Judge when to wait for a fair wind | Harbour loop, supplies, weather reading (§3.6) | KPI: wait-vs-sail decision outcomes; score dimension |
| L7 Use tide and current | Tide gates, stream drift, ground track (§5.3) | KPI: tide-gate timing; quiz item |
| L8 Steer with a quarter-mounted oar | Asymmetric oar model, Scratch control (§4.2, §6) | KPI: oar-work smoothness; teacher observation |
| L9 Know the route geography and history | Briefings, debriefs, real-route replay (§3.3) | Pre/post quiz (O6) |
| L10 Program a controller from sensory feedback | Scratch reporters with realistic error (§6.2, D3) | Working student `.sb3`; coding rubric |

---

## Appendix F — Reviewer Checklist

For the reviewer of this plan — please respond on each line (accept / amend / reject):

- [ ] Scope and non-goals (§1.3) — anything missing that stakeholders will expect?
- [ ] Historical framing and sensitivity (§1.4) — acceptable for target schools?
- [ ] Scenario slate and cut order (§3.2, §10) — agree S0–S3 + S5, cut S4 then S6?
- [ ] **Scale model: ship 1:1, per-scenario k ∈ [8,32], warp ≤ 8× (§3.5, D1/D7)** — the single biggest design call
- [ ] Both quantified scale deviations and their mitigations (§3.5) — acceptable?
- [ ] Harbour/supplies/waiting-for-fair-wind as a scored mechanic (§3.6) — agree?
- [ ] No charts; oral description + player sketch map (§3.7) — agree, and is the sketch map graded?
- [ ] Sail polar: θ_luff ≈ 55° default, validated at G3, θ_vmg taught explicitly (§4.4) — agree?
- [ ] Scratch editor path = TurboWarp (D2) — any classroom constraints?
- [ ] Scratch telemetry realism, server-side enforced (§6.2, D3, Appendix B.3) — agree?
- [ ] Two-crew LAN mode deferred to post-1.0 (D10) — agree?
- [ ] Asset licensing route (D11, §7.3) — Apache-2.0 with CC0/CC-BY-only committed assets?
- [ ] Difficulty matrix defaults (§7.6) — sensible for the target age?
- [ ] Schedule, gate owners and timeboxes (§9) — realistic for the assumed 1.5–2 FTE?
- [ ] Open questions §13 items 1–12 — decisions requested

---

**End of plan v1.2 — awaiting review feedback.**
