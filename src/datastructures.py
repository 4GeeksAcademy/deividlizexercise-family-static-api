
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = []

        

    def _generateId(self):
        generated_Id = self._next_id
        self._next_id += 1
        return generated_Id

    def add_member(self, member : dict):
        self.member = member
        self.member['id'] = self._generateId()
        self.member['last_name'] = self.last_name
        self.member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(self.member)
        return self._members
    
        # fill this method and update the return
       

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return True


    def get_member(self, id):
        for member in self._members:
            if member['id'] == int(id):
                return member
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
