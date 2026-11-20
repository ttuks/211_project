import shelve
class StorageData:
    def __init__(self):
        self.filename = "deadline_data"
    def load(self):
        db = shelve.open(self.filename)
        if "assignments" in db:
            assignments = db["assignments"]
        else:
            assignments = []
        db.close()
        return assignments
    def save(self, assignments):
        db = shelve.open(self.filename)
        db["assignments"] = assignments
        db.close()