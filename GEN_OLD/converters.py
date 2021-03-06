# -*- coding: utf-8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec,
                    File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath)
import os


class CreateDICOMSeriesInputSpec(CommandLineInputSpec):
    patientName = traits.Str(argstr="--patientName %s", desc="The name of the patient (0010,0010)")
    patientID = traits.Str(argstr="--patientID %s", desc="The patient ID (0010,0020)")
    patientBirthDate = traits.Str(argstr="--patientBirthDate %s", desc="Patient birth date (0010,0030)")
    patientSex = traits.Str(argstr="--patientSex %s", desc="Patient sex (0010,0040)")
    patientComments = traits.Str(argstr="--patientComments %s", desc="Patient comments (0010,4000)")
    studyID = traits.Str(argstr="--studyID %s", desc="The study ID (0020,0010)")
    studyDate = traits.Str(argstr="--studyDate %s", desc="The date of the study (0008,0020)")
    studyTime = traits.Str(argstr="--studyTime %s", desc="The time of the study (0008,0030)")
    studyComments = traits.Str(argstr="--studyComments %s", desc="Study comments (0032,4000)")
    studyDescription = traits.Str(argstr="--studyDescription %s", desc="Study description (0008,1030)")
    modality = traits.Str(argstr="--modality %s", desc="Modality (0008,0060)")
    manufacturer = traits.Str(argstr="--manufacturer %s", desc="Manufacturer (0008,0070)")
    model = traits.Str(argstr="--model %s", desc="model (0008,1090)")
    seriesNumber = traits.Str(argstr="--seriesNumber %s", desc="The series number (0020,0011)")
    seriesDescription = traits.Str(argstr="--seriesDescription %s", desc="Series description (0008,103E)")
    seriesDate = traits.Str(argstr="--seriesDate %s", desc="The date of the series (0008,0021)")
    seriesTime = traits.Str(argstr="--seriesTime %s", desc="The time of the series (0008,0031)")
    rescaleIntercept = traits.Float(argstr="--rescaleIntercept %f", desc="Rescale interscept (0028,1052). Converts pixel values on disk to pixel values in memory. (Pixel value in memory) = (Pixel value on disk) * rescaleSlope + rescaleIntercept.  Default is 0.0. Data values are converted on write (the data is scaled and shifted so that the slope and interscept will bring it back to the current intensity range).")
    rescaleSlope = traits.Float(argstr="--rescaleSlope %f", desc="Rescale slope (0028,1053). Converts pixel values on disk to pixel values in memory. (Pixel value in memory) = (Pixel value on disk) * rescaleSlope + rescaleInterscept.  Default is 1.0. Data values are converted on write (the data is scaled and shifted so that the slope and interscept will bring it back to the current intensity range).")
    contentDate = traits.Str(argstr="--contentDate %s", desc="The date of the image content (0008,0023)")
    contentTime = traits.Str(argstr="--contentTime %s", desc="The time of the image content (0008,0033)")
    studyInstanceUID = traits.Str(argstr="--studyInstanceUID %s", desc="The study instance UID (0020,000d)")
    seriesInstanceUID = traits.Str(argstr="--seriesInstanceUID %s", desc="The series instance UID (0020,000e)")
    frameOfReferenceInstanceUID = traits.Str(argstr="--frameOfReferenceInstanceUID %s", desc="The frame of reference instance UID (0020,0052)")
    inputVolume = File(argstr="%s", desc="Input volume to be resampled", position=-1, exists=True)
    dicomDirectory = traits.Either(traits.Bool, Directory(), argstr="--dicomDirectory %s", desc="The directory to contain the DICOM series.", hash_files=False)
    dicomPrefix = traits.Str(argstr="--dicomPrefix %s", desc="The prefix of the DICOM filename.")
    dicomNumberFormat = traits.Str(argstr="--dicomNumberFormat %s", desc="The printf-style format to be used when creating the per-slice DICOM filename.")
    reverseImages = traits.Bool(argstr="--reverseImages ", desc="Reverse the slices.")
    useCompression = traits.Bool(argstr="--useCompression ", desc="Compress the output pixel data.")
    type = traits.Enum("UnsignedChar", "Char", "UnsignedChar", "Short", "UnsignedShort", "Int", "UnsignedInt", argstr="--type %s", desc="Type for the new output volume.")


class CreateDICOMSeriesOutputSpec(TraitedSpec):
    dicomDirectory = Directory(desc="The directory to contain the DICOM series.", exists=True)


class CreateDICOMSeries(SEMLikeCommandLine):
    """title: Create a DICOM Series

category: Converters

description: Create a DICOM Series from a Slicer volume. User can specify values for selected DICOM tags in the UI. Given the number of tags DICOM series have, it is impossible to expose all tags in UI. So only important tags can be set by the user.

version: 0.1.0.$Revision$(alpha)

documentation-url: https://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/CreateDICOMSeries

contributor: Bill Lorensen (GE)

acknowledgements: This command module was derived from Insight/Examples (copyright) Insight Software Consortium

"""

    input_spec = CreateDICOMSeriesInputSpec
    output_spec = CreateDICOMSeriesOutputSpec
    _cmd = " CreateDICOMSeries "
    _outputs_filenames = {'dicomDirectory':'dicomDirectory'}
    _redirect_x = False


