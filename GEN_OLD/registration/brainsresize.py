# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class BRAINSResizeInputSpec(CommandLineInputSpec):
    inputVolume = File(argstr="--inputVolume %s", desc="Image To Scale", exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="--outputVolume %s", desc="Resulting scaled image", hash_files=False)
    pixelType = traits.Enum("float", "short", "ushort", "int", "uint", "uchar", "binary", argstr="--pixelType %s", desc="Specifies the pixel type for the input/output images.  The \'binary\' pixel type uses a modified algorithm whereby the image is read in as unsigned char, a signed distance map is created, signed distance map is resampled, and then a thresholded image of type unsigned char is written to disk.")
    scaleFactor = traits.Float(argstr="--scaleFactor %f", desc="The scale factor for the image spacing.")


class BRAINSResizeOutputSpec(TraitedSpec):
    outputVolume = File(desc="Resulting scaled image", exists=True)


class BRAINSResize(SEMLikeCommandLine):
    """title: Resize Image (BRAINS)

category: Registration

description: This program is useful for downsampling an image by a constant scale factor.

version: 5.2.0

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: This tool was developed by Hans Johnson.

acknowledgements: The development of this tool was supported by funding from grants NS050568 and NS40068 from the National Institute of Neurological Disorders and Stroke and grants MH31593, MH40856, from the National Institute of Mental Health.

"""

    input_spec = BRAINSResizeInputSpec
    output_spec = BRAINSResizeOutputSpec
    _cmd = " BRAINSResize "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False
