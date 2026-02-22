from model import get_data
from view import print_table
from error_handler import int_prompt_validator
from random import sample
from typing import List, Dict

def randomize_rows(num_rows: int, table: list) -> List[Dict]:
    random_row_nums = sample(range(0,len(table) -1), num_rows)
    randized_table = []
    for ran_row_num in random_row_nums:
        randized_table.append(table[ran_row_num -1])
    return randized_table


def main_loop() -> None:
    while True:
        record_num_condition = [i for i in range(1, len(get_data))]
        record_num = int_prompt_validator("How many rows would you like to see?: ",condition=record_num_condition)
        print(print_table(randomize_rows(record_num, get_data)))
        return
        