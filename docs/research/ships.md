# Ships and the Sail Polar — Research Draft

**Status:** Draft v0.1 for G1/G3 review. Dimensions are from published archaeological reports and
are reliable to the stated precision; **sail areas, displacement and polar coefficients must be
verified against the Roskilde sea-trial publications before G3.** Do not ship physics constants
from this draft without the G3 validation procedure (plan §4.4).

---

## Ship types used

| Type | Role | Representative find | Length | Beam | Notes |
|---|---|---|---|---|---|
| **knarr** | Ocean cargo/trader | Skuldelev 1 (c. 1030, Norway) | ~16.3 m | ~4.8 m | Deeper, beamier hull resists leeway; ~24 t cargo; sail ~78 m² (verify) |
| **longship** | War/speed (also trade) | Skuldelev 2 (c. 1042, Dublin) | ~29.4 m | ~3.8 m | ~60 oars; sail ~112 m² (verify); shallow draft, fast, more leeway |
| **karvi** | Small general-purpose | Skuldelev 3 (c. 1040, Denmark) | ~14 m | ~3.3 m | Sail ~45 m² (verify); few oars; coastal work |

*Reference dimensions also: Oseberg (21.5 m, 15 oar-pairs, c. 820); Gokstad (23.2 m, 16
oar-pairs, c. 890, sail est. ~110 m²). These inform hull-form modelling and steering-oar
geometry but are not the player ships.*

---

## The steering oar (*stjórn*)

- Mounted on the **starboard quarter** through a withy/pin; helmsman works a tiller.
  *stjórnborði* (starboard) = "steering-board side"; *bakborði* (port) = the side the helmsman
  had his back to.
- Blade is a broad hydrofoil, pivoting ~30–45° each side. The off-centre, single-side mount
  means the oar is asymmetric: a centred oar still imparts slight yaw, and authority drops at
  low speed (∝ flow²) and when heel lifts the blade out of water. These are modelled (§4.2–4.3).
- **This is the player's only steering control, driven from Scratch (§6).**

---

## Speeds and the sail polar (plan §4.4)

**Speed (planning, reconstruction-derived):** knarr cruise 5–7 kn; longship bursts higher
(replica *Sea Stallion* has exceeded 12–14 kn under sail in favourable conditions). Rowing is
crew-power-limited and well below hull speed.

**The two angles that matter — do not conflate them:**

| Quantity | Symbol | Design default | Meaning | Source to verify |
|---|---|---|---|---|
| Luffing angle | θ_luff | **55° ± 5° off the true wind** | Inside this the sail shivers and drive → ~0 | Square-sail wind-tunnel + replica trials |
| Best-VMG angle | θ_vmg | θ_luff + 10–15° | Course that maximizes velocity made good to windward | Same trials; operational rule of thumb |

- θ_luff is a **default to be fixed by G3 validation**, not an asserted fact.
- Sailing at θ_luff "feels heroic and goes nowhere" — exactly the learner mistake the game
  teaches. θ_vmg is the working upwind angle.
- Angles are specified against **true** wind in the physics doc and displayed against
  **apparent** wind in the HUD/instructor mode, with the distinction documented (a classic
  error source).

**Leeway:** 5–15° to leeward close-hauled, larger for the longship (shallower) than the knarr
(deeper). The player must aim upwind of the mark — a core teaching point.

---

## Physics model inputs needed (G3)

1. Sail lift/drag polar (C_L, C_D vs. angle of attack) for a square sail, from wind-tunnel and
   replica-trial data.
2. Sail area per ship type (verify ~78 / ~112 / ~45 m² above).
3. Hull drag polar and lateral-resistance coefficients per hull form (knarr vs longship vs karvi).
4. Steering-oar blade area, pivot geometry and lift coefficient.
5. Buoyancy sample layout per hull (8–16 points).

All of these feed `docs/design/physics.md` (equations, coefficients, sources) and the Phase 3
sandbox; the G3 automated polar sweep (§11) validates the resulting θ_luff and θ_vmg against the
reference table.

---

## Sources to verify (G3)

- Viking Ship Museum Roskilde — excavation reports for Skuldelev 1/2/3/5 and the *Ottar*
  (Skuldelev 1) and *Sea Stallion from Glendalough* (Skuldelev 2) sea-trial publications.
- Crumlin-Pedersen, *Viking-Age Ships and Shipbuilding in Hedeby/Haithabu and Schleswig*.
- Published square-sail aerodynamics (wind-tunnel) used by the reconstructions.
- Reconstruction voyage logs (*Sea Stallion* 2007–08 Roskilde–Dublin) for speed and leeway data.
