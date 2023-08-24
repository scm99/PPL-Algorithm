from csp import CSP
from prettytable import PrettyTable
import copy



# Class for PPL Problem Definition
class PPLScheduling(CSP):

    def __init__(self, people, availabilities, navs, consider_navs = True):
        """Initialize Problem of Scheduling the slots for the PPL."""

        # Case in which we should or not consider navs
        self.consider_navs = consider_navs

        # People's Availabilities rearranged
        domains = dict()
        for person in people:
            personal_availability = []
            for slot in availabilities:
                if person in availabilities[slot]:
                    personal_availability.append(slot)

            domains[person] = personal_availability

        # If some people are doing navs take that into account and rearrange domains 
        if consider_navs:
            self.navs = navs
            for name in navs:
                aux_name = name+"1"
                people.append(aux_name)
                domains[aux_name] = domains[name]

        # Save problem variables and respective domains
        self.variables = people
        self.domains = domains

        # Find Constraints for all people
        neighbors = dict()
        for person in people:
            personal_neighbors = copy.copy(people)
            personal_neighbors.remove(person)
            neighbors[person] = personal_neighbors
        self.neighbors = neighbors 

        # Initialize Constraint Satisfaction Problem
        self.csp = CSP.__init__(self, variables=self.variables, domains=self.domains, neighbors=self.neighbors, constraints=ppl_constraint)


    def display(self, solution):
        """
        Method to display the solution found.
        """
        
        plan = [''] * 20

        # In case we consider navs
        if self.consider_navs:
            for person in self.variables:
                slot = solution[person]
                if person[:-1] in self.navs:
                    plan[slot] = person[:-1]
                else:
                    plan[slot] = person
        else:
            for person in self.variables:
                slot = solution[person]
                plan[slot] = person

        # Create Table
        t = PrettyTable([' ', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        t.add_row(['9h-10h30', plan[0], plan[4], plan[8], plan[12], plan[16]])
        t.add_row(['10h30-12h', plan[1], plan[5], plan[9], plan[13], plan[17]])
        t.add_row(['14h-15h30', plan[2], plan[6], plan[10], plan[14], plan[18]])
        t.add_row(['15h30-17h', plan[3], plan[7], plan[11], plan[15], plan[19]])
        print(t)


def ppl_constraint(A, a, B, b):
    """Constraint for PPL Scheduling"""

    # Case in which we have navs - slots must be one after the other and only options (0, 1) or (2, 3)
    if A == B[:-1] or A[:-1] == B:
        return (a == (b+1) and (b % 2 == 0)) or ((a+1) == b and (a % 2 == 0))
    
    # All people should have different slots
    else:
        return a != b
