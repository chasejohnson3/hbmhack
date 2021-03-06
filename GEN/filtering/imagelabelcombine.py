# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import pydra
from pydra.engine import specs
import attr


input_fields = [
    (
        "InputLabelMap_A", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Label map image",
                "position": -3
            }
        ),
    ),
    (
        "InputLabelMap_B", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Label map image",
                "position": -2
            }
        ),
    ),
    (
        "OutputLabelMap", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Resulting Label map image",
                "position": -1
            }
        ),
    ),
    (
        "first_overwrites", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--first_overwrites ",
                "help_string": "Use first or second label when both are present"
            }
        ),
    ),
]

output_fields = [
    (
        "OutputLabelMap", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "Resulting Label map image",
                "position": -1,
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

ImageLabelCombine_task = pydra.ShellCommandTask(
    name="ImageLabelCombine",
    executable=" ImageLabelCombine ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)