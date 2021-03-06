# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class VotingBinaryHoleFillingImageFilterInputSpec(CommandLineInputSpec):
    radius = InputMultiPath(traits.Int, argstr="--radius %s", desc="The radius of a hole to be filled", sep=",")
    majorityThreshold = traits.Int(argstr="--majorityThreshold %d", desc="The number of pixels over 50% that will decide whether an OFF pixel will become ON or not. For example, if the neighborhood of a pixel has 124 pixels (excluding itself), the 50% will be 62, and if you set a Majority threshold of 5, that means that the filter will require 67 or more neighbor pixels to be ON in order to switch the current OFF pixel to ON.")
    background = traits.Int(argstr="--background %d", desc="The value associated with the background (not object)")
    foreground = traits.Int(argstr="--foreground %d", desc="The value associated with the foreground (object)")
    inputVolume = File(argstr="%s", desc="Input volume to be filtered", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="Output filtered", position=-1, hash_files=False)


class VotingBinaryHoleFillingImageFilterOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output filtered", position=-1, exists=True)


class VotingBinaryHoleFillingImageFilter(SEMLikeCommandLine):
    """title: Voting Binary Hole Filling Image Filter

category: Filtering

description: Applies a voting operation in order to fill-in cavities. This can be used for smoothing contours and for filling holes in binary images. This technique is used frequently when segmenting complete organs that may have ducts or vasculature that may not have been included in the initial segmentation, e.g. lungs, kidneys, liver.

version: 0.1.0.$Revision$(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/VotingBinaryHoleFillingImageFilter

contributor: Bill Lorensen (GE)

acknowledgements: This command module was derived from Insight/Examples/Filtering/VotingBinaryHoleFillingImageFilter (copyright) Insight Software Consortium

"""

    input_spec = VotingBinaryHoleFillingImageFilterInputSpec
    output_spec = VotingBinaryHoleFillingImageFilterOutputSpec
    _cmd = " VotingBinaryHoleFillingImageFilter "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False
