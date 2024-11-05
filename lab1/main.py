import re
import argparse


def parser_of_file() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Returns most count number codes",
    )
    parser.add_argument("filename", type=str, help="Path to file.")

    return parser.parse_args()


def get_codes(filename: str) -> dict:
    """
    Extracts and counts the occurrence of 3-digit area codes from phone numbers in the given file.

    Parameters:
        filename (str): The path to the file containing phone numbers.

    Returns:
        dict: A dictionary where keys are 3-digit area codes
    """
    code_counts = dict()
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    phone_numbers = re.findall(r'\+7 (\d{3}) \d{3}-\d{2}-\d{2}', data)

    for code in phone_numbers:
        if code in code_counts:
            code_counts[code] += 1
        else:
            code_counts[code] = 1
    return code_counts


def find_most_common_code(code_counts: dict) -> tuple:
    """
    Finds the most common 3-digit code

    Parameters:
        code_counts (dict): A dictionary where keys are 3-digit area codes
        and values

    Returns:
        tuple: A tuple containing the most common code and its count,
    """
    most_common_code = max(code_counts.items(), key=lambda item: item[1])
    return most_common_code


def main():
    args = parser_of_file()

    try:
        codes = get_codes(args.filename)
        max_codes = find_most_common_code(codes)
        print(f"The most common code is '{max_codes[0]}' with {max_codes[1]} occurrences.")
    except FileNotFoundError:
        print("FILE ERROR")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
