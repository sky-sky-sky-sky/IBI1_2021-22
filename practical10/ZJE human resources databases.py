class Staff(object):
    def __init__(self,firstname,lastname,location,role):
        self.firstname=firstname
        self.location=location
        self.lastname=lastname
        self.role=role
c=Staff('yuxing','che','International Campus','administration')
print('name is',c.firstname,c.lastname,'. the location is',c.location,'. the role is',c.role,'.')
