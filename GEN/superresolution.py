# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import pydra
from pydra.engine import specs
import attr


input_fields = [
    (
        "inputMRVolumes", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--inputMRVolumes %s...",
                "help_string": "Input image files names"
            }
        ),
    ),
    (
        "inputMask", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--inputMask %s",
                "help_string": "Input mask file name. If set, image histogram percentiles will be calculated within the mask"
            }
        ),
    ),
    (
        "outputMaximumGradientImage", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputMaximumGradientImage %s",
                "help_string": "output gradient image file name"
            }
        ),
    ),
    (
        "outputEdgeMap", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--outputEdgeMap %s",
                "help_string": "output edgemap file name"
            }
        ),
    ),
    (
        "lowerPercentileMatching", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--lowerPercentileMatching %f",
                "help_string": "Map lower quantile and below to minOutputRange. It should be a value between zero and one."
            }
        ),
    ),
    (
        "upperPercentileMatching", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--upperPercentileMatching %f",
                "help_string": "Map upper quantile and above to maxOutputRange. It should be a value between zero and one."
            }
        ),
    ),
    (
        "minimumOutputRange", 
        attr.ib(
            type=traits.Int,
            metadata={
                "argstr": "--minimumOutputRange %d",
                "help_string": "Map lower quantile and below to minimum output range. It should be an epsilon number greater than zero. Default is 1."
            }
        ),
    ),
    (
        "maximumOutputRange", 
        attr.ib(
            type=traits.Int,
            metadata={
                "argstr": "--maximumOutputRange %d",
                "help_string": "Map upper quantile and above to maximum output range. Default is 255 that is the maximum range of unsigned char."
            }
        ),
    ),
    (
        "numberOfThreads", 
        attr.ib(
            type=traits.Int,
            metadata={
                "argstr": "--numberOfThreads %d",
                "help_string": "Explicitly specify the maximum number of threads to use."
            }
        ),
    ),
]

output_fields = [
    (
        "outputMaximumGradientImage", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "output gradient image file name",
                "exists": True
            }
        ),
    ),
    (
        "outputEdgeMap", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "output edgemap file name",
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

GenerateEdgeMapImage_task = pydra.ShellCommandTask(
    name="GenerateEdgeMapImage",
    executable=" GenerateEdgeMapImage ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)