# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import pydra
from pydra.engine import specs
import attr


input_fields = [
    (
        "imageVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--imageVolume %s",
                "help_string": "Image Volume"
            }
        ),
    ),
    (
        "labelVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--labelVolume %s",
                "help_string": "Label Volume"
            }
        ),
    ),
    (
        "labelNameFile", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--labelNameFile %s",
                "help_string": "Label Name File"
            }
        ),
    ),
    (
        "outputPrefixColumnNames", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--outputPrefixColumnNames %s",
                "help_string": "Prefix Column Name(s)"
            }
        ),
    ),
    (
        "outputPrefixColumnValues", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--outputPrefixColumnValues %s",
                "help_string": "Prefix Column Value(s)"
            }
        ),
    ),
    (
        "labelFileType", 
        attr.ib(
            type=traits.Enum,
            metadata={
                "argstr": "--labelFileType %s",
                "help_string": "Label File Type"
            }
        ),
    ),
    (
        "numberOfHistogramBins", 
        attr.ib(
            type=traits.Int,
            metadata={
                "argstr": "--numberOfHistogramBins %d",
                "help_string": "Number Of Histogram Bins"
            }
        ),
    ),
    (
        "minMaxType", 
        attr.ib(
            type=traits.Enum,
            metadata={
                "argstr": "--minMaxType %s",
                "help_string": "Define minimim and maximum values based upon the image, label, or via command line"
            }
        ),
    ),
    (
        "userDefineMinimum", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--userDefineMinimum %f",
                "help_string": "User define minimum value"
            }
        ),
    ),
    (
        "userDefineMaximum", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--userDefineMaximum %f",
                "help_string": "User define maximum value"
            }
        ),
    ),
]

output_fields = [
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))


BRAINSLabelStats_task = pydra.ShellCommandTask(
    name="BRAINSLabelStats",
    executable=" BRAINSLabelStats ", 
    input_spec=input_spec_pdr,
    
)

input_fields = [
    (
        "petDICOMPath", 
        attr.ib(
            type=Directory,
            metadata={
                "argstr": "--petDICOMPath %s",
                "help_string": "Input path to a directory containing a PET volume containing DICOM header information for SUV computation"
            }
        ),
    ),
    (
        "petVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--petVolume %s",
                "help_string": "Input PET volume for SUVbw computation (must be the same volume as pointed to by the DICOM path!)."
            }
        ),
    ),
    (
        "labelMap", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--labelMap %s",
                "help_string": "Input label volume containing the volumes of interest"
            }
        ),
    ),
    (
        "color", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--color %s",
                "help_string": "Color table to to map labels to colors and names"
            }
        ),
    ),
    (
        "csvFile", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "--csvFile %s",
                "help_string": "A table holding the output SUV values in comma separated lines, one per label. Optional."
            }
        ),
    ),
    (
        "OutputLabel", 
        attr.ib(
            type=traits.Str,
            metadata={
                "argstr": "--OutputLabel %s",
                "help_string": "List of labels for which SUV values were computed"
            }
        ),
    ),
    (
        "OutputLabelValue", 
        attr.ib(
            type=traits.Str,
            metadata={
                "argstr": "--OutputLabelValue %s",
                "help_string": "List of label values for which SUV values were computed"
            }
        ),
    ),
    (
        "SUVMax", 
        attr.ib(
            type=traits.Str,
            metadata={
                "argstr": "--SUVMax %s",
                "help_string": "SUV max for each label"
            }
        ),
    ),
    (
        "SUVMean", 
        attr.ib(
            type=traits.Str,
            metadata={
                "argstr": "--SUVMean %s",
                "help_string": "SUV mean for each label"
            }
        ),
    ),
    (
        "SUVMin", 
        attr.ib(
            type=traits.Str,
            metadata={
                "argstr": "--SUVMin %s",
                "help_string": "SUV minimum for each label"
            }
        ),
    ),
]

output_fields = [
    (
        "csvFile", 
        attr.ib(
            type=File,
            metadata={
                "help_string": "A table holding the output SUV values in comma separated lines, one per label. Optional.",
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

PETStandardUptakeValueComputation_task = pydra.ShellCommandTask(
    name="PETStandardUptakeValueComputation",
    executable=" PETStandardUptakeValueComputation ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)