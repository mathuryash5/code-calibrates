REPEAT_COPY_PROMPT = '''
Q: say java twice and data once, and then repeat all of this three times.

# solution using Python:

def solution():
    """Q: say java twice and data once, and then repeat all of this three times."""
    result = []
    tmp = ["java", "java", "data"]
    for i in range(3):
        result.extend(tmp)
    return " ".join(result)



Q: ask a group of insects in what family? four times. after the fourth time say The happy family

# solution using Python:

def solution():
    """Q: ask a group of insects in what family? four times. after the fourth time say The happy family"""
    result = []
    tmp = []
    for i in range(1, 5):
        tmp.append("a group of insects in what family?")
    tmp.append("The happy family")
    result.extend(tmp)
    return " ".join(result)



Q: Repeat the word duck four times, but halfway through also say quack

# solution using Python:

def solution():
    """Q: Repeat the word duck four times, but halfway through also say quack"""
    result = []
    for i in range(1, 5):
        result.append("duck")
        if i == 2:
            result.append("quack")
    return " ".join(result)



Q: Print boolean eleven times, but after the 3rd and 8th also say correct

# solution using Python:

def solution():
    """Q: Print boolean eleven times, but after the 3rd and 8th also say correct"""
    result = []
    for i in range(1, 12):
        result.append("boolean")
        if i == 3 or i == 8:
            result.append("correct")
    return " ".join(result)



Q: {question}

# solution using Python:
'''.strip() + '\n\n'