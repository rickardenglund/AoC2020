import requests
import os
import argparse


def main():
    parser = argparse.ArgumentParser("get puzzle input")
    parser.add_argument("day", help="the day to download the input for", type=int)
    parser.add_argument("output_file", help="file to output the input", type=argparse.FileType('w'))
    args = parser.parse_args()

    session_id = ""
    try:
        f = open(os.path.join(os.getenv("HOME"), '.aoc/session_id'))
        session_id = f.read().strip()
    except IOError:
        print('You are not logged in')
        exit(-1)
    finally:
        f.close()

    r = requests.get(f"https://adventofcode.com/2020/day/{args.day}/input", headers={"Cookie": "session=" + session_id})
    if r.status_code != 200:
        print('failed to get puzzle', r.status_code, r.text)
        exit(-1)

    content = f"input = '''{r.text.strip()}'''\n\ntest_input = '''<test_input>'''\n"

    args.output_file.write(content)
    args.output_file.close()


if __name__ == '__main__':
    main()
