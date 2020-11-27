#!/usr/bin/env python2
"""Apply environment variables to rsyslog config files"""

import json
import os
from jinja2 import Template


def apply_template(jinja2_file, output_file, replacements):
    """Replace the replacements values in jinja2_file, write to output_file"""
    with open(jinja2_file, "r") as j2_file:
        j2_text = j2_file.read()
    template = Template(j2_text)
    replaced_text = template.render(**replacements)
    with open(output_file, "w+") as write_file:
        write_file.write(replaced_text)


# /etc/rsyslog.conf
apply_template(
    jinja2_file="/etc/rsyslog.conf.j2",
    output_file="/etc/rsyslog.conf",
    replacements={
        "senders": os.environ["ALLOWEDSENDERS"],
    },
)

