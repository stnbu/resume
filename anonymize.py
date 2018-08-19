#!/usr/bin/env python

styles = {
    'red_dot_under': 'border-bottom: 1px #DB7093 dashed;',
    None: None,
}

dictionary = [

    # My stuff
    ('mburr', 'bapp', None),
    ('Mike', 'Bob', None),
    ('Burr', 'Applicant', None),
    ('unintuitive.org', 'me.example.com', None),
    ('stnbu', 'ghnick', None),

    # Every Town -> Springfield
    ('Milpitas', 'Springfield', 'red_dot_under'),
    ('Winston-Salem', 'Springfield', 'red_dot_under'),
    ('Palo Alto', 'Springfield', 'red_dot_under'),
    ('San Jose', 'Springfield', 'red_dot_under'),
    ('Gainesville', 'Springfield', 'red_dot_under'),

    # States that have a "Springfield"
    ('North Carolina', 'Massachusetts', 'red_dot_under'),
    ('Florida', 'Illinois', 'red_dot_under'),
    ('California', 'Missouri', 'red_dot_under'),

    # minor noise
    ('1996', '1997', 'red_dot_under'),

    # Company name mappings
    ('Betco', 'Company One', 'red_dot_under'),
    ('PointDx', 'Company Two', 'red_dot_under'),
    ('Greatwall Systems', 'Company Three', 'red_dot_under'),
    ('Triad Semiconductor', 'Company Four', 'red_dot_under'),
    ('Cisco Systems', 'Company Five', 'red_dot_under'),
    ('Cisco', 'Company Five', 'red_dot_under'),  # and therefore order matters...
    ('VMware', 'Company Six', 'red_dot_under'),
    ('GE Healthcare Worldwide', 'Gigantic Company', 'red_dot_under'),
    ('Mentor Graphics', 'Expensive Software Company', 'red_dot_under'),

    # UF gets renamed via "Florida". We rename this one too.
    ('Wake Forest', 'Fancy Private', 'red_dot_under'),

    # Propriatary tools
    ('Qali', 'SmartTool', 'red_dot_under'),
    ('Goat', 'A-Tool', 'red_dot_under'),
    ('UCS', 'TLA3', 'red_dot_under'),
]

# not super efficient. yep.
with open('resume.html', 'r') as f:
    for line in f:
        for old, new, style in dictionary:
            if style is not None:
                new = '<span style="{}">{}</span>'.format(styles[style], new)
            line = line.replace(old, new)
        print(line, end='')
        
