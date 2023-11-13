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

OBJECT_COUNTING_PROMPT = '''
Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?

# solution in Python:

def solution():
	# note: I'm not counting the chair, tables, or fridges
	vegetables_to_count = {{'potato': 2,'cauliflower': 1,'lettuce head': 1,'cabbage': 1,'onion': 2}}
	return sum(vegetables_to_count.values())



Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?

# solution in Python:

def solution():
	musical_instruments_to_count = {{'drum': 1,'flute': 1,'clarinet': 1,'violin': 1,'accordion': 4,'piano': 1,'trombone': 1,'trumpet': 1}}
	return sum(musical_instruments_to_count.values())



Q: I have a chair, two ovens, and three tables. How many objects do I have?

# solution in Python:

def solution():
	objects_to_count = {{'chair': 1,'oven': 2,'table': 3}}
	return sum(objects_to_count.values())



Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'

