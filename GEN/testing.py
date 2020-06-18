# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import pydra
from pydra.engine import specs
import attr


input_fields = [
    (
        "ri", 
        attr.ib(
            type=traits.List,
            metadata={
                "argstr": "--ri %s"
            }
        ),
    ),
    (
        "ro", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--ro %s..."
            }
        ),
    ),
]

output_fields = [
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))


CLIROITest_task = pydra.ShellCommandTask(
    name="CLIROITest",
    executable=" CLIROITest ", 
    input_spec=input_spec_pdr,
    
)

input_fields = [
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputVolume %s",
                "help_string": "Input image."
            }
        ),
    ),
    (
        "outputCSVFile", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputCSVFile %s",
                "help_string": "A file to write out final information report in CSV file: HA,BA,LR,MetricValue(cc)"
            }
        ),
    ),
]

output_fields = [
    (
        "outputCSVFile", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "A file to write out final information report in CSV file: HA,BA,LR,MetricValue(cc)",
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

ComputeReflectiveCorrelationMetric_task = pydra.ShellCommandTask(
    name="ComputeReflectiveCorrelationMetric",
    executable=" ComputeReflectiveCorrelationMetric ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)

input_fields = [
    (
        "inputLandmarkFiles", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--inputLandmarkFiles %s",
                "help_string": "Input landmark files names (.fcsv or .wts)."
            }
        ),
    ),
    (
        "inputLandmarkListFile", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputLandmarkListFile %s",
                "help_string": "A single file for a list of filenames one per line."
            }
        ),
    ),
    (
        "outputLandmarkFile", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputLandmarkFile %s",
                "help_string": "Ouput landmark file name that includes average values for landmarks (.fcsv or .wts)"
            }
        ),
    ),
]

output_fields = [
    (
        "outputLandmarkFile", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "Ouput landmark file name that includes average values for landmarks (.fcsv or .wts)",
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

GenerateAverageLmkFile_task = pydra.ShellCommandTask(
    name="GenerateAverageLmkFile",
    executable=" GenerateAverageLmkFile ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)

input_fields = [
    (
        "inputLandmarkFile1", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputLandmarkFile1 %s",
                "help_string": "First input landmark file (.fcsv or .wts)"
            }
        ),
    ),
    (
        "inputLandmarkFile2", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--inputLandmarkFile2 %s",
                "help_string": "Second input landmark file. This can be a vector of baseline file names (.fcsv or .wts)"
            }
        ),
    ),
    (
        "weights", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--weights %s",
                "help_string": "Weights on the tolerance to accept ( tolerance  / weights )"
            }
        ),
    ),
    (
        "tolerance", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--tolerance %f",
                "help_string": "The maximum error (in mm) allowed in each direction of a landmark"
            }
        ),
    ),
]

output_fields = [
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))


LandmarksCompare_task = pydra.ShellCommandTask(
    name="LandmarksCompare",
    executable=" LandmarksCompare ", 
    input_spec=input_spec_pdr,
    
)