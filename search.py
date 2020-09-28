#! usr/bin/env python3
# search.py - Open a Google search.
# py.exe search.py <search> - Open results in global.
# py.exe search.py <search> [-l <language>] - Get results in desired language.
# py.exe search.py <search> [-i <language>] - Get Google interface in desired language.
# py.exe search.py <search> [-li|-il <language>] - Get results and Google interface in desired lang.

import webbrowser
import sys
from get import get

p_args = ['-l', '-i', '-li', '-il']
args = sys.argv[1:]
interface = language = 'pt-br'

if args:
    if len(args) == 1 and args[0] == '--help':
        print('search.py - Open a google search.')
        print('py.exe search.py <search> - Open results in global.')
        print('py.exe search.py <search> [-l <language>] - Get results in desired language.')
        print(
            'py.exe search.py <search> [-i <language>] - Get Google interface in desired language.')
        print(
            'py.exe search.py <search> [-li|-il <language>] - Get results and Google interface in desired lang.')
    else:
        try:
            for p_arg in p_args:
                p_arg_index = get(args, p_arg)
                if p_arg_index is not None:
                    value = args.pop(p_arg_index + 1)
                    args.pop(p_arg_index)
                    if p_arg == '-l':
                        language = value
                    elif p_arg == '-i':
                        interface = value
                    elif p_arg in ['-li', '-il']:
                        interface = language = value

            webbrowser.open(
                f'https://google.com/search?q={" ".join(args)}&hl={interface}&lr=lang_{language}')
        except IndexError:
            print('Invalid language for search.')
else:
    print('Invalid command, try py.exe search.py --help')
