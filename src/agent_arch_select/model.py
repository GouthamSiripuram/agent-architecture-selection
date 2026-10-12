from __future__ import annotations
import math
from typing import Dict, Mapping

ARCHITECTURES = (
    "single_agent",
    "single_agent_tools",
    "planner_executor_verifier",
    "hierarchical_multi_agent",
)

COEFFICIENTS = {
    "single_agent":              dict(D=.05, S=.05, V=.02, H=.05, P=.06, K=.05),
    "single_agent_tools":        dict(D=.10, S=.30, V=.08, H=.08, P=.08, K=.12),
    "planner_executor_verifier": dict(D=.45, S=.35, V=.70, H=.35, P=.25, K=.35),
    "hierarchical_multi_agent":  dict(D=.85, S=.80, V=.65, H=.75, P=.55, K=.70),
}

FEATURE_MAP = {
    "decomposability":"D",
    "specialization_need":"S",
    "verification_value":"V",
    "coordination_burden":"H",
    "error_propagation_risk":"P",
    "resource_sensitivity":"K",
}

def _feature(value, name):
    value = float(value)
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"{name} must be finite and in [0,1]; got {value!r}")
    return value

def _validated_features(features: Mapping[str, float]) -> dict[str,float]:
    missing = [k for k in FEATURE_MAP if k not in features]
    if missing:
        raise KeyError(f"missing features: {missing}")
    return {k:_feature(features[k], k) for k in FEATURE_MAP}

def architecture_utility(features: Mapping[str,float], architecture: str, cost_aversion: float = 1.0) -> float:
    if architecture not in COEFFICIENTS:
        raise KeyError(architecture)
    cost_aversion = float(cost_aversion)
    if not math.isfinite(cost_aversion) or cost_aversion < 0:
        raise ValueError("cost_aversion must be finite and non-negative")
    x = _validated_features(features)
    c = COEFFICIENTS[architecture]
    return (
        c["D"]*x["decomposability"]
        + c["S"]*x["specialization_need"]
        + c["V"]*x["verification_value"]
        - c["H"]*x["coordination_burden"]
        - c["P"]*x["error_propagation_risk"]
        - cost_aversion*c["K"]*x["resource_sensitivity"]
    )

def score_architectures(features: Mapping[str,float], cost_aversion: float = 1.0) -> Dict[str,float]:
    return {a: architecture_utility(features, a, cost_aversion) for a in ARCHITECTURES}

def recommend_architecture(features: Mapping[str,float], cost_aversion: float = 1.0,
                           tie_tolerance: float = 1e-12) -> str:
    scores = score_architectures(features, cost_aversion)
    best = max(scores.values())
    winners = [a for a, s in scores.items() if abs(s-best) <= tie_tolerance]
    if len(winners) != 1:
        raise ValueError(f"architecture tie requires explicit resolution: {winners}")
    return winners[0]
