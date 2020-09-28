#! usr/bin/env python3
# lucky.py - Opens several Google search results.
# py.exe lucky.py <search> - Open 5 top results of search.
# py.exe lucky.py <search> [-n <number>] - Open 'n' top results of search.
# py.exe lucky.py <search> [-l <language>] - Open "n" top results  in language

import webbrowser
from googlesearch import search
import sys
from get import get

p_args = ['-n', '-l']
args = sys.argv[1:]
num = 5
language = 'pt-br'


if args:
    if len(args) == 1 and args[0] == '--help':
        print('py.exe lucky.py <search> - Open 5 top results of search.')
        print('py.exe lucky.py <search> [-n <number>] - Open "n" top results of search.')
        print('py.exe lucky.py <search> [-l <language>] - Open "n" top results  in language')
    else:
        try:
            for p_arg in p_args:
                p_arg_index = get(args, p_arg)
                if p_arg_index is not None:
                    value = args.pop(p_arg_index + 1)
                    args.pop(p_arg_index)
                    if p_arg == '-n':
                        num = value
                    elif p_arg == '-l':
                        language = value

            if args:
                # ' '.join(args), stop=num, lang=language, country=
                for url in search(' '.join(args), stop=num, lang=language):
                    webbrowser.open(url)
            else:
                raise ValueError
        except (IndexError, ValueError, TypeError):
            print('Invalid command, try py.exe lucky.py --help')
else:
    print('Invalid command, try py.exe lucky.py --help')
