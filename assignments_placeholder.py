from datetime import date


assignmentstatus = ["Not Started", "In Progress", "Done"]


class CourseAssignment:
    def __init__(self, course,title,due,weight,status):
        self.course = course
        self.title = title
        self.due = due
        self.weight = weight
        self.status = status

    def inputcheck(self):
        error = []
        if self.course.strip() == "":
            error.append("Missing course information")

    def remaining(self):
        remainingdate = (date.fromisoformat(self.due) - date.today()).days
        return remainingdate
    
    def overdue(self):
        if self.remaining() < 0 and self.status != "Done":
            return True
        else:
            return False
    
