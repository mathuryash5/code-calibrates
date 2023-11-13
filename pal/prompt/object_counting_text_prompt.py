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

OBJECT_COUNTING_BETA_SYSTEM_MESSAGE = "Let's think step by step to solve object counting based on a given question"

OBJECT_COUNTING_PROMPT = '''
# Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?
# A: 
Chair, tables and fridges are not vegetables, so we are not counting them.
Two potatoes, cauliflower, lettuce head, cabbage and two onions are vegetables, so they will be counted
The total number of vegetables are 2 + 1 + 1 + 1 + 2
The answer is: 7

# Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?
# A:
Drum, flute, clarinet, violin, four accordions, piano, trombone and trumpet are musical instruments, so they will be counted
The total number of musical instruments are 1 + 1 + 1 + 1 + 4 + 1 + 1 + 1
The answer is: 11

# Q: I have a chair, two ovens, and three tables. How many objects do I have?
# A:
Chair, two ovens and three tables are objects, so they will be counted
The total number of objects are 1 + 2 + 3
The answer is: 6

# Q: {question}
# A:
'''.strip()

