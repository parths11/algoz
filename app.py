import argparse
from search import breadth_first
from search import depth_first
from search import binary


def main():
    # arg parser
    parser = argparse.ArgumentParser(description="search for word in file")

    # word
    parser.add_argument(
        "-w",
        "--word",
        required=True,
        help="word to be searched for",
        )

    # file
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="path to the file to be searched",
        )

    # algorithm
    parser.add_argument(
        "-sa",
        "--search-algorithm",
        required=True,
        choices=["binary-search", "depth-first-search", "breadth-first-search"],
        help="algorithm to be used to search the word in the file",
        )
    
    # order
    parser.add_argument(
        "-o",
        "--order",
        required=True,
        choices=["pre-order", "post-order", "in-order", "level-order"],
        help="the order in which to traverse the tree",
        )

    args = parser.parse_args()

    # depth first search
    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return
    
    # breadth first search
    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return

    # binary search
    if args.search_algorithm == "binary-search":
        binary.search(args)
        return


if __name__ == "__main__":
    main()
    