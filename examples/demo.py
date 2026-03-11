from core.belief_graph import Belief
from core.propagation_engine import BeliefEdge

# belief A
interest_rates = Belief(
    belief_id="interest_rates_increase",
    statement="Interest rates are increasing",
    confidence=0.6
)

# belief B
housing_affordability = Belief(
    belief_id="affordability_declines",
    statement="Housing affordability declines when interest rates rise",
    confidence=0.5
)

print("Initial beliefs")
print("Interest rates:", interest_rates.confidence)
print("Affordability:", housing_affordability.confidence)

# add evidence to belief A
interest_rates.add_evidence(0.85)
interest_rates.update_confidence()

print("\nAfter evidence update")
print("Interest rates:", interest_rates.confidence)

# connect beliefs
edge = BeliefEdge(
    source=interest_rates,
    target=housing_affordability,
    weight=0.7
)

# propagate change
edge.propagate()

print("\nAfter propagation")
print("Affordability:", housing_affordability.confidence)
