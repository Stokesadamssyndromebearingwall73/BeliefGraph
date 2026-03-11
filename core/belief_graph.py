class Belief:
    def __init__(self, belief_id, statement, confidence=0.5):
        self.belief_id = belief_id
        self.statement = statement
        self.confidence = confidence
        self.evidence = []

    def add_evidence(self, likelihood):
        self.evidence.append(likelihood)

    def update_confidence(self):
        prior = self.confidence

        for likelihood in self.evidence:
            evidence_prob = (
                likelihood * prior +
                (1 - likelihood) * (1 - prior)
            )
            posterior = (likelihood * prior) / evidence_prob
            prior = posterior

        self.confidence = prior
        return self.confidence
