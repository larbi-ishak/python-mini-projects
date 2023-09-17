import argparse
from rich import print
from rich.console import Console


def get_args():
    parser = argparse.ArgumentParser(
        description='spanish article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("file",
                        help='just a word to classify it',
                        metavar='str',
                        default=".\inputs\gettysburg.txt",
                        type=str)

    parser.add_argument("-n", "--number",
                        required=False,
                        default=10,
                        help='to reverse order',)

    return parser.parse_args()


def main():
    console = Console()
    console.print("[bold yellow]:warning:[/bold yellow]\t[bold underline purple] More linux command version  Python [/bold underline purple]\t[bold yellow]:warning:[/bold yellow] ")
    args = get_args()

    with open(args.file, "r") as file:
        line_list = [line for line in file]
        n = int(args.number)
        i = 0
        choice = "n"
        while True:
            if choice == "p":
                i -= n
                try:
                    m = list(range(0, n))
                    m.reverse()
                    for d in m:
                        if i <= 0:
                            raise IndexError("")
                        print(f"{i-d}\t{line_list[i-d]}")
                except IndexError:
                    console.print(
                        "[bold green]Begin--- no previous lines[/bold green]")

            elif choice == "n":
                try:
                    for d in range(1, n+1):
                        print(f"{i+d}\t{line_list[i+d]}")
                except IndexError:
                    console.print(
                        "[bold green]End--- no next lines[/bold green]")
                i += n
            elif choice == "q" or choice == "":
                break
            else:
                console.print(
                    "[underline bold red]wrong choice[/underline bold red]")

            console.print("something from the console")
            choice = input("[n]ext , [p]rev , anything else to quit\n>")


if __name__ == "__main__":
    main()
