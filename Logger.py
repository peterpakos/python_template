# -*- coding: utf-8 -*-
"""
Logger module

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2017 WANdisco. All rights reserved.
"""

import os
import logging


def get_logger(dir_name='logs', file_name='application.log', debug=False, quiet=False,
               console_level='INFO', file_level='INFO'):
    log_file = '%s/%s.log' % (dir_name, file_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not quiet and console_level:
        if debug:
            console_formatter = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s %(message)s')
        else:
            console_formatter = logging.Formatter('%(asctime)s %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG if debug else getattr(logging, console_level.upper()))
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    if file_level:
        file_formatter = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s %(message)s')
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG if debug else getattr(logging, file_level.upper()))
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
