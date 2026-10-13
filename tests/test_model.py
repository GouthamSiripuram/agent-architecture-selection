import pytest
from agent_arch_select.model import recommend_architecture, score_architectures

def base():
    return {"decomposability":.5,"specialization_need":.5,"verification_value":.5,
            "coordination_burden":.5,"error_propagation_risk":.5,"resource_sensitivity":.5}

def test_nan_rejected():
    x=base(); x["decomposability"]=float("nan")
    with pytest.raises(ValueError):
        recommend_architecture(x)

def test_out_of_range_rejected():
    x=base(); x["verification_value"]=1.1
    with pytest.raises(ValueError):
        score_architectures(x)

def test_negative_cost_aversion_rejected():
    with pytest.raises(ValueError):
        score_architectures(base(), cost_aversion=-1)

def test_high_cost_and_coordination_prefers_simple_family():
    x={"decomposability":.1,"specialization_need":.1,"verification_value":.1,
       "coordination_burden":.7,"error_propagation_risk":.7,"resource_sensitivity":1.0}
    assert recommend_architecture(x) in {"single_agent","single_agent_tools"}

@pytest.mark.parametrize("tolerance", [-1, float("nan"), float("inf")])
def test_invalid_tie_tolerance_rejected(tolerance):
    with pytest.raises(ValueError):
        recommend_architecture(base(), tie_tolerance=tolerance)

def test_exact_tie_requires_resolution():
    with pytest.raises(ValueError, match="tie requires explicit resolution"):
        recommend_architecture(dict.fromkeys(base(), 0))

def test_controlled_example_matches_documented_utilities():
    assert score_architectures(base()) == pytest.approx({
        'single_agent': -.020, 'single_agent_tools': .100,
        'planner_executor_verifier': .275, 'hierarchical_multi_agent': .150,
    })

def test_resource_aversion_cannot_increase_utility():
    lower, higher = score_architectures(base(), 0), score_architectures(base(), 4)
    assert all(higher[a] < lower[a] for a in lower)
