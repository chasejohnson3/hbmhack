# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class CurvatureAnisotropicDiffusionInputSpec(CommandLineInputSpec):
    conductance = traits.Float(argstr="--conductance %f", desc="Conductance controls the sensitivity of the conductance term. As a general rule, the lower the value, the more strongly the filter preserves edges. A high value will cause diffusion (smoothing) across edges. Note that the number of iterations controls how much smoothing is done within regions bounded by edges.")
    iterations = traits.Int(argstr="--iterations %d", desc="The more iterations, the more smoothing. Each iteration takes the same amount of time. If it takes 10 seconds for one iteration, then it will take 100 seconds for 10 iterations. Note that the conductance controls how much each iteration smooths across edges.")
    timeStep = traits.Float(argstr="--timeStep %f", desc="The time step depends on the dimensionality of the image. In Slicer the images are 3D and the default (.0625) time step will provide a stable solution.")
    inputVolume = File(argstr="%s", desc="Input volume to be filtered", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="Output filtered", position=-1, hash_files=False)


class CurvatureAnisotropicDiffusionOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output filtered", position=-1, exists=True)


class CurvatureAnisotropicDiffusion(SEMLikeCommandLine):
    """title: Curvature Anisotropic Diffusion

category: Filtering.Denoising

description: Performs anisotropic diffusion on an image using a modified curvature diffusion equation (MCDE).\n\nMCDE does not exhibit the edge enhancing properties of classic anisotropic diffusion, which can under certain conditions undergo a 'negative' diffusion, which enhances the contrast of edges.  Equations of the form of MCDE always undergo positive diffusion, with the conductance term only varying the strength of that diffusion. \n\n Qualitatively, MCDE compares well with other non-linear diffusion techniques.  It is less sensitive to contrast than classic Perona-Malik style diffusion, and preserves finer detailed structures in images.  There is a potential speed trade-off for using this function in place of Gradient Anisotropic Diffusion.  Each iteration of the solution takes roughly twice as long.  Fewer iterations, however, may be required to reach an acceptable solution.

version: 0.1.0.$Revision$(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/CurvatureAnisotropicDiffusion

contributor: Bill Lorensen (GE)

acknowledgements: This command module was derived from Insight/Examples (copyright) Insight Software Consortium

"""

    input_spec = CurvatureAnisotropicDiffusionInputSpec
    output_spec = CurvatureAnisotropicDiffusionOutputSpec
    _cmd = " CurvatureAnisotropicDiffusion "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False


class GaussianBlurImageFilterInputSpec(CommandLineInputSpec):
    sigma = traits.Float(argstr="--sigma %f", desc="Sigma value in physical units (e.g., mm) of the Gaussian kernel")
    inputVolume = File(argstr="%s", desc="Input volume", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="Blurred Volume", position=-1, hash_files=False)


class GaussianBlurImageFilterOutputSpec(TraitedSpec):
    outputVolume = File(desc="Blurred Volume", position=-1, exists=True)


class GaussianBlurImageFilter(SEMLikeCommandLine):
    """title: Gaussian Blur Image Filter

category: Filtering.Denoising

description: Apply a gaussian blurr to an image

version: 0.1.0.$Revision: 1.1 $(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/GaussianBlurImageFilter

contributor: Julien Jomier (Kitware), Stephen Aylward (Kitware)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = GaussianBlurImageFilterInputSpec
    output_spec = GaussianBlurImageFilterOutputSpec
    _cmd = " GaussianBlurImageFilter "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False


class GradientAnisotropicDiffusionInputSpec(CommandLineInputSpec):
    conductance = traits.Float(argstr="--conductance %f", desc="Conductance controls the sensitivity of the conductance term. As a general rule, the lower the value, the more strongly the filter preserves edges. A high value will cause diffusion (smoothing) across edges. Note that the number of iterations controls how much smoothing is done within regions bounded by edges.")
    iterations = traits.Int(argstr="--iterations %d", desc="The more iterations, the more smoothing. Each iteration takes the same amount of time. If it takes 10 seconds for one iteration, then it will take 100 seconds for 10 iterations. Note that the conductance controls how much each iteration smooths across edges.")
    timeStep = traits.Float(argstr="--timeStep %f", desc="The time step depends on the dimensionality of the image. In Slicer the images are 3D and the default (.0625) time step will provide a stable solution.")
    inputVolume = File(argstr="%s", desc="Input volume to be filtered", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="Output filtered", position=-1, hash_files=False)
    useImageSpacing = traits.Bool(argstr="--useImageSpacing ", desc="![CDATA[Take into account image spacing in the computation.  It is advisable to turn this option on, especially when the pixel size is different in different dimensions. However, to produce results consistent with Slicer4.2 and earlier, this option should be turned off.]]")


class GradientAnisotropicDiffusionOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output filtered", position=-1, exists=True)


class GradientAnisotropicDiffusion(SEMLikeCommandLine):
    """title: Gradient Anisotropic Diffusion

category: Filtering.Denoising

description: Runs gradient anisotropic diffusion on a volume.\n\nAnisotropic diffusion methods reduce noise (or unwanted detail) in images while preserving specific image features, like edges.  For many applications, there is an assumption that light-dark transitions (edges) are interesting.  Standard isotropic diffusion methods move and blur light-dark boundaries.  Anisotropic diffusion methods are formulated to specifically preserve edges. The conductance term for this implementation is a function of the gradient magnitude of the image at each point, reducing the strength of diffusion at edges. The numerical implementation of this equation is similar to that described in the Perona-Malik paper, but uses a more robust technique for gradient magnitude estimation and has been generalized to N-dimensions.

version: 0.1.0.$Revision$(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/GradientAnisotropicDiffusion

contributor: Bill Lorensen (GE)

acknowledgements: This command module was derived from Insight/Examples (copyright) Insight Software Consortium

"""

    input_spec = GradientAnisotropicDiffusionInputSpec
    output_spec = GradientAnisotropicDiffusionOutputSpec
    _cmd = " GradientAnisotropicDiffusion "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False


class MedianImageFilterInputSpec(CommandLineInputSpec):
    neighborhood = InputMultiPath(traits.Int, argstr="--neighborhood %s", desc="The size of the neighborhood in each dimension", sep=",")
    inputVolume = File(argstr="%s", desc="Input volume to be filtered", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="Output filtered", position=-1, hash_files=False)


class MedianImageFilterOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output filtered", position=-1, exists=True)


class MedianImageFilter(SEMLikeCommandLine):
    """title: Median Image Filter

category: Filtering.Denoising

description: The MedianImageFilter is commonly used as a robust approach for noise reduction. This filter is particularly efficient against "salt-and-pepper" noise. In other words, it is robust to the presence of gray-level outliers. MedianImageFilter computes the value of each output pixel as the statistical median of the neighborhood of values around the corresponding input pixel.

version: 0.1.0.$Revision$(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/MedianImageFilter

contributor: Bill Lorensen (GE)

acknowledgements: This command module was derived from Insight/Examples/Filtering/MedianImageFilter (copyright) Insight Software Consortium

"""

    input_spec = MedianImageFilterInputSpec
    output_spec = MedianImageFilterOutputSpec
    _cmd = " MedianImageFilter "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False
