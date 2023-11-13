MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You are a helpful agent that reasons about questions in steps.'

MATH_CHAT_BETA_PROMPT = '''
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today? (Hint: The answer is near to 6).
A:
	"""
	We know the Answer Hints: 6. 
	With the Answer Hints: 6, we will answer the question. 
	There are 15 trees originally. 
	Then there were 21 trees after the Grove workers planted some more. 
	So there must have been 21 - 15 = 6 trees that were planted. 
	The answer is 6.
	"""


Q: : If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot? (Hint: The answer is near to 10, 8).
A:
	"""
	We know the Answer Hints: 10, 8. 
	With the Answer Hints: 10, 8, we will answer the question.
	There are originally 3 cars. Then 2 more cars arrive. 
	Now 3 + 2 = 5 cars are in the parking lot. 
	The answer is 5.
	"""
	
	
Q: : Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total? (Hint: The answer is near to 30, 35).
A:
	"""
	We know the Answer Hints: 30, 35. 
	With the Answer Hints: 30, 35, we will answer the question.
	Originally, Leah had 32 chocolates and her sister had 42. 
	So in total they had 32 + 42 = 74. 
	After eating 35, they had 74 - 35 = 39 pieces left in total. 
	The answer is 39.
	"""
	

Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny? (Hint: The answer near to 8, 12).
A:
	"""
	We know the Answer Hints: 8, 12. 
	With the Answer Hints: 8, 12, we will answer the question.
	Jason had 20 lollipops originally. 
	Then he had 12 after giving some to Denny. 
	So he gave Denny 20 - 12 = 8 lollipops. 
	The answer is 8.
	"""


Q: : Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now? (Hint: The answer is near to 9, 5).
A:
	"""
	We know the Answer Hints: 9, 5.
	With the Answer Hints: 9, 5, we will answer the question.
	Shawn started with 5 toys.
	He then got 2 toys each from his mom and dad. 
	So he got 2 * 2 = 4 more toys.
	Now he has 5 + 4 = 9 toys.
	The answer is 9.
	"""
	
	
Q:  There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room? (Hint: The answer is near to 20).
A:
	"""
	We know the Answer Hints: 20. 
	With the Answer Hints: 20, we will answer the question. 
	There were originally 9 computers.
	For each day from monday to thursday, 5 more computers were installed.
	So 4 * 5 = 20 computers were added. 
	Now 9 + 20 = 29 computers are now in the server room. 
	The answer is 29
	"""
	
	
Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday? (Hint: The answer is near to 45).
A:
	"""
	We know the Answer Hints: 45. 
	With the Answer Hints: 45, we will answer the question. 
	Michael started with 58 golf balls.
	He lost 23 on Tuesday, and lost 2 more on wednesday. 
	So he had 58 - 23 = 35 at the end of Tuesday, and 35 - 2 = 33 at the end of wednesday. 
	The answer is 33.
	"""
	
	
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left? (Hint: The answer is near to 8).
A:
	"""
	We know the Answer Hints: 8.
	With the Answer Hints: 8, we will answer the question. 
	Olivia had 	23 dollars.
	She bought 5 bagels for 3 dollars each. 
	So she spent 5 * 3 = 15 dollars.
	Now she has 23 - 15 = 8 dollars left.
	The answer is 8.
	"""
	

Q: {question}
A:
'''.strip()

"""
Step 1: Feed in the question using CoT.
Step 2: 1 answer from Step 1. Choose majority
Step 3: Use PHP with hint from Step 2
Step 4: 10 answers from Step 3. Choose majority. If answer is different goto Step 3 else break"""
