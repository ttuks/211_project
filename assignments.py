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
        if self.title.strip() == "":
            error.append("Required title entry")
        
        if len(self.course) != 6:
            error.append("Incorrect course code")
        
        try:
            float(self.weight)
        except ValueError:
            error.append("Not a number")
        else:
            if float(self.weight) < 0 or float(self.weight) > 100:
                error.append("Invalid weight")
                
        
        return error

    def remaining(self):
        remainingdate = (date.fromisoformat(self.due) - date.today()).days
        return remainingdate
    
    def overdue(self):
        if self.remaining() < 0 and self.status != "Done":
            return True
        else:
            return False
    
