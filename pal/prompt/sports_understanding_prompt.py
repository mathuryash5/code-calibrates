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
```
def solution():
	player_name = "Lebron James"
	player_sport = "basketball"
	playing_action = "turnaround jumper"
	playing_sport = "basketball"
	if player_sport == playing_sport:
		return "plausible"
	else:
		return "implausible"
```

# Q: Lionel Messi hit a three-run homer. 
```
def solution():
	player_name = "Lionel Messi"
	player_sport = "soccer"
	playing_action = "three-run homer"
	playing_sport = "baseball"
	if player_sport == playing_sport:
		return "plausible"
	else:
		return "implausible"
```

# Q: Mike Trout took ball four in the World Series.
```
def solution():
	player_name = "Mike Trout"
	player_sport = "baseball"
	competition_name = "World Series"
	competition_sport = "baseball"
	if player_sport == competition_sport:
		return "plausible"
	else:
		return "implausible"
```

# Q: Tom Brady threw a touchdown in the Champions League Final.
```
def solution():
	player_name = "Tom Brady"
	player_sport = "american football"
	competition_name = "Champions League"
	competition_sport = "soccer"
	if player_sport == competition_sport:
		return "plausible"
	else:
		return "implausible"
```

# Q: {question}
'''.strip()

