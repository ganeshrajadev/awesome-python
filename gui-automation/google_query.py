__author__ = "rohitbabugaddeti"

import sys
import webbrowser

# output to print for --help option
help_output = f"""Usage: python {sys.argv[0]} --keyword="<string>" [--category=<supported_cats>]

required arguments:
    --keyword               your search keyword

optional arguments:
    --category              the category you want to search in. ex: images, news etc.
                            defaults to 'all' category.

supported categories:
    --supported-cats        'python {sys.argv[0]} --supported-cats' lets you check for the supported categories

"""

args_required = 1
# output to print for number of arguments mismatch error
args_no_error = f"""requires at least {args_required} args, passed {len(sys.argv) - 1}

please run 

python {sys.argv[0]} --help 

for more info on usage

"""

# output to print for invalid argument error
arg_error = f"""Invalid argument '<arg>' passed

please run 

python {sys.argv[0]} --help 

for more info on usage

"""

# available operations
opts_dict = {
    "news": "nws",
    "images": "isch",
    "videos": "vid",
    "shopping": "shop",
    "books": "bks",
}

# base search url
base_url = "https://www.google.com/search?q="

if __name__ == "__main__":
    args = sys.argv.copy()
    # variable to track invalid argument error
    flag = 0

    # check for number of arguments mismatch
    if len(args) < args_required + 1:
        print(args_no_error)
        sys.exit()

    arg1 = args.pop(1)

    if arg1 == "--help":
        print(help_output)
        flag = 1
        sys.exit()

    if arg1 == "--supported-cats":
        print(opts_dict.keys())
        flag = 1
        sys.exit()

    if arg1.startswith("--keyword="):
        key_word = arg1.replace("--keyword=", "")
        if len(args) > 1 and args[1].startswith("--category="):
            search_category = args.pop(1).replace("--category=", "")
            if search_category not in opts_dict.keys():
                print(
                    f"Unsupported/Invalid search category {search_category}. Use --supported-cats or --help to know more"
                )
                flag = 1
                sys.exit()

            webbrowser.open(f"{base_url}{key_word}&tbm={opts_dict[search_category]}")
            flag = 1
            sys.exit()

        webbrowser.open(f"{base_url}{key_word}")
        flag = 1
        sys.exit()

    if not flag:
        print(arg_error.replace("<arg>", arg1))
