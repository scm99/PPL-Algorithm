from problem import PPLScheduling
from csp import backtracking_search

# People
people = [
          'Daenarys Targaryen',
          'John Snow',
          'Arya Stark',
          'Ned Stark',
          'Cercei Lannister',
          'Little Finger',
          'Tyrion Lannister',
          'Lord Varys',
          'Joffrey Baratheon',
          'Samwell Tarly'
]          

navs = ['Daenarys Targaryen']

# Availabilities of all the People
availabilities = {
    ## Monday
    # 9h-10h30
    0: {'Daenarys Targaryen'},
    # 10h30-12h
    1: {'Daenarys Targaryen', 'John Snow'},
    # 14h-15h30
    2: {'Arya Stark', 'Ned Stark', 'John Snow', 'Daenarys Targaryen'},
    # 15h30-17h
    3: {'Arya Stark', 'Ned Stark', 'Cercei Lannister', 'John Snow', 'Daenarys Targaryen'},

    ## Tuesday
    # 9h-10h30
    4: {'Ned Stark'},
    # 10h30-12h
    5: {'Ned Stark', 'John Snow'},
    # 14h-15h30
    6: {'Arya Stark', 'Ned Stark', 'John Snow', 'Daenarys Targaryen'},
    # 15h30-17h
    7: {'Arya Stark', 'Ned Stark', 'Cercei Lannister', 'John Snow', 'Daenarys Targaryen'},

    ## Wednesday
    # 9h-10h30
    8: {'Ned Stark', 'Daenarys Targaryen',},
    # 10h30-12h
    9: {'Ned Stark', 'Daenarys Targaryen', 'John Snow'},
    # 14h-15h30
    10: {'Arya Stark', 'Ned Stark', 'John Snow', 'Daenarys Targaryen'},
    # 15h30-17h
    11: {'Arya Stark', 'Ned Stark', 'Cercei Lannister', 'John Snow', 'Daenarys Targaryen'},

    ## Thursday
    # 9h-10h30
    12: {'Ned Stark', 'Daenarys Targaryen'},
    # 10h30-12h
    13: {'Ned Stark', 'Daenarys Targaryen'},
    # 14h-15h30
    14: {'Arya Stark', 'Ned Stark', 'Daenarys Targaryen'},
    # 15h30-17h
    15: {'Arya Stark', 'Ned Stark', 'Cercei Lannister', 'Daenarys Targaryen'},

    ## Friday
    # 9h-10h30
    16: {'Lord Varys', 'Daenarys Targaryen', 'Tyrion Lannister', 'Joffrey Baratheon', 'Little Finger'},
    # 10h30-12h
    17: {'Lord Varys', 'Daenarys Targaryen', 'Tyrion Lannister', 'Joffrey Baratheon', 'Little Finger'},
    # 14h-15h30
    18: {'Samwell Tarly', 'Daenarys Targaryen', 'Tyrion Lannister', 'Joffrey Baratheon', 'Little Finger'},
    # 15h30-17h
    19: {'Samwell Tarly', 'Daenarys Targaryen', 'Tyrion Lannister', 'Joffrey Baratheon', 'Little Finger'},
    
}

# Initialize the Problem
scheduling_problem = PPLScheduling(people=people, availabilities=availabilities, navs = navs, consider_navs = True)

# Search a Solution
backtracking_search(csp=scheduling_problem)#, select_unassigned_variable=mrv)#, order_domain_values=lcv)#, select_unassigned_variable=mrv)
# Display Solution
scheduling_problem.display(scheduling_problem.infer_assignment())

