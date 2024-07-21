class Project:
    """Represent a project with details such as name, start date, priority, cost estimate, and completion percentage."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)
    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"
    def __repr__(self):
        """Return a detailed string representation of the project."""
        return f"Project({self.name!r}, {self.start_date!r}, {self.priority!r}, {self.cost_estimate!r}, {self.completion_percentage!r})"
    def __lt__(self, other):
        """Compare projects based on priority."""
        return self.priority < other.priority