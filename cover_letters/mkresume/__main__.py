#!/usr/bin/env python
# -*- mode: python; coding: utf-8 -*-

import sys
import re
import argparse
from _parts import *

ARGS = None
SIGNATURE = """Mike Burr
mburr@unintuitive.org
https://unintuitive.org/
"""
THANKS = """I believe that I am a very good candidate for this role! Please get in touch at your earliest convenience.

Thank you."""

URL_MARKDOWN_RE = r'\<\<(?P<text>.*?)\|(?P<url>.*?)\>\>'

class Exit(Exception):
    None
    
def mkurl(m):
    d = m.groupdict()
    if ARGS.format == 'text':
        return '%s [%s]' % (d['text'], d['url'])
    elif ARGS.format == 'html':
        return '<a href="%s">%s</a>' % (d['url'], d['text'])
    else:
        raise Exit('Unknown format: %s' % fmt)

def get_resume():

    context = dict(
        position='<<%s|%s>>' % (ARGS.job_title, ARGS.job_url),
        company_name=ARGS.company_name,
    )

    lines = []
    lines.append(ARGS.salutation)
    lines.append('')
    for name in ARGS.paragraphs:
        try:
            line = globals()['X_%s' % name.upper()]
        except NameError:
            raise Exit('Unknown paragraph name: %s' % name)
        line = line.format(**context)
        lines.append(line)
        lines.append('')
    lines.append(THANKS)
    lines.append('')
    lines.append(SIGNATURE)

    def foo(string):
        return re.sub(URL_MARKDOWN_RE, mkurl, string)

    lines = map(foo, lines)
    
    return '\n'.join(lines)

def get_args(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('paragraphs', nargs='*')
    parser.add_argument('--salutation', choices=['Hello!', 'Greetings!'], default='Hello!')
    parser.add_argument('--format', choices=['text', 'html'], default='html')
    parser.add_argument('--job-title', required=True)
    parser.add_argument('--job-url', required=True)
    parser.add_argument('--company-name', required=True)
    parser.add_argument('--list', default=False, action='store_true')
    return parser.parse_args(argv)

def print_paragraph_choices():
    for name, _ in globals().items():
        if name.startswith('X_'):
            print(name[2:])

if __name__ == '__main__':

    # yup. gigantic hack.
    if '--list' in sys.argv:
        print_paragraph_choices()
        sys.exit(0)
    ARGS = get_args(sys.argv)
    ARGS.paragraphs = ARGS.paragraphs[1:]
    print(get_resume())
