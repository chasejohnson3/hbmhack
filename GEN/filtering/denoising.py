# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

import pydra
from pydra.engine import specs
import attr


input_fields = [
    (
        "conductance", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--conductance %f",
                "help_string": "Conductance controls the sensitivity of the conductance term. As a general rule, the lower the value, the more strongly the filter preserves edges. A high value will cause diffusion (smoothing) across edges. Note that the number of iterations controls how much smoothing is done within regions bounded by edges."
            }
        ),
    ),
    (
        "iterations", 
        attr.ib(
            type=traits.Int,
            metadata={
                "argstr": "--iterations %d",
                "help_string": "The more iterations, the more smoothing. Each iteration takes the same amount of time. If it takes 10 seconds for one iteration, then it will take 100 seconds for 10 iterations. Note that the conductance controls how much each iteration smooths across edges."
            }
        ),
    ),
    (
        "timeStep", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--timeStep %f",
                "help_string": "The time step depends on the dimensionality of the image. In Slicer the images are 3D and the default (.0625) time step will provide a stable solution."
            }
        ),
    ),
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Input volume to be filtered",
                "position": -2
            }
        ),
    ),
    (
        "outputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Output filtered",
                "position": -1
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
                "help_string": "Output filtered",
                "position": -1,
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

CurvatureAnisotropicDiffusion_task = pydra.ShellCommandTask(
    name="CurvatureAnisotropicDiffusion",
    executable=" CurvatureAnisotropicDiffusion ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)

input_fields = [
    (
        "sigma", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--sigma %f",
                "help_string": "Sigma value in physical units (e.g., mm) of the Gaussian kernel"
            }
        ),
    ),
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Input volume",
                "position": -2
            }
        ),
    ),
    (
        "outputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Blurred Volume",
                "position": -1
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
                "help_string": "Blurred Volume",
                "position": -1,
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

GaussianBlurImageFilter_task = pydra.ShellCommandTask(
    name="GaussianBlurImageFilter",
    executable=" GaussianBlurImageFilter ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)

input_fields = [
    (
        "conductance", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--conductance %f",
                "help_string": "Conductance controls the sensitivity of the conductance term. As a general rule, the lower the value, the more strongly the filter preserves edges. A high value will cause diffusion (smoothing) across edges. Note that the number of iterations controls how much smoothing is done within regions bounded by edges."
            }
        ),
    ),
    (
        "iterations", 
        attr.ib(
            type=traits.Int,
            metadata={
                "argstr": "--iterations %d",
                "help_string": "The more iterations, the more smoothing. Each iteration takes the same amount of time. If it takes 10 seconds for one iteration, then it will take 100 seconds for 10 iterations. Note that the conductance controls how much each iteration smooths across edges."
            }
        ),
    ),
    (
        "timeStep", 
        attr.ib(
            type=traits.Float,
            metadata={
                "argstr": "--timeStep %f",
                "help_string": "The time step depends on the dimensionality of the image. In Slicer the images are 3D and the default (.0625) time step will provide a stable solution."
            }
        ),
    ),
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Input volume to be filtered",
                "position": -2
            }
        ),
    ),
    (
        "outputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Output filtered",
                "position": -1
            }
        ),
    ),
    (
        "useImageSpacing", 
        attr.ib(
            type=traits.Bool,
            metadata={
                "argstr": "--useImageSpacing ",
                "help_string": "![CDATA[Take into account image spacing in the computation.  It is advisable to turn this option on, especially when the pixel size is different in different dimensions. However, to produce results consistent with Slicer4.2 and earlier, this option should be turned off.]]"
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
                "help_string": "Output filtered",
                "position": -1,
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

GradientAnisotropicDiffusion_task = pydra.ShellCommandTask(
    name="GradientAnisotropicDiffusion",
    executable=" GradientAnisotropicDiffusion ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)

input_fields = [
    (
        "neighborhood", 
        attr.ib(
            type=InputMultiPath,
            metadata={
                "argstr": "--neighborhood %s",
                "help_string": "The size of the neighborhood in each dimension"
            }
        ),
    ),
    (
        "inputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Input volume to be filtered",
                "position": -2
            }
        ),
    ),
    (
        "outputVolume", 
        attr.ib(
            type=File,
            metadata={
                "argstr": "%s",
                "help_string": "Output filtered",
                "position": -1
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
                "help_string": "Output filtered",
                "position": -1,
                "exists": True
            }
        ),
    ),
]

input_spec_pdr = specs.SpecInfo(name="Input", fields=input_fields, bases=(specs.ShellSpec,))
output_spec_pdr = specs.SpecInfo(name="Output", fields=output_fields, bases=(specs.ShellSpec,))

MedianImageFilter_task = pydra.ShellCommandTask(
    name="MedianImageFilter",
    executable=" MedianImageFilter ", 
    input_spec=input_spec_pdr,
    output_spec=output_spec_pdr
)