"""Generate independently varied synthetic architecture-selection scenarios.
These are design probes, not empirical labels or measured LLM outcomes.
"""
import json, random
from pathlib import Path

FEATURES = [
    "decomposability","specialization_need","verification_value",
    "coordination_burden","error_propagation_risk","resource_sensitivity"
]

def main(out_path="data/architecture_scenarios_v0_2.jsonl", n=48, seed=260907):
    rng = random.Random(seed)
    out = Path(out_path); out.parent.mkdir(parents=True, exist_ok=True)
    # Independent seeded variation avoids hard-wiring high decomposability to low coordination burden.
    rows=[]
    for i in range(n):
        row={"scenario_id":f"CAAA2-{i+1:03d}", "synthetic":True}
        row.update({k:round(rng.random(), 6) for k in FEATURES})
        rows.append(row)
    with out.open("w") as f:
        for r in rows: f.write(json.dumps(r)+"\n")
    print(f"Wrote {n} independently varied synthetic scenarios to {out}")

if __name__ == "__main__":
    main()
