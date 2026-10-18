# Viking Ship Navigation Game

A learning game about how the Vikings sailed between known landmarks — built in Unreal Engine 5,
with the ship's side-mounted steering oar (*stjórn*) controlled from a Scratch program.

- Sail real Viking-age sea routes (North Sea, North Atlantic, Baltic, Norwegian coast)
- Navigate by landmarks, transits, swell and the wool pennant on the yard — no GPS
- Historically informed wind, tides and square-sail physics
- Write your own Scratch program to work the steering oar

## Status

**Phase 0/1 in progress.** The plan is under review ([docs/PROJECT_PLAN.md](docs/PROJECT_PLAN.md),
v1.2 — reviewers start with Appendix F). Repository scaffolding is set up and the historical
research drafts are underway:

- `docs/research/` — routes, wind, tides, ships, navigation drafts (see
  [docs/research/README.md](docs/research/README.md) for status and G1 verification items)
- `tools/route_geometry.py` — computes leg distances, bearings, horizon distances and the
  world-scale/session-length model (run `python3 tools/route_geometry.py`)

Next: design docs (`docs/design/`, `docs/scenarios/`) after the G1 research review, then the UE
physics sandbox (Phase 3).

## Repository layout

```
├── docs/      # documentation (project plan; research, design, scenario and integration docs)
│   ├── research/    # Phase 1: routes, wind, tides, ships, navigation
│   ├── design/      # physics spec and design docs (Phase 2a)
│   ├── scenarios/   # per-scenario design docs (Phase 2a)
│   └── integration/ # Scratch bridge protocol (Phase 5)
├── ue/        # Unreal Engine project (to be created)
├── scratch/   # Scratch extension, local bridge service, example .sb3 programs (to come)
├── tools/     # route_geometry.py; heightmap import, wind/tide processing (to come)
└── README.md
```

## License

See [LICENSE](LICENSE). Third-party data attribution will be tracked in `docs/ATTRIBUTION.md`
(GEBCO bathymetry CC BY 4.0, Copernicus DEM, SRTM, ERA5).
