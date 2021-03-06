#!/usr/bin/env python
#
# Copyright (c) 2013, Roberto Riggio
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the CREATE-NET nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY CREATE-NET ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CREATE-NET BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version < '2.7':
    raise ValueError("Sorry Python versions older than 2.7 are not supported")

setup(name="joule",
      version="0.1",
      description="Joule",
      author="Roberto Riggio",
      author_email="roberto.riggio@create-net.org",
      url="https://github.com/rriggio/joule",
      long_description="Joule is an energy consumption profiler for WLANs",
      data_files = [('etc/', ['xively.conf'])],
      entry_points={ "console_scripts" : [ "joule-daemon=joule.daemon:main",
                     "joule-profiler=joule.profiler:main",
                     "joule-modeller=joule.modeller:main",
                     "joule-dumpcsv=joule.dumpcsv:main",
                     "joule-template=joule.template:main"]},
      packages=['joule'],
      license = "Python",
      platforms="any"
)
