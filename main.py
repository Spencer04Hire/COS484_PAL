import openai
import pal
from pal.prompt import algorithmic_prompt, colored_object_prompt, date_understanding_prompt, math_prompt, penguin_prompt
from pal.core.runtime import PythonRuntime, JavaRuntime

MODEL = 'gpt-4o-mini'



interface = pal.interface.ProgramChatInterface(model=MODEL,
											   get_answer_from_stdout=True,
											   verbose=False,
											   runtime=JavaRuntime(),
											   system_message='You are a helpful assistant that can only write Java code that solves mathematical reasoning questions in a manner identical to the examples that you will be provided.')

question = "say python twice and data once, and then repeat all of this three times."
prompt = algorithmic_prompt.REPEAT_COPY_PROMPTS["Java"] % (question)

answer = interface.run(prompt, time_out=10)

# Returns python python data python python data python python data
print('\n==========================')
print(f'The answer is {answer}.')
print('==========================\n')



question = "I have an apple, three bananas, a strawberry, a peach, three oranges, a plum, a raspberry, two grapes, a nectarine, and a blackberry. How many fruits do I have?"
prompt = algorithmic_prompt.OBJECT_COUNTING_PROMPTS["Java"] % (question)


answer = interface.run(prompt, time_out=10)

# Returns 15
print('\n==========================')
print(f'The answer is {answer}.')
print('==========================\n')




question = "On the nightstand, you see a mauve stress ball and a purple booklet. What color is the booklet?"
prompt = colored_object_prompt.COLOR_OBJECT_PROMPTS["Java"] % (question)

answer = interface.run(prompt, time_out=10)

# Returns purple
print('\n==========================')
print(f'The answer is {answer}.')
print('==========================\n')






question = "Yesterday was April 30, 2021. What is the date today in MM/DD/YYYY?"
prompt = date_understanding_prompt.DATE_UNDERSTANDING_PROMPTS["Java"] % (question)

answer = interface.run(prompt, time_out=10)

# Returns 05/01/2021
print('\n==========================')
print(f'The answer is {answer}.')
print('==========================\n')



question = "Mrs. Hilt met 15 friends. Nine of the friends were carrying pears. The rest were carrying oranges. How many friends were carrying oranges?"
prompt = math_prompt.math_prompt["Java"] % (question)

answer = interface.run(prompt, time_out=10)

# Should be 6
print('\n==========================')
print(f'The answer is {answer}.')
print('==========================\n')





question = "Here is a table where the first line is a header and each subsequent line is a penguin:\n\nname, age, height (cm), weight (kg)\nLouis, 7, 50, 11\nBernard, 5, 80, 13\nVincent, 9, 60, 11\nGwen, 8, 70, 15\n\nFor example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.\nWhat is the age of Bernard?"
prompt = penguin_prompt.PENGUIN_PROMPTS["Java"] % (question)

answer = interface.run(prompt, time_out=10)

# Should be 5
print('\n==========================')
print(f'The answer is {answer}.')
print('==========================\n')
    