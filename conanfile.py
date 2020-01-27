#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class LibmodbusConan(ConanFile):
    name = "libmodbus"
    version = "3.1.6"
    description = "A Modbus library for Linux, Mac OS X, FreeBSD, QNX and Windows"
    topics = ("modbus")
    url = "https://github.com/swissdotnet-sa/conan-libmodbus"
    homepage = "https://github.com/stephane/libmodbus"
    author = "Simon Lepasteur <slepasteur@gmail.com>"
    license = "LGPL-2.1"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = self.homepage
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="fe0c141cd10d58bb848643f00f2d4b4005214f93312d7b66ac805fd369876651")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        with tools.chdir(self._source_subfolder):
            self.run("bash autogen.sh")
            autotools = AutoToolsBuildEnvironment(self)
            autotools.configure(args=["--without-documentation"])
            autotools.make()
            autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["modbus"]
