# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import pydra
from pydra.engine import specs
import attr


input_fields = [
    (
        "AC", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--AC %s",
                "help_string": "Location of AC Point "
            }
        ),
    ),
    (
        "ACisIndex", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--ACisIndex ",
                "help_string": "AC Point is Index"
            }
        ),
    ),
    (
        "PC", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--PC %s",
                "help_string": "Location of PC Point "
            }
        ),
    ),
    (
        "PCisIndex", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--PCisIndex ",
                "help_string": "PC Point is Index"
            }
        ),
    ),
    (
        "SLA", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--SLA %s",
                "help_string": "Location of SLA Point "
            }
        ),
    ),
    (
        "SLAisIndex", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--SLAisIndex ",
                "help_string": "SLA Point is Index"
            }
        ),
    ),
    (
        "IRP", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--IRP %s",
                "help_string": "Location of IRP Point "
            }
        ),
    ),
    (
        "IRPisIndex", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--IRPisIndex ",
                "help_string": "IRP Point is Index"
            }
        ),
    ),
    (
        "inputLandmarksFile", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputLandmarksFile %s",
                "help_string": "input landmarks file: *.fcsv"
            }
        ),
    ),
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputVolume %s",
                "help_string": "Input image used to define physical space of images"
            }
        ),
    ),
    (
        "outputBox", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputBox %s",
                "help_string": "Name of the resulting Talairach Bounding Box file"
            }
        ),
    ),
    (
        "outputGrid", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputGrid %s",
                "help_string": "Name of the resulting Talairach Grid file"
            }
        ),
    ),
]

output_fields = [
    (
        "outputBox", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "Name of the resulting Talairach Bounding Box file",
                "exists": True
            }
        ),
    ),
    (
        "outputGrid", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "Name of the resulting Talairach Grid file",
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

BRAINSTalairach_task = pydra.ShellCommandTask(
    name="BRAINSTalairach",
    executable=" BRAINSTalairach ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)

input_fields = [
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputVolume %s",
                "help_string": "Input image used to define physical space of resulting mask"
            }
        ),
    ),
    (
        "talairachParameters", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--talairachParameters %s",
                "help_string": "Name of the Talairach parameter file."
            }
        ),
    ),
    (
        "talairachBox", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--talairachBox %s",
                "help_string": "Name of the Talairach box file."
            }
        ),
    ),
    (
        "hemisphereMode", 
        attr.ib(
            type=traits.Enum,
            metadata={
                "argstr": "--hemisphereMode %s",
                "help_string": "Mode for box creation: left, right, both"
            }
        ),
    ),
    (
        "expand", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--expand ",
                "help_string": "Expand exterior box to include surface CSF"
            }
        ),
    ),
    (
        "outputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputVolume %s",
                "help_string": "Output filename for the resulting binary image"
            }
        ),
    ),
]

output_fields = [
    (
        "outputVolume", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "Output filename for the resulting binary image",
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

BRAINSTalairachMask_task = pydra.ShellCommandTask(
    name="BRAINSTalairachMask",
    executable=" BRAINSTalairachMask ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)