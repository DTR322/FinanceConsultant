class RBGoal:
    def __init__(self,
                 goal_id: int | None = None,
                 priority: int | None = None):
        self.id = goal_id
        self.priority = priority

    def to_dict(self) -> dict:
        data = {'id': self.id, 'priority': self.priority}
        return {k: v for k, v in data.items() if v is not None}
