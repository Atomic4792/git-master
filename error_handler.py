def int_prompt_validator(prompt: str, condition=None) -> int:
    print(condition)
    while True:
        raw_input = input(prompt)
        try:
            user_input = int(raw_input)
        except ValueError:
            print(f"{raw_input} is not a number")
            continue

        if condition is None or user_input in condition:
            return user_input
        else:
            print(f"{user_input} is not a valid input")