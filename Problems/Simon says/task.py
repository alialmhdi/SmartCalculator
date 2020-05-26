def what_to_do(instructions):
    if len(instructions) != 0:
        simon = 'Simon says'
        instructions_length = len(instructions)
        simon_length = len(simon)
        simon_index = instructions.find(simon)
        simon_in_end = simon_length + simon_index == instructions_length
        simon_count = instructions.count(simon)
        if simon_index == 0 and simon_count == 1:
            return f'I {instructions[simon_length + 1:]}'
        if simon_in_end and simon_count == 1:
            return f'I {instructions[:simon_length + 1]}'
        return "I won't do it!"
    return "I won't do it!"


