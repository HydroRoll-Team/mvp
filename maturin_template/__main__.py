import subprocess
import sys

def run_cli(*args):
    result = subprocess.run(
        ["maturin_template", *args],
        capture_output=True,
        text=True
    )
    return result.stdout

def main():
    args = sys.argv[1:]
    print(run_cli(*args))
    return 0

if __name__ == "__main__":
    sys.exit(main())