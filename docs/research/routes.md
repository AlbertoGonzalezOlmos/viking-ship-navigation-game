# Viking Sea Routes — Research Draft

**Status:** Draft v0.1 for G1 review. Distances and bearings are computed
(`tools/route_geometry.py`); seamark names/heights, harbour details and historical notes
require verification against the cited sources before scenario construction (G2a).

**Data provenance:** great-circle distances on WGS84 (mean Earth radius 6371 km), adequate for
waypoint planning. Final UE levels use per-scenario projected coordinates, not these
great-circle numbers. Prevailing-wind and tide statements are summarized in
[wind.md](wind.md) and [tides.md](tides.md) with sources.

**Scope (per plan §2):** full depth for S0–S3 now; S5/S6 are summaries; S4 is documented but
first on the cut list.

---

## Route summary (computed)

| # | Route | Ship | Total real distance | Cruise @ 6 kn |
|---|-------|------|---------------------|---------------|
| S0 | Tutorial: home waters (fictional fjord circuit) | karvi | 25.7 km | ~2.3 h |
| S1 | Rogaland (Stavanger) → Shetland (Lerwick) | longship | 409.2 km | ~37 h |
| S2 | Limfjord transit (Thyborøn → Aalborg) | knarr | 110.8 km | ~10 h |
| S3 | Bergen → Shetland (Iceland route, leg 1) | knarr | 357.6 km | ~32 h |
| S4 | Vinland saga route (3 legs) | knarr | 2,138.1 km | ~192 h |
| S5 | Birka → Visby (Gotland), Baltic | longship (trade) | 193.3 km | ~17 h |
| S6 | The North Way (Molde → Kristiansund) | karvi | 50.5 km | ~4.5 h |

