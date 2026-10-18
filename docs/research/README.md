# Research Index

Phase 1 deliverable set (plan §2.3). All documents are **drafts for G1 review** — verify against
the cited sources before scenario construction (G2a).

| Document | Covers | Status |
|---|---|---|
| [routes.md](routes.md) | Route geography, computed leg distances/bearings, seamarks, hazards, seasons | Draft v0.1 — distances computed; seamarks/harbours to verify |
| [wind.md](wind.md) | Prevailing winds per region, per-scenario defaults, scripted weather events | Draft v0.1 — verify monthly wind roses (G4) |
| [tides.md](tides.md) | Tidal regimes, stream strengths, major currents, tide-gate design | Draft v0.1 — verify stream data (G4) |
| [ships.md](ships.md) | Ship types, steering oar, speed, sail polar (θ_luff / θ_vmg), physics inputs | Draft v0.1 — verify sail areas and polar coefficients (G3) |
| [navigation.md](navigation.md) | Landmark piloting, lookout, bearings, lead line, latitude sailing, sun-compass | Draft v0.1 — sun-compass presented as debated (D9) |

## Computed data

All distances, bearings, horizon and identification-range numbers come from
`tools/route_geometry.py` (run `python3 tools/route_geometry.py`). Regenerate any number by
editing the waypoints there, not by hand. Per-scenario seamark identification ranges:
`python3 tools/route_geometry.py --ident S3` (or any scenario id).

## Open verification items for G1

1. Seamark names and heights per scenario (currently illustrative in `routes.md`).
2. Exact harbour coordinates and the real Limfjord channel axis (straight-line planning distance
   is 110.8 km; the sailed track is longer and winding).
3. Sail areas and displacement for Skuldelev 1/2/3 (marked "verify" in `ships.md`).
4. θ_luff and θ_vmg reference values from the Roskilde sea-trial publications.
5. Tidal-stream strengths in the Limfjord narrows and Norwegian sounds.
6. Monthly wind roses for the scenario boxes (pilot charts + ERA5).

## Next: design docs

`docs/design/` (physics spec, §3.5 scale deviations, §4.4 polar) and
`docs/scenarios/S0..S6.md` are produced in Phase 2a, after G1.
