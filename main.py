from problem import PPLScheduling
from csp import backtracking_search

# People
people = [
          'Alvaro',
          'Anne-Lise',
          'Sara',
          'Corentin',
          'John Holden',]

navs = ['Sara']

# Availabilities of all the People
availabilities = {
    ## Monday
    # 9h-10h30
    0: {'Sara'},
    # 10h30-12h
    1: {'Sara', 'John Holden'},
    # 14h-15h30
    2: {'Alvaro', 'Anne-Lise', 'John Holden', 'Sara'},
    # 15h30-17h
    3: {'Alvaro', 'Anne-Lise', 'Corentin', 'John Holden', 'Sara'},

    ## Tuesday
    # 9h-10h30
    4: {'Anne-Lise'},
    # 10h30-12h
    5: {'Anne-Lise', 'John Holden'},
    # 14h-15h30
    6: {'Alvaro', 'Anne-Lise', 'John Holden', 'Sara'},
    # 15h30-17h
    7: {'Alvaro', 'Anne-Lise', 'Corentin', 'John Holden', 'Sara'},

    #{'Alex', 'Alvaro', 'Anne-Lise', 'Corentin', 'François Wagner', 'Hadrien', 'Ines', 'John Holden', 'Margaux', 'Mathurin', 'Nourhen', 'Pauline', 'Sara', 'Thomas Raby', 'Yannis'},


    ## Wednesday
    # 9h-10h30
    8: {'Anne-Lise', 'Sara',},
    # 10h30-12h
    9: {'Anne-Lise', 'Sara', 'John Holden'},
    # 14h-15h30
    10: {'Alvaro', 'Anne-Lise', 'John Holden', 'Sara'},
    # 15h30-17h
    11: {'Alvaro', 'Anne-Lise', 'Corentin', 'John Holden', 'Sara'},

    ## Thursday
    # 9h-10h30
    12: {'Anne-Lise', 'Sara'},
    # 10h30-12h
    13: {'Anne-Lise', 'Sara'},
    # 14h-15h30
    14: {'Alvaro', 'Anne-Lise', 'Sara'},
    # 15h30-17h
    15: {'Alvaro', 'Anne-Lise', 'Corentin', 'Sara'},

    ## Friday
    # 9h-10h30
    16: {'Nourhen', 'Sara', 'Sofiane', 'Thomas Raby', 'Yannis'},
    # 10h30-12h
    17: {'Nourhen', 'Sara', 'Sofiane', 'Thomas Raby', 'Yannis'},
    # 14h-15h30
    18: {'Ines', 'Sara', 'Sofiane', 'Thomas Raby', 'Yannis'},
    # 15h30-17h
    19: {'Ines', 'Sara', 'Sofiane', 'Thomas Raby', 'Yannis'},
    
}

# Initialize the Problem
scheduling_problem = PPLScheduling(people=people, availabilities=availabilities, navs = navs, consider_navs = True)

# Search a Solution
backtracking_search(csp=scheduling_problem)#, select_unassigned_variable=mrv)#, order_domain_values=lcv)#, select_unassigned_variable=mrv)
# Display Solution
scheduling_problem.display(scheduling_problem.infer_assignment())

