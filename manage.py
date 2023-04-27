import pathlib
import runpy
from typing import List

import click

BASE_PROBLEMS_DIR = pathlib.Path(__file__).parent.resolve() / "src"
PROBLEM_DIR_NAME_PREFIX = "problem_"


def validate_number_param(ctx, param, value) -> int:
    if value != -1 and value <= 0:
        raise click.BadParameter("invalid value")
    return value


def get_problem_number_by_dir_name(dir_name: str) -> int:
    _, problem_number = dir_name.split("_")
    return int(problem_number)


def get_all_problems() -> List[int]:
    result = []
    for x in BASE_PROBLEMS_DIR.iterdir():
        if x.is_dir():
            result.append(get_problem_number_by_dir_name(x.name))
    result.sort()
    return result


def execute_problem(problem_number: int) -> None:
    try:
        print(f"=== start execute euler problem #{problem_number} ===")

        problem_dir_file = BASE_PROBLEMS_DIR / (PROBLEM_DIR_NAME_PREFIX + str(problem_number)) / "main.py"

        runpy.run_path(path_name=problem_dir_file.absolute(), run_name='__main__')
    except Exception as ex:
        print(f"ERROR execute euler problem :(  {ex}")
    else:
        print(f"=== end execute euler problem ===")


@click.command()
@click.option("--number", "-n", default=-1, help="Number of euler problem. -1 = run all euler problems",
              callback=validate_number_param)
def main(number: int) -> None:
    all_problems = get_all_problems()

    if number == -1:
        for problem_number in all_problems:
            execute_problem(problem_number)
        return

    if number != -1 and number not in all_problems:
        print("euler problem not found!")
        return

    execute_problem(number)


if __name__ == '__main__':
    main()
