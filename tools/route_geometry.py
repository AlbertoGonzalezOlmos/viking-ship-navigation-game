#!/usr/bin/env python3
"""
Route geometry toolkit for the Viking Ship Navigation Game.

Phase 1 research support (docs/research/routes.md, docs/design/physics.md §3.5):
  - great-circle leg distances and initial (forward) bearings
  - horizon / seamark visibility distances
  - the world-scale model from the project plan (D1, §3.5):
      ship 1:1, geography uniform 1:k, identification range as a fraction of leg length

Usage:
  python3 tools/route_geometry.py            # print full tables
  python3 tools/route_geometry.py --json     # machine-readable output
  python3 tools/route_geometry.py --scale k=32 warp=4  # session-length table

All coordinates are WGS84 (lat, lon) in decimal degrees. Distances are great-circle
on a mean-Earth radius of 6371 km (adequate for waypoint planning; final levels use
per-scenario projected coordinates).
"""

import argparse
import json
import math

EARTH_RADIUS_KM = 6371.0
KN_TO_KMH = 1.852


def great_circle(lat1, lon1, lat2, lon2):
    """Return (distance_km, initial_bearing_deg) from point 1 to point 2."""
    p1, q1 = math.radians(lat1), math.radians(lon1)
    p2, q2 = math.radians(lat2), math.radians(lon2)
    dq = q2 - q1
    dp = p2 - p1
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dq / 2) ** 2
    dist = 2 * EARTH_RADIUS_KM * math.asin(min(1.0, math.sqrt(a)))
    y = math.sin(dq) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dq)
    bearing = (math.degrees(math.atan2(y, x)) + 360.0) % 360.0
    return dist, bearing


def horizon_distance(eye_height_m, object_height_m, refraction=1.08):
    """Radar/visual horizon distance in km. Standard atmospheric refraction ~8%."""
    return refraction * 3.57 * (math.sqrt(eye_height_m) + math.sqrt(object_height_m))


# --------------------------------------------------------------------------- #
# Route database. "seamarks" are illustrative (from the plan's §2.2); heights  #
# are placeholders to be replaced from research maps during Phase 1.           #
# --------------------------------------------------------------------------- #

ROUTES = {
    "S0": {
        "name": "Tutorial: home waters (fictionalized Roskilde-fjord-like circuit)",
        "ship": "karvi",
        "waypoints": [
            ("Start", 55.74, 12.06),
            ("N-mid", 55.78, 12.02),
            ("E-mid", 55.75, 11.95),
            ("Finish", 55.64, 12.09),
        ],
    },
    "S1": {
        "name": "Rogaland (Stavanger) -> Shetland (Lerwick)",
        "ship": "longship",
        "waypoints": [
            ("Stavanger", 58.9700, 5.7331),
            ("Lerwick", 60.1540, -1.1491),
        ],
    },
    "S2": {
        "name": "Limfjord transit (Thyboron -> Aalborg)",
        "ship": "knarr",
        "waypoints": [
            ("Thyboron", 56.7000, 8.2100),
            ("Aalborg", 57.0480, 9.9180),
        ],
    },
    "S3": {
        "name": "Bergen -> Shetland (first leg of the Iceland route)",
        "ship": "knarr",
        "waypoints": [
            ("Bergen", 60.3913, 5.3221),
            ("Lerwick", 60.1540, -1.1491),
        ],
    },
    "S4": {
        "name": "Vinland saga route (Greenland -> Helluland -> Markland -> Vinland)",
        "ship": "knarr",
        "waypoints": [
            ("Eiriksfjord (Brattahlid)", 61.1520, -45.5170),
            ("Helluland (S. Baffin)", 60.5000, -64.0000),
            ("Markland (Labrador)", 56.0000, -61.0000),
            ("L'Anse aux Meadows", 51.5963, -55.5320),
        ],
    },
    "S5": {
        "name": "Birka -> Visby (Gotland), Baltic",
        "ship": "longship (trade)",
        "waypoints": [
            ("Birka (Bjorko)", 59.3340, 17.5510),
            ("Visby", 57.6400, 18.3000),
        ],
    },
    "S6": {
        "name": "The North Way (Molde -> Kristiansund coastal hop)",
        "ship": "karvi",
        "waypoints": [
            ("Molde", 62.7370, 7.1590),
            ("Kristiansund", 63.1100, 7.7280),
        ],
    },
}

# Ship cruise speed (kn) used for session-length estimates.
CRUISE_KN = 6.0

