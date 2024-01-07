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

import os
import time

import openai
from langchain import OpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

openai.api_key = os.getenv('OPENAI_API_KEY')
if openai.api_key == "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":
    openai.organization = 'org-4vFClSRiVOtShsEcrhyX9NMM'


# GPT-3 API
def chat_api(model, max_tokens, stop, prompt, temperature,
            top_p, n, best_of):
    ans = openai.ChatCompletion.create(
        model=model,
        max_tokens=max_tokens,
        stop=stop,
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant that can write Python code that solves mathematical reasoning questions similarly to the examples that you will be provided.'},
            {'role': 'user', 'content': prompt}],
        temperature=temperature,
        top_p=top_p,
        n=n)
    return [choice['message']['content'] for choice in ans['choices']]


def call_gpt(prompt, model='code-davinci-002', stop=None, temperature=0., top_p=1.0,
        max_tokens=128, majority_at=None):
    num_completions = majority_at if majority_at is not None else 1
    num_completions_batch_size = 5

    completions = []
    for i in range(20 * (num_completions // num_completions_batch_size + 1)):
        try:
            requested_completions = min(num_completions_batch_size, num_completions - len(completions))
            ans = openai.Completion.create(
                            model=model,
                            max_tokens=max_tokens,
                            stop=stop,
                            prompt=prompt,
                            temperature=temperature,
                            top_p=top_p,
                            n=requested_completions,
                            best_of=requested_completions)
            completions.extend([choice['text'] for choice in ans['choices']])
            if len(completions) >= num_completions:
                return completions[:num_completions]
        except openai.error.OpenAIError as allErrors:
            print(allErrors)
            time.sleep(min(i**2, 60))
    raise RuntimeError('Failed to call GPT API')


def call_text_gpt(model, examples, question, stop=None, temperature=0., top_p=1.0,
        max_tokens=128, majority_at=None):

    completions = []
    example_prompt = PromptTemplate(input_variables=["question", "answer"], template="Q: {question}\nA: {answer}")
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        suffix="Q: {input}\nA: ",
        input_variables=["input"]
    )
    num_completions = majority_at if majority_at is not None else 1
    num_completions_batch_size = 5
    while True:
        try:
            requested_completions = min(num_completions_batch_size, num_completions - len(completions))
            llm = OpenAI(model_name='text-davinci-003', temperature=temperature, max_tokens=max_tokens, top_p=top_p,
                         n=requested_completions, best_of=requested_completions)
            result = llm.generate([prompt.format(input=question)])
            generation = result.generations[0]
            for res in generation:
                completions.append(res.text)
            # print(len(completions))
            if len(completions) >= num_completions:
                return completions[:num_completions]
        except openai.error.RateLimitError as e:
            print("Hitting rate limit errors, waiting for : {} seconds before retrying".format(wait))
            time.sleep(min(wait, 60))
            wait *= 2
        except Exception as e:
            print('An exception occurred: {}'.format(e))
            raise RuntimeError('Failed to call {model} api')


def call_chat_gpt(messages, model='gpt-3.5-turbo', stop=None, temperature=0., top_p=1.0, max_tokens=128, majority_at=None):
    wait = 1
    num_completions = majority_at if majority_at is not None else 1
    num_completions_batch_size = 5
    completions = []
    while True:
        try:
            requested_completions = min(num_completions_batch_size, num_completions - len(completions))
            ans = openai.ChatCompletion.create(
                model=model,
                max_tokens=max_tokens,
                stop=stop,
                messages=messages,
                temperature=temperature,
                top_p=top_p,
                n=requested_completions
            )
            completions.extend([choice['message']['content'] for choice in ans['choices']])
            if len(completions) >= num_completions:
                return completions[:num_completions]
            # return ans.choices[0]['message']['content']
        except openai.error.RateLimitError as e:
            print("Hitting rate limit errors, waiting for : {} seconds before retrying".format(wait))
            time.sleep(min(wait, 60))
            wait *= 2
    raise RuntimeError('Failed to call chat gpt')


