# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:23:55 2021

@author: d.glaesner
"""

import ctypes
import sys

from ctypes.util import find_library
from cpuid import cpuid
from cpuid import cpu_vendor
from cpuid import cpu_name
from cpuid import cpu_microarchitecture



def check_python():
    """
    checks if the version of installed python meets the tensorflow requirements
    """
    print("Checking Python installation:")
    py_version = sys.version_info.major, sys.version_info.minor
    print("  => Python version: %d.%d" % py_version)
    if (py_version[0] != 3 or py_version[1]  < 5 or py_version[1] > 8):
        print("  => ATTENTION: TensorFlow requires Python version 3.5 - 3.8.")
    print("\n")


def check_tensorflow():
    """
    checks if tensorflow module is installed correctly
    """
    print("Checking Tensorflow installation:")
    try:
        import tensorflow as tf
        print("  => TensorFlow successfully installed.")
        print("  => Version: ", tf.__version__)
        print("  => GPU Support: ", tf.test.is_built_with_cuda())
        print("  => GPU Devices: ",tf.config.list_physical_devices('GPU'))
    except ImportError as error_code:
        print("  => ERROR: Failed to import the TensorFlow module.")
        print(error_code)
    print("\n")


def check_cuda_dlls():
    """
    checks if the CUDA dlls are available
    """
    print("Checking CUDA installation:")
    check_dll("msvcp140.dll")
    check_dll("cudart64_110.dll")
    check_dll("nvcuda.dll")
    check_dll("cudnn64_8.dll")
    print("\n")


def check_hardware():
    """
    checks the hardware
    """
    print("Checking Hardware:")
    print("  => Vendor ID         : %s" % cpu_vendor())
    print("  => CPU name          : %s" % cpu_name())
    print("  => Microarchitecture : %s%s" % cpu_microarchitecture())
    print("  => Vector instructions supported:")
    print("     -> SSE    : %s" % has_instruction(1, 3, 25))
    print("     -> SSE2   : %s" % has_instruction(1, 3, 26))
    print("     -> SSE3   : %s" % has_instruction(1, 2, 0))
    print("     -> SSSE3  : %s" % has_instruction(1, 2, 9))
    print("     -> SSE4.1 : %s" % has_instruction(1, 2, 19))
    print("     -> SSE4.2 : %s" % has_instruction(1, 2, 20))
    print("     -> SSE4a  : %s" % has_instruction(0x80000001, 2, 6))
    print("     -> AVX    : %s" % has_instruction(1, 2, 28))
    print("     -> AVX2   : %s" % has_instruction(7, 1, 5))
    print("     -> BMI1   : %s" % has_instruction(7, 1, 3))
    print("     -> BMI2   : %s" % has_instruction(7, 1, 8))
    print("\n")

    if has_instruction(1, 2, 28) != "Yes":
        print("  => ATTENTION: instruction set AVX is needed")


def has_instruction(identifier, reg_idx, bit):
    """
    checks if instruction-set is available
    returns 'Yes' if available and '--' if not
    """
    regs = cpuid(identifier)
    if (1 << bit) & regs[reg_idx]:
        return "Yes"
    return "--"


def check_dll(name):
    """
    checks if a dll is available
    """
    try:
        _ = ctypes.WinDLL(name)
        dll_path = find_library(name)
        print("  => %s found:\n      %s" %(name, dll_path))
    except OSError:
        print("  => ATTENTION: Could not load '%s'" %name)

check_python()
check_tensorflow()
check_cuda_dlls()
check_hardware()
