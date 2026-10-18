# Tides and Currents — Research Draft

**Status:** Draft v0.1 for G1/G4 review. Ranges and stream strengths are planning values;
**verify against tidal-stream atlases and tide tables before G4.**

**Framing (plan §5.3):** tides matter historically because Viking crews timed harbour
departures and channel transits to the fair tide. They are simulated with a small harmonic model
(M2 + S2 constituents) per scenario — sufficient for the game's fidelity. The Baltic is
effectively non-tidal, which is itself a teaching point (contrast S5 with S2/S6).

---

## Tidal regimes by scenario

| # | Region | Type | Spring range (planning) | Streams / notes |
|---|---|---|---|---|
| S0 | Sheltered fjord | Negligible | < 0.1 m | No tide in tutorial |
| S1 | North Sea / Shetland | Semidiurnal (M2) | 1.5–2.0 m | Tide races around headlands; relevant on departure and landfall |
| S2 | Limfjord | Semidiurnal, distorted | ~0.3 m range but **strong streams** through narrows | The tide *gate* — ebb/flood direction and strength control passage |
| S3 | North Sea / Norwegian Sea | Semidiurnal (M2) | ~1.0 m (Bergen is near an amphidromic point) | Weak at sea; matter on departure/landfall only |
| S4 | NW Atlantic / Labrador | Semidiurnal | ~1.0–1.5 m | Plus the **Labrador Current** (south-flowing) and icebergs |
| S5 | Baltic | **Non-tidal** | < 0.05 m | Wind-driven level changes (seiches) only |
| S6 | Norwegian coast | Semidiurnal (M2) | 1.0–2.0 m | Strong streams in sounds (Moskstraumen-type) |

---

## Major currents (per scenario, §5.3)

| Current | Scenario | Direction | Planning speed | Notes |
|---|---|---|---|---|
| Norwegian Coastal Current | S6 (and S3 departure) | N along the coast | 0.5–1.5 kn | Offshore drift to track in instructor mode |
| North Atlantic Drift | S3 (subtle) | NE | 0.3–0.5 kn | Minor but included for consistency |
| Labrador Current | S4 | S | 0.5–1.5 kn | Carries ice; landfall drift hazard |
| (Baltic) | S5 | none | — | Non-tidal; wind-driven only |

---

## Game design consequences

- **Tide gate (S2, S6):** passage timing is a planning decision in the briefing — "catch the
  fair tide" or wait. Grounding depth uses tide height, so a rising tide can refloat a grounded
  ship (recovery mechanic, §3.3).
- **Ground track vs. water track:** currents shift the over-ground track; shown only in
  instructor mode (plan §5.3).
- **Determinism:** tide phase is driven by the scenario seed and voyage clock, so "same weather,
  different helmsmen" classroom comparisons are reproducible.

---

## Sources to verify (G4)

- UK Admiralty / NGA tidal-stream atlases: North Sea, Norwegian coast, Skagerrak–Kattegat.
- Local tide tables for Lerwick, Bergen, Aalborg/Thyborøn, and the Baltic reference stations.
- Sailing directions for stream strengths in Limfjord narrows and Norwegian sounds.
- For S4: Canadian Hydrographic Service / NGA for the Labrador coast and Labrador Current.
