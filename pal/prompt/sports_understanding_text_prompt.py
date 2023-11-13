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

SPORTS_UNDERSTANDING_BETA_SYSTEM_MESSAGE = 'You are a helpful agent who can help determine if a sports statement is plausible or implausible'

SPORTS_UNDERSTANDING_PROMPT = '''
# Q: Lebron James hit the turnaround jumper.
# A:
Lebron James plays basketball i.e the player sport.
Turnaround jumper is an action in basketball i.e the playing sport.
Since the player sport and the playing sport is the same.
The answer is: plausible

# Q: Lionel Messi hit a three-run homer. 
# A:
Lionel Messi plays soccer i.e the player sport.
Three-run homer is an action in baseball i.e the playing sport.
Since the player sport and the playing sport is different.
The answer is: implausible

# Q: Mike Trout took ball four in the World Series.
# A:
Mike Trout plays baseball i.e the player sport.
World Series is a competition in baseball i.e the playing sport.
Since the player sport and the playing sport is the same.
The answer is: plausible

# Q: Tom Brady threw a touchdown in the Champions League Final.
# A:
Tom Brady plays american football i.e the player sport.
Champions League is a competition in soccer i.e the playing sport.
Since the player sport and the playing sport is different.
The answer is: implausible

# Q: {question}
# A:
'''.strip()

