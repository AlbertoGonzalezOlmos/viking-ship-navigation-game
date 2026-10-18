# Prevailing Winds and Weather — Research Draft

**Status:** Draft v0.1 for G1/G4 review. Directions are the well-established modern prevailing
patterns (pilot charts / ERA5), used as a proxy for the Medieval Climate Anomaly (c. 950–1250).
**Verify the exact seasonal wind roses and the MCA caveat wording before G4.**

**Framing decision (plan §5.1):** in-game wind is "plausible, not exact" for c. 800–1100. We use
modern prevailing winds as the base because (a) they are measured and citable, and (b) the
Medieval Climate Anomaly shifted intensities and some tracks but did not reverse the fundamental
hemispheric pattern (mid-latitude westerlies). The caveat is stated in-game where relevant.

---

## Regional prevailing winds (summary)

| Region | Prevailing direction | Seasonality | Notes for scenarios |
|---|---|---|---|
| North Sea (S1, S3 east part) | SW–W | Strongest autumn/winter; summer (Jun–Aug) moderate and more variable | Outbound to Shetland/Ireland is a reach-to-run with SW winds; a N or NE wind makes it a slog |
| Norwegian Sea (S3 west part) | W–SW | Gales frequent Oct–Mar; summer more settled | Drives the Iceland settlement route: outbound runs before it |
| Skagerrak / Kattegat / Limfjord (S2) | W–SW | Summer moderate; channeled along the fjord axis | Local sea breezes add diurnal variability |
| Baltic (S5) | W–SW, lighter than North Sea | Summer moderate; winter can freeze | Shifty; land/sea breeze dominates in summer |
| Norwegian coast / fjords (S6) | Channeled along valleys; W–SW at sea | Katabatic (drainage) winds at dawn; acceleration through sounds | Highly local — motivates the spatial wind model (§5.2) |

---

## Per-scenario wind defaults (for the UE `WindSubsystem`)

| # | Base wind (direction FROM) | Base speed | Variability σ | Notes |
|---|---|---|---|---|
| S0 | W | 8 kn | ±5° | Gentle, steady; tutorial |
| S1 | SW | 12 kn | ±12° | Fair-to-foul; squalls |
| S2 | W | 10 kn | ±12° | Sea-breeze modulation |
| S3 | W–SW | 14 kn | ±15° | Before-the-wind leg |
| S4 | N–NE | 10 kn | ±15° | Cold, damp, fog |
| S5 | W–SW | 9 kn | ±18° | Shifty, light |
| S6 | W–SW | 11 kn | ±15° | Channel acceleration +20% in sounds |

*Speed units are knots (wind). Variability σ is the plan's difficulty parameter (§7.6),
Helmsman default. These are planning defaults — replace with per-month wind roses from
pilot charts during G4.*

---

## Scripted weather events (per scenario weather script, §5.2)

- **S1:** a **backing wind** (S→SE) before the Shetland approach forces the player off the
  rhumb line — historically a common late-summer pattern that made landfall uncertain.
- **S2:** diurnal **sea breeze** in the afternoon; a squall line moving through the fjord.
- **S3:** long-period North Atlantic swell builds over the leg; a fast-moving **frontal
  squall** with wind veering W→NW tests reefing.
- **S4:** a **fog bank** off the Labrador coast; iceberg/sea-ice field.
- **S5:** scattered showers with gust cells (convective); light-and-variable near the
  archipelago.
- **S6:** **katabatic gust** at dawn off a fjord wall; channel jet accelerating through a
  sound.

---

## Wind reading without instruments (design constraints, §5.1)

The player must read wind through: sail set and luffing, the wool pennant on the yard, wave
amplitude and whitecaps, foam streaks, and rigging/wave audio. No numeric wind readout in normal
play. The `WindSubsystem` is the single source of truth feeding sail forces, pennant, particles,
audio and sea state identically.

---

## Sources to verify (G4)

- US NGA / UK Admiralty Pilot Charts, North Atlantic & Baltic (monthly wind roses).
- Copernicus ERA5 reanalysis, seasonal surface-wind statistics for the scenario boxes.
- Lamb, *Climate, History and the Modern World* — Medieval Climate Anomaly context.
- Local sailing directions for channel-acceleration and katabatic notes (S6, S2).
