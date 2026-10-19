import sys
from checks import run_all
from report import render


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    results = run_all(path)
    print(render(results))


if __name__ == "__main__":
    main()
    #just make 
