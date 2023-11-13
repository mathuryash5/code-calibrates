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

REPEAT_COPY_BETA_SYSTEM_MESSAGE = 'You are a helpful agent who can help repeat words based on what is asked to you.'

REPEAT_COPY_PROMPT = '''
# Q: Repeat the word duck four times, but halfway through also say quack
# A:
On repeating the word duck four times we get: duck duck duck duck
Halfway through if we say quack, we have to say quack in between the 2nd word and the 3rd word
The answer is: duck duck quack duck duck

# Q: Print boolean eleven times, but after the 3rd and 8th also say correct
# A:
On repeating the word boolean eleven times we get: boolean boolean boolean boolean boolean boolean boolean boolean boolean boolean boolean
We have to also say the correct after the 3rd and 8th time.
The answer is: boolean boolean boolean correct boolean boolean boolean boolean boolean correct boolean boolean boolean

# Q: say java twice and data once, and then repeat all of this three times.
# A:
On repeating the word java twice we get: java java
If we say the word data once we get: java java data
We have to repeat the entire phrase three times.
The answer is: java java data java java data java java data

# Q: ask a group of insects in what family? four times. after the fourth time say The happy family
# A:
On repeating the words ask a group of insects in what family? four times we get: ask a group of insects in what family? ask a group of insects in what family? ask a group of insects in what family? ask a group of insects in what family?
We have to say the words The happy family after the fourth time
The answer is: ask a group of insects in what family? ask a group of insects in what family? ask a group of insects in what family? ask a group of insects in what family? The happy family

# Q: {question}
# A:
'''.strip()

