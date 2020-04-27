class MoodReport:
    """The MoodReport object contains data from two tables, mood_report
    and mood_value, mood_value exists for deduplication purposes"""

    def __init__(self, id, mood_value_id, user_id, date, mood_value):
        self.id = id
        self.mood_value_id = mood_value_id
        self.user_id = user_id
        self.date = date
        self.mood_value = mood_value