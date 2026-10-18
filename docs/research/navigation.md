# Navigation Techniques — Research Draft

**Status:** Draft v0.1 for G1 review. This maps each documented Viking navigation technique to an
in-game mechanic (plan §3.7). Technique descriptions are well attested; **the sun-compass
(Uunartoq) function is debated and must be presented as such in-game (D9).**

**Core design principle:** Vikings had **no charts and no written sailing directions** — route
knowledge was oral, held by the *styrimaðr*. Therefore the game provides no chart, no plotted
route and no GPS-style position readout. The techniques below are the player's only tools.

---

## Techniques and their in-game mechanics

### 1. Landmark piloting / leading marks (transits)
Two marks held in line indicate a safe course or a turning point.
- **In-game:** transits are discovered (two seamarks align) and must be held; the game highlights
  the alignment only after the player has found it (discovery, not hand-holding). Core mechanic
  of S2/S6 and every harbour approach.

### 2. Hand bearings (*fingrar*)
Coarse angular measure — the height/bearing of a mark in "fingers" held at arm's length.
- **In-game:** aiming at a seamark reports its height in fingers above the horizon. Teaches why
  the *rate of change* of a bearing reveals range and drift.

### 3. The lookout (*útkik*)
A crew member in the bows or at the mast raises eye height, extending the horizon.
- **In-game:** stationing the lookout raises h_eye in the horizon formula
  (d ≈ 3.57·(√h_eye + √h_mark) km) and unlocks spoken reports ("land fine on the starboard bow,
  two fingers above the water"). The reports are the primary position information.

### 4. Lead line (sounding)
Depth and bottom character under the keel.
- **In-game:** depth matches the real bathymetry; bottom-type flavour ("grey sand", "shell").
  Essential in shallow-water legs (S2, S6); grounding depth uses tide height.

### 5. Swell, birds and clouds
Ocean swell direction persists independently of local wind; seabirds and cloud banks over land
reveal it before it is visible.
- **In-game:** long-period swell direction is rendered separately from wind chop; bird flocks and
  a "land loom" cloud effect appear over land within detection range. The S3/S4 landfall lessons.

### 6. Latitude sailing (sun and stars)
Sun altitude at noon (or North Star altitude) gives rough latitude on clear days.
- **In-game:** taught in S3; the player checks sun height against a known value for the
  destination latitude. Cloud cover makes it unavailable — forcing dead reckoning.

### 7. The sun-compass (Uunartoq fragment) — debated
The fragment is often interpreted as a bearing-dial/sun-compass, but its function is **not
established**.
- **In-game (D9):** optional aid in S3/S4 only, with an explicit note that scholars debate it.
  Default off for S0–S2.

### 8. Dead reckoning and *hafvilla*
Time × speed = distance along a held heading; *hafvilla* is the state of losing one's bearings
(calm, fog, overcast that hides the sun/stars).
- **In-game:** speed is felt via the log-line analogue; *hafvilla* is an emergent state when
  weather removes all fixes — the scenario debrief explains its historical danger.

---

## The sketch map (the only "chart")

The player may plot what they believe they have seen on a crude vellum sketch — seamarks, rough
bearings, their own track. It is exported with the debrief as a teacher-assessable artifact
(plan O6, §3.7) and compared against the true track.

---

## Visibility model (for all of the above)

- Horizon: d(km) ≈ 3.57·(√h_eye + √h_mark), +~8% standard refraction.
- Identification range uses the plan's fraction-of-leg rule (§3.5), capped by weather
  visibility: `IdentRange = (real horizon ÷ real leg) × in-game leg`. Computed per scenario by
  `tools/route_geometry.py`.

---

## Sources to verify (G1)

- *Óláfs saga helga* sailing directions (in *Heimskringla*) — the primary oral-navigation text.
- Ottar's and Wulfstan's accounts (Orosius / King Alfred, c. 890) — coastal route description.
- Scholarship on the Uunartoq sun-compass fragment (both pro and sceptical positions).
- Roesdahl, *The Vikings* — navigation chapter; Graham-Campbell, *The Viking World*.
- Seaver, *The Frozen Echo* — Greenland navigation and the limits of the techniques.