# Per-scenario scale factors and warp from the plan (§3.2), tunable.
DEFAULT_SCALE = {"S0": 8, "S1": 32, "S2": 32, "S3": 32, "S4": 32, "S5": 32, "S6": 16}
DEFAULT_WARP = {"S0": 1, "S1": 4, "S2": 1, "S3": 4, "S4": 8, "S5": 2, "S6": 1}


def route_table():
    rows = []
    for sid, r in ROUTES.items():
        legs = []
        total = 0.0
        for i in range(len(r["waypoints"]) - 1):
            (n1, a1, b1), (n2, a2, b2) = r["waypoints"][i], r["waypoints"][i + 1]
            d, brg = great_circle(a1, b1, a2, b2)
            total += d
            legs.append({"from": n1, "to": n2, "km": round(d, 1), "bearing": round(brg, 1)})
        rows.append(
            {
                "id": sid,
                "name": r["name"],
                "ship": r["ship"],
                "legs": legs,
                "total_km": round(total, 1),
            }
        )
    return rows


def session_table(scale=None, warp=None):
    scale = scale or DEFAULT_SCALE
    warp = warp or DEFAULT_WARP
    rows = []
    for sid, r in ROUTES.items():
        total = sum(
            great_circle(a1, b1, a2, b2)[0]
            for (_, a1, b1), (_, a2, b2) in zip(r["waypoints"], r["waypoints"][1:])
        )
        k = scale.get(sid, 32)
        w = warp.get(sid, 1)
        game_km = total / k
        hours = game_km / (CRUISE_KN * KN_TO_KMH)
        minutes = hours * 60 / w
        rows.append(
            {
                "id": sid,
                "real_km": round(total, 1),
                "k": k,
                "warp": w,
                "game_km": round(game_km, 2),
                "hours_1x": round(hours, 2),
                "minutes": round(minutes, 1),
            }
        )
    return rows


def identification_ranges(leg_km, eye_m=5.0, refraction=1.08):
    """§3.5 rule: IdentRange = (real horizon / real leg) * in-game leg, per seamark class."""
    classes = [
        ("Major peak", 1000.0),
        ("Island / skerry group", 200.0),
        ("Headland / low profile", 50.0),
        ("Cairn / horgr, small skerry", 3.0),
    ]
    out = []
    for name, h in classes:
        hz = horizon_distance(eye_m, h, refraction)
        frac = hz / leg_km
        out.append(
            {
                "class": name,
                "height_m": h,
                "real_horizon_km": round(hz, 1),
                "fraction_of_leg": round(frac, 4),
            }
        )
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--scale", default=None, help="override scale, e.g. k=32")
    ap.add_argument("--warp", default=None, help="override warp, e.g. warp=4")
    ap.add_argument("--ident", default=None, help="identification ranges for a leg, e.g. 358")
    args = ap.parse_args()

    scale = dict(DEFAULT_SCALE)
    warp = dict(DEFAULT_WARP)
    if args.scale:
        k = int(args.scale.split("=")[1])
        scale = {sid: k for sid in ROUTES}
    if args.warp:
        w = int(args.warp.split("=")[1])
        warp = {sid: w for sid in ROUTES}

    out = {
        "routes": route_table(),
        "sessions": session_table(scale, warp),
        "cruise_kn": CRUISE_KN,
    }
    if args.ident:
        out["identification"] = identification_ranges(float(args.ident))

    if args.json:
        print(json.dumps(out, indent=2))
        return

    print("=== Viking sea routes: great-circle legs ===")
    for r in out["routes"]:
        print(f"\n{r['id']}  {r['name']}  [{r['ship']}]  total {r['total_km']} km")
        for l in r["legs"]:
            print(f"    {l['from']:26s} -> {l['to']:26s} {l['km']:7.1f} km   bearing {l['bearing']:6.1f}°")

    print("\n\n=== Session length at scale k (cruise 6 kn) ===")
    print(f"{'id':4s} {'real km':>8s} {'k':>3s} {'warp':>5s} {'game km':>8s} {'h@1x':>6s} {'min':>7s}")
    for s in out["sessions"]:
        print(
            f"{s['id']:4s} {s['real_km']:8.1f} {s['k']:3d} {s['warp']:5d} "
            f"{s['game_km']:8.2f} {s['hours_1x']:6.2f} {s['minutes']:7.1f}"
        )

    if "identification" in out:
        print("\n\n=== Seamark identification ranges (fraction-of-leg rule, §3.5) ===")
        for c in out["identification"]:
            print(
                f"  {c['class']:32s} h={c['height_m']:7.0f} m  horizon {c['real_horizon_km']:5.1f} km "
                f" -> {c['fraction_of_leg']*100:5.1f}% of leg"
            )


if __name__ == "__main__":
    main()