class DWICompareInputSpec(CommandLineInputSpec):
    inputVolume1 = File(argstr="--inputVolume1 %s", desc="First input volume (.nhdr or .nrrd)", exists=True)
    inputVolume2 = File(argstr="--inputVolume2 %s", desc="Second input volume (.nhdr or .nrrd)", exists=True)
    useIdentityMeasurementFrame = traits.Bool(argstr="--useIdentityMeasurementFrame ", desc="Do comparisons with identity mesasurement frames")


class DWICompareOutputSpec(TraitedSpec):
    pass


class DWICompare(SEMLikeCommandLine):
    """title: Nrrd DWI comparison

category: Converters

description: Compares two nrrd format DWI images and verifies that gradient magnitudes, gradient directions, measurement frame, and max B0 value are identicle.  Used for testing DWIConvert.

version: 5.2.0

documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/DWIConvert

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Mark Scully (UIowa)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.  Additional support for DTI data produced on Philips scanners was contributed by Vincent Magnotta and Hans Johnson at the University of Iowa.

"""

    input_spec = DWICompareInputSpec
    output_spec = DWICompareOutputSpec
    _cmd = " DWICompare "
    _outputs_filenames = {}
    _redirect_x = False


class DWISimpleCompareInputSpec(CommandLineInputSpec):
    inputVolume1 = File(argstr="--inputVolume1 %s", desc="First input volume (.nhdr or .nrrd)", exists=True)
    inputVolume2 = File(argstr="--inputVolume2 %s", desc="Second input volume (.nhdr or .nrrd)", exists=True)
    checkDWIData = traits.Bool(argstr="--checkDWIData ", desc="check for existence of DWI data, and if present, compare it")


class DWISimpleCompareOutputSpec(TraitedSpec):
    pass


class DWISimpleCompare(SEMLikeCommandLine):
    """title: Nrrd DWI comparison

category: Converters

description: Compares two nrrd format DWI images and verifies that gradient magnitudes, gradient directions, measurement frame, and max B0 value are identicle.  Used for testing DWIConvert.

version: 5.2.0

documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/4.1/Modules/DWIConvert

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Mark Scully (UIowa)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.  Additional support for DTI data produced on Philips scanners was contributed by Vincent Magnotta and Hans Johnson at the University of Iowa.

"""

    input_spec = DWISimpleCompareInputSpec
    output_spec = DWISimpleCompareOutputSpec
    _cmd = " DWISimpleCompare "
    _outputs_filenames = {}
    _redirect_x = False


class OrientScalarVolumeInputSpec(CommandLineInputSpec):
    inputVolume1 = File(argstr="%s", desc="Input volume 1", position=-2, exists=True)
    outputVolume = traits.Either(traits.Bool, File(), argstr="%s", desc="The oriented volume", position=-1, hash_files=False)
    orientation = traits.Enum("Axial", "Coronal", "Sagittal", "RIP", "LIP", "RSP", "LSP", "RIA", "LIA", "RSA", "LSA", "IRP", "ILP", "SRP", "SLP", "IRA", "ILA", "SRA", "SLA", "RPI", "LPI", "RAI", "LAI", "RPS", "LPS", "RAS", "LAS", "PRI", "PLI", "ARI", "ALI", "PRS", "PLS", "ARS", "ALS", "IPR", "SPR", "IAR", "SAR", "IPL", "SPL", "IAL", "SAL", "PIR", "PSR", "AIR", "ASR", "PIL", "PSL", "AIL", "ASL", argstr="--orientation %s", desc="Orientation choices")


class OrientScalarVolumeOutputSpec(TraitedSpec):
    outputVolume = File(desc="The oriented volume", position=-1, exists=True)


class OrientScalarVolume(SEMLikeCommandLine):
    """title: Orient Scalar Volume

category: Converters

description: Orients an output volume. Rearranges the slices in a volume according to the selected orientation. The slices are not interpolated. They are just reordered and/or permuted. The resulting volume will cover the original volume. NOTE: since Slicer takes into account the orientation of a volume, the re-oriented volume will not show any difference from the original volume, To see the difference, save the volume and display it with a system that either ignores the orientation of the image (e.g. Paraview) or displays individual images.

version: 0.1.0.$Revision$(alpha)

documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/OrientImage

contributor: Bill Lorensen (GE)

acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.

"""

    input_spec = OrientScalarVolumeInputSpec
    output_spec = OrientScalarVolumeOutputSpec
    _cmd = " OrientScalarVolume "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
    _redirect_x = False
