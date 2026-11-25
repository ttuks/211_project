import shelve
from assignments import CourseAssignment

class StorageData:
    def __init__(self):
        self.filename = "deadline_data"
    def load(self):
        db = shelve.open(self.filename)
        if "assignments" in db:
            assignments = db["assignments"]
        else:
            assignments = self.get_starter()
        db.close()
        return assignments

    def save(self, assignments):
        db = shelve.open(self.filename)
        db["assignments"] = assignments
        db.close()

    def get_starter(self):
        data = [["CCT202", "Reading Notes week1","2026-09-17",1,"Done"],
               ["CCT202", "Reading Notes week2","2026-09-24",1,"Done"],
               ["CCT202", "Reading Notes week3","2026-10-01",1,"Done"],
               ["CCT202", "Reading Notes week4","2026-10-08",1,"Done"],
               ["CCT202", "HMC Relationship Report Presentation", "2026-10-13", 10, "Done"],
               ["CCT202", "HMC Relationship Report (Individual)", "2026-10-15", 20, "Done"],
               ["CCT202", "HMC Relationship Presentation Peer-Reflection", "2026-10-23", 7, "Done"],
               ["CCT202", "Human-Machine Interface Proposal (Group)", "2026-11-16", 30, "In Progress"],
               ["CCT202", "Human-Machine Interface Proposal Presentation (in-class)", "2026-11-20", 10, "Not Started"],
               ["CCT204", "Sketching: Photoshop", "2026-09-12", 1, "Done"],
               ["CCT204", "Introduction to Adobe Illustrator", "2026-09-21", 1, "Done"],
               ["CCT204", "Typography in Illustrator", "2026-09-28", 1, "Done"],
               ["CCT204", "Norman Doors in the GTA", "2026-10-01", 20, "Done"],
               ["CCT204", "Getting Started in Blender 3D", "2026-10-19", 1, "Done"],
               ["CCT204", "Redesign an Everyday Thing Project", "2026-11-05", 20, "Done"],
               ["CCT204", "Design Thinking Final Project", "2026-12-01", 30, "In Progress"],
               ["CCT208", "Quiz1", "2026-09-18", 1, "Done"],
               ["CCT208", "Quiz2", "2026-09-25", 1, "Done"],
               ["CCT208", "Quiz3", "2026-10-02", 1, "In Progress"],
               ["CCT208", "Midterm", "2026-11-09", 30, "Not Started"],
               ["CCT211", "LAB10", "2026-11-23", 1, "Not Started"],
               ["CCT211", "LAB11", "2026-11-30", 1, "Not Started"],
               ["CCT211", "Project 2: Persistent Form", "2026-12-01", 25, "In Progress"],
               ["CCT211", "LAB12", "2026-12-07", 1, "Not Started"],
               ["CCT211", "LAB9", "2026-11-16", 1, "Done"],
               ["CCT211", "Final test", "2026-12-22", 30, "Not Started"],
               ["WRI293", "A2: Multimodal Communication", "2026-12-12", 30, "In Progress"],
               ["WRI293", "A1: Software Documentation", "2026-10-23", 20, "Done"],
               ["WRI293", "Midterm Visual Based", "2026-10-14", 15, "Done"],
               ["WRI293", "Everyday Critique1", "2026-09-30", 10, "Done"],
               ["WRI293", "Everyday Critique2", "2026-11-09", 10, "Done"],]
        assignments = []
        for d in data:
            assignments.append(CourseAssignment(d[0], d[1], d[2], d[3], d[4]))
        return assignments


