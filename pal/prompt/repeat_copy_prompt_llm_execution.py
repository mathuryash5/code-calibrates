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

REPEAT_COPY_BETA_SYSTEM_MESSAGE = 'You will write python program to repeat phrases as specified. You will only write code blocks.'

REPEAT_COPY_PROMPT = '''
# Q: Repeat the word duck four times, but halfway through also say quack
```
def solution():
	result = []
	for i in range(1, 5):
		result.append("duck")
		if i == 2:
			result.append("quack")
	return " ".join(result)
res = solution()
print("The answer is ", res)
```
The answer is duck duck quack duck duck

# Q: Print boolean eleven times, but after the 3rd and 8th also say correct
```
def solution():
	result = []
	for i in range(1, 12):
		result.append("boolean")
		if i == 3 or i == 8:
			result.append("correct")
	return " ".join(result)
res = solution()
print("The answer is ", res)
```
The answer is boolean boolean boolean correct boolean boolean boolean boolean boolean correct boolean boolean boolean
	
# Q: say java twice and data once, and then repeat all of this three times.
```
def solution():
	result = []
	tmp = ["java", "java", "data"]
	for i in range(3):
		result.extend(tmp)
	return " ".join(result)
res = solution()
print("The answer is ", res)
```
The answer is java java data java java data java java data

# Q: ask a group of insects in what family? four times. after the fourth time say The happy family
```
def solution():
	result = []
	tmp = []
	for i in range(1, 5):
		tmp.append("a group of insects in what family?")
	tmp.append("The happy family")
	result.extend(tmp)
	return " ".join(result)
res = solution()
print("The answer is ", res)
```
The answer is ask a group of insects in what family? ask a group of insects in what family? ask a group of insects in what family? ask a group of insects in what family? The happy family

# Q: {question}
'''.strip()

