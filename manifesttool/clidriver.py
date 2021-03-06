# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright 2016-2017 ARM Limited or its affiliates
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
import logging, sys

from manifesttool.argparser import MainArgumentParser
from manifesttool import create, parse, verify, cert, init, sign
from manifesttool import update
import colorama
colorama.init()


LOG = logging.getLogger(__name__)
LOG_FORMAT='[%(levelname)s] %(asctime)s - %(name)s - %(message)s'

def main():
    driver = CLIDriver()
    return driver.main()

class CLIDriver(object):

    def __init__(self):
        self.options = MainArgumentParser().parse_args().options

        log_level = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'exception': logging.CRITICAL
        }[self.options.log_level]
        logging.basicConfig(level=log_level,
                            format=LOG_FORMAT,
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.addLevelName( logging.INFO, "\033[1;32m%s\033[1;0m" % logging.getLevelName(logging.INFO))
        logging.addLevelName( logging.WARNING, "\033[1;93m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
        logging.addLevelName( logging.CRITICAL, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.CRITICAL))

        LOG.debug('CLIDriver created. Arguments parsed and logging setup.')

    def main(self):
        rc = { "create": create.main,
          "parse": parse.main,
          "verify": verify.main,
          "cert": cert.main,
          "init": init.main,
          "update" : update.main,
          "sign": sign.main
        }[self.options.action](self.options) or 0

        sys.exit(rc)
