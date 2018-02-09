# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import struct
from . import core

"""
Human Interface Device (HID) specific descriptors
=================================================

The spec docs are available here: http://www.usb.org/developers/hidpage/

* Author(s): Scott Shawcroft
"""

class HIDDescriptor(core.Descriptor):
    fields = [('bcdHID', "H", 0x0111),
              ('bCountryCode', "b", 0)]
    bDescriptorType = 0x21

    def __init__(self, *args, **kwargs):
        self.subdescriptors = []
        if "subdescriptors" in kwargs:
            self.subdescriptors = kwargs["subdescriptors"]
        super().__init__(*args, **kwargs)

    def __bytes__(self):
        pieces = [super().__bytes__()]
        pieces.append(struct.pack("b", len(self.subdescriptors)))
        for subdescriptor in self.subdescriptors:
            pieces.append(struct.pack("bH",
                                      subdescriptor.bDescriptorType,
                                      subdescriptor.bLength))
        return b''.join(pieces)

    @property
    def bLength(self):
        return 6 + 3 * len(self.subdescriptors)

class ReportDescriptor:
    pass

class ReportItem:
    def __init__(self, data):
        pass

class MainItem(ReportItem):
    itemType = 0x0
    pass

class GlobalItem(ReportItem):
    itemType = 0x1
    pass

class LocalItem(ReportItem):
    itemType = 0x2
    pass

# TODO(tannewt): Maybe provide a separate module that provides constants
# for the bits in the input, output and feature data bytes.
class Input(MainItem):
    itemTag = 0b1000

class Output(MainItem):
    itemTag = 0b1001

class Feature(MainItem):
    itemTag = 0b1011

class Collection(MainItem):
    itemTag = 0b1010

class EndCollection(MainItem):
    itemTag = 0b1100

class UsagePage(GlobalItem):
    itemTag = 0b0000

class LogicalMinimum(GlobalItem):
    itemTag = 0b0001

class LogicalMaximum(GlobalItem):
    itemTag = 0b0010

class PhysicalMinimum(GlobalItem):
    itemTag = 0b0011

class PhysicalMaximum(GlobalItem):
    itemTag = 0b0100

class UnitExponent(GlobalItem):
    itemTag = 0b0101

class Unit(GlobalItem):
    itemTag = 0b0110

class ReportSize(GlobalItem):
    itemTag = 0b0111

class ReportID(GlobalItem):
    itemTag = 0b1000

class ReportCount(GlobalItem):
    itemTag = 0b1001
