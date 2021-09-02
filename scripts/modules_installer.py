#!/usr/bin/env python3
"""
/****************************************************************************
    pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
    stored in Postgres
    -------------------
    begin                : 2018-04-22
    copyright            : (C) 2008 by Salvatore Larosa
    email                : lrssvtml (at) gmail (dot) com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *                                                                        *
 ***************************************************************************/
"""

import subprocess
import sys
import platform
#from .. modules.utility.pyarchinit_OS_utility import Pyarchinit_OS_Utility

packages = sys.argv[1].split(',') if len(sys.argv) >= 2 else []

# Adding the dependencies python modules in
# package list in order to install via pip module


if not packages:
    packages = [
        'totalopenstation'
    ]

python_path = sys.exec_prefix
python_version = sys.version[:3]

if platform.system()=='Windows':
    cmd = '{}\python'.format(python_path)
elif platform.system()=='Darwin':
    cmd = '{}/bin/python{}'.format(python_path, python_version)
else:
    cmd = '{}/bin/python{}'.format(python_path, python_version)

# install pip if it is not found

for p in packages:
    
    subprocess.check_call(['python','-m','pip', 'install',  p ], shell=True)
    
