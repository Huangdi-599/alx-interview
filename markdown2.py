#!/usr/bin/python3

"""
Markdown script using Python.
"""

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print('Missing {}'.format(input_file), file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r') as markdown_file:
        with open(output_file, 'w') as html_file:
            unordered_start = False
            ordered_start = False
            paragraph = False

            for line in markdown_file:
                line = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1).replace('__', '</em>', 1)

                md5_matches = re.findall(r'\[\[(.+?)\]\]', line)
                if md5_matches:
                    line = line.replace(md5_matches[0], hashlib.md5(md5_matches[0].encode()).hexdigest())

                remove_c_matches = re.findall(r'\(\((.+?)\)\)', line, flags=re.IGNORECASE)
                if remove_c_matches:
                    line = line.replace(remove_c_matches[0], remove_c_matches[0].replace('c', '').replace('C', ''))

                length = len(line)
                stripped_line = line.strip()

                if 1 <= length <= 6 and line.startswith('#'):
                    heading_num = length
                    line = f'<h{heading_num}>{stripped_line}</h{heading_num}>\n'

                unordered_num = length - len(stripped_line.lstrip('-'))
                if unordered_num:
                    if not unordered_start:
                        html_file.write('<ul>\n')
                        unordered_start = True
                    line = f'<li>{stripped_line.lstrip("-")}</li>\n'

                if unordered_start and not unordered_num:
                    html_file.write('</ul>\n')
                    unordered_start = False

                ordered_num = length - len(stripped_line.lstrip('*'))
                if ordered_num:
                    if not ordered_start:
                        html_file.write('<ol>\n')
                        ordered_start = True
                    line = f'<li>{stripped_line.lstrip("*")}</li>\n'

                if ordered_start and not ordered_num:
                    html_file.write('</ol>\n')
                    ordered_start = False

                if not (heading_num or unordered_start or ordered_start):
                    if length > 1:
                        if not paragraph:
                            html_file.write('<p>\n')
                            paragraph = True
                        else:
                            html_file.write('<br/>\n')
                    elif paragraph:
                        html_file.write('</p>\n')
                        paragraph = False

                if length > 1:
                    html_file.write(line)

            if unordered_start:
                html_file.write('</ul>\n')
            if ordered_start:
                html_file.write('</ol>\n')
            if paragraph:
                html_file.write('</p>\n')

    sys.exit(0)