*S4 total is the sum of three saga legs (Eiriksfjord→Helluland 1,001 km; Helluland→Markland
530 km; Markland→L'Anse aux Meadows 607 km). At k=32 and 8× warp the shortest single leg still
exceeds the 25-minute session target — the arithmetic reason S4 is first on the cut list (§3.2,
§10 of the plan).*

---

## S0 — Tutorial: home waters (fictional)

- **Type:** sheltered fjord circuit, modeled loosely on Roskilde Fjord (realm of the
  Skuldelev ships) but fictionalized so no real seamarks are required.
- **Purpose:** teach steering-oar asymmetry, reading the pennant, the first transit, and the
  lookout before any open water.
- **Circuit (computed):** Start → N-mid 5.1 km @ 331°; N-mid → E-mid 5.5 km @ 233°; E-mid →
  Finish 15.1 km @ 144°.
- **Wind/tide:** gentle steady breeze; no tide (fjord, per [tides.md](tides.md)).
- **Session:** 17 min @ 1× at k=8.

---

## S1 — Rogaland → Shetland (first leg of the Ireland route)

- **Historical context:** the classic summer "raiding corridor" from western Norway to the
  British Isles, converging on Dublin (longphort founded c. 841). Also a trade and settlement
  route — framing follows plan §1.4 (no glorification).
- **Leg:** Stavanger (58.97°N, 5.73°E) → Lerwick (60.15°N, 1.15°W): **409.2 km, initial
  bearing 291.7°** (roughly WNW).
- **Navigation character:** open-sea departure; landfall on Shetland by swell, birds and the
  coastal profile. Dead reckoning across the Norwegian Trench crossing.
- **Seamarks (to verify):**
  - Norwegian coast: Karmøy/Stavanger headland profile as departure marks.
  - Shetland landfall: Sumburgh Head / Fitful Head profiles, Fair Isle skerry group as a
    leading mark on approach.
- **Hazards:** SW wind can be foul (close reach on the outbound); tide races around Shetland
  headlands; summer storms (per [wind.md](wind.md)).
- **Season:** May–September.
- **Session:** 17 min @ 4× at k=32.

---

## S2 — Limfjord transit (Thyborøn → Aalborg)

- **Historical context:** in the Viking age the Limfjord was **open to the North Sea at its
  western end** (it closed by sand drift c. 1100–1200), making it a sheltered through-route
  across northern Jutland that avoided the dangerous sail around Skagen. Related hub: Hedeby
  (Haithabu) on the Schlei, with the overland portage to the Treene/Eider system.
- **Leg:** Thyborøn (56.70°N, 8.21°E) → Aalborg (57.05°N, 9.92°E): **110.8 km, bearing 68.8°**
  (ENE). This is a straight-line simplification; the real channel is winding — the UE level
  follows the real fjord axis, and the 110.8 km is the planning distance, not the sailed track.
- **Navigation character:** narrow-channel piloting, transits between headlands, shallow water,
  using the tide. The single best scenario for the lead line and tide gates.
- **Seamarks (to verify):** channel headland pairs, low coastal profiles, shore cairns.
- **Hazards:** shifting shoals, tidal streams through the narrows (strongest at the western
  opening and Agger/Thyborøn channel), lee shores in a crosswind.
- **Season:** May–September (winter ice possible historically).
- **Session:** 19 min @ 1× at k=32.

---

## S3 — Bergen → Shetland (Iceland route, leg 1)

- **Historical context:** first open-water leg of the North Atlantic settlement route
  (Norway → Shetland/Faroes → Iceland → Greenland). Governed by the **westerlies** — outbound
  legs run with the wind; the homeward (eastbound) legs fight it, which is why return voyages
  ran more southerly. This is the core "wind vs. square sail" scenario.
- **Leg:** Bergen (60.39°N, 5.32°E) → Lerwick (60.15°N, 1.15°W): **357.6 km, bearing 268.6°**
  (nearly due W).
- **Navigation character:** run/broad reach before the westerlies; latitude sailing (hold the
  sun/star altitude); landfall by swell direction, birds and the Shetland profile.
- **Seamarks (to verify):** Shetland landfall (Sumburgh/Fitful Head, Fair Isle); Bergen-side
  departure profile. Snæfellsjökull-type distant-peak landfall applies to the later Iceland
  leg, not this one.
- **Hazards:** North Atlantic swell; squalls; a backing wind can force the ship off the rhumb
  line; lee shore on Shetland if over-run.
- **Season:** May–September.
- **Session:** 15 min @ 4× at k=32.

---

## S4 — Vinland saga route (stretch/cut candidate)

- **Historical context:** the saga route Greenland → Helluland (Baffin) → Markland (Labrador) →
  Vínland (L'Anse aux Meadows, c. 1000). Documented but first on the cut list.
- **Legs (computed):** Eiriksfjord → Helluland 1,001 km @ 274°; Helluland → Markland 530 km @
  159°; Markland → L'Anse aux Meadows 607 km @ 142°.
- **Navigation character:** fog, icebergs, sea ice, cold-water swell; landfall by bird flight
  and swell direction; Labrador Current (south-flowing) as a drift hazard.
- **Session problem:** even at k=32, 8× warp, the shortest leg is ~22 min and the full route
  45 min. If kept, re-scope to a single coastal leg (Markland landfall) rather than a crossing.

---

## S5 — Birka → Visby (Gotland), Baltic

- **Historical context:** Baltic trade leg. Birka (Björkö, active c. 750–975) was a major
  emporium; Gotland was a trade nexus (its hoards testify to the eastern trade, the *Austrvegr*
  toward Novgorod/Holmgarðr and Miklagarðr). Visby's prominence is later (12th c.), so the
  scenario lands on Gotland rather than "at Visby".
- **Leg:** Birka (59.33°N, 17.55°E) → Visby (57.64°N, 18.30°E): **193.3 km, bearing 166.7°**
  (SSE).
- **Navigation character:** archipelago piloting between islands and skerries; short hops with
  land in sight much of the way.
- **Hazards:** shifty Baltic winds; **negligible tide** (a deliberate teaching contrast with
  S2/S6); autumn/winter ice out of season.
- **Session:** 16 min @ 2× at k=32.

---

## S6 — The North Way (Molde → Kristiansund coastal hop)

- **Historical context:** the Norwegian coastal route ("the way to the north", which names
  Norway). Ottar (Ohthere) of Hålogaland described sailing this coast and north to the White
  Sea c. 890. Fjord piloting par excellence.
- **Leg:** Molde (62.74°N, 7.16°E) → Kristiansund (63.11°N, 7.73°E): **50.5 km, bearing 34.5°**
  (NNE). Short hop chosen to fit a single lesson period; longer hops are candidate extra legs.
- **Navigation character:** fjord piloting, transits, headland rounding, inner-lead channels.
- **Hazards:** katabatic and channel-accelerated winds; strong tidal streams in sounds
  (Moskstraumen-type); lee shores under steep fjord walls.
- **Session:** 17 min @ 1× at k=16.

---

## Sources to verify (G1)

- Roesdahl, *The Vikings* — route geography and settlement chronology.
- Graham-Campbell, *The Viking World* — trade routes and emporia (Birka, Hedeby, Dublin).
- Englert & Trakadas (eds.), *Wulfstan's Voyage* — Baltic route detail.
- *Óláfs saga helga* (in *Heimskringla*) — sailing directions Norway→Greenland/Iceland.
- Adam of Bremen — Hedeby and Baltic context.
- Ingstad & Ingstad, *The Viking Discovery of America* — Vinland route.
- Modern charts / Admiralty sailing directions for exact seamark names, profiles and depths.
