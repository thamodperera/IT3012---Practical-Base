# logic_engine.py


class KnowledgeBase:
    """
    A declarative Knowledge Base (KB) storing Facts and Rules (Horn Clauses),
    equipped with a Forward Chaining inference engine using Modus Ponens.
    """

    def __init__(self):
        # Set to store unique string facts (e.g., "TargetVisible")
        self.facts = set()
        # List to store rules as Tuples: ([list_of_premises], "conclusion_string")
        self.rules = []

    def tell_fact(self, fact_string: str):
        """Adds a fact to the facts set."""
        self.facts.add(fact_string)

    def tell_rule(self, premise_list: list, conclusion_string: str):
        """Appends a rule as a tuple of (premise_list, conclusion_string) to rules."""
        self.rules.append((premise_list, conclusion_string))

    def clear_facts(self):
        """Empties the facts set."""
        self.facts.clear()

    def forward_chain(self):
        """
        Data-driven Forward Chaining algorithm.
        Iteratively applies Generalized Modus Ponens across all Horn clauses
        until a full pass results in no newly deduced facts.
        """
        new_facts_added = True

        while new_facts_added:
            new_facts_added = False

            for premises, conclusion in self.rules:
                if conclusion not in self.facts:
                    # Modus Ponens Check: If all premises are known facts
                    if all(p in self.facts for p in premises):
                        self.facts.add(conclusion)
                        new_facts_added = True
