# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#     # Money spent by Olivia
#     money_spent = bagels * bagel_cost
#     # Money left with Olivia
#     money_left = money_initial - money_spent
#     # Result
#     result = money_left
#     return result

MATH_PROMPT = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

# solution in Python:


def solution():
    """Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"""
    # Olivia has $23
    money_initial = 23
    # She bought five bagels
    bagels = 5
    # for $3 each
    bagel_cost = 3
    # Money spent by Olivia for buying bagels is bagels * bagel_cost
    money_spent = bagels * bagel_cost
    # Money left with Olivia is money_initial - money_spent
    money_left = money_initial - money_spent
    # Result
    result = money_left
    return result





Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

# solution in Python:


def solution():
    """Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"""
    # Michael had 58 golf balls
    golf_balls_initial = 58
    # On tuesday, he lost 23 golf balls
    golf_balls_lost_tuesday = 23
    # On wednesday, he lost 2 more
    golf_balls_lost_wednesday = 2
    # Golf balls left at the end is golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    # Result
    result = golf_balls_left
    return result





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

# solution in Python:


def solution():
    """There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
    # There were nine computers in the server room
    computers_initial = 9
    # Five more computers were installed each day
    computers_per_day = 5
    # from monday to thursday there are 4 days
    num_days = 4
    # Number of computers added is computers_per_day * num_days  
    computers_added = computers_per_day * num_days
    # Total number of computers is computers_initial + computers_added 
    computers_total = computers_initial + computers_added
    # Result
    result = computers_total
    return result





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

# solution in Python:


def solution():
    """Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
    # Shawn has five toys
    toys_initial = 5
    # he got two toys from his mom
    mom_toys = 2
    # he got two toys from his dad
    dad_toys = 2
    # Total number of toys received is mom_toys + dad_toys 
    total_received = mom_toys + dad_toys
    # Total number of toys he has now are toys_initial + total_received 
    total_toys = toys_initial + total_received
    # Result
    result = total_toys
    return result





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Python:


def solution():
    """Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
    # Jason had 20 lollipops initially
    jason_lollipops_initial = 20
    # Number of lollipops Jason has after giving to Denny
    jason_lollipops_after = 12
    # Number of lollipops that Jason gave Denny are jason_lollipops_initial - jason_lollipops_after 
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    # Result
    result = denny_lollipops
    return result





Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

# solution in Python:


def solution():
    """Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
    # Leah had 32 chocolates
    leah_chocolates = 32
    # her sister had 42
    sister_chocolates = 42
    # Total number of chocolates they both had
    total_chocolates = leah_chocolates + sister_chocolates
    # Number of chocolates eaten by both
    chocolates_eaten = 35
    # Number of chocolates left is total_chocolates - chocolates_eaten 
    chocolates_left = total_chocolates - chocolates_eaten
    # Result
    result = chocolates_left
    return result





Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

# solution in Python:


def solution():
    """If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"""
    # There are 3 cars in the parking lot
    cars_initial = 3
    # 2 more cars arrive
    cars_arrived = 2
    # Total number of cars in the parking lot is cars_initial + cars_arrived
    total_cars = cars_initial + cars_arrived
    # Result
    result = total_cars
    return result





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

# solution in Python:


def solution():
    """There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
    # There are 15 trees in the grove
    trees_initial = 15
    # Number of trees in the grove after planting trees
    trees_after = 21
    # Number of trees planted by the grove workers is trees_after - trees_initial 
    trees_added = trees_after - trees_initial
    # Result
    result = trees_added
    return result





Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'