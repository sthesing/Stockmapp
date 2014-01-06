##! /usr/bin/python
# -*- coding: utf8 -*-
## Copyright (c) 2014 Stefan Thesing
##
##This file is part of Stockmapp.
##
##Stockmapp is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##Stockmapp is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License
##along with Stockmapp. If not, see http://www.gnu.org/licenses/.

__author__ = "Stefan Thesing <software@webdings.de>"
__version__ = "0.1.0"
__date__ = "Date: 2014/01/06"
__copyright__ = "Copyright (c) 2014 Stefan Thesing"
__license__ = "GPL"

import sys
import argparse
from classes.stockmapp import Stockmapp

if __name__ == "__main__":
    """
    Stockmapp is a little tool to catalogue arbitrary items and to check them into and out of containers.
    """ 
    #################################################
    # Define command line arguments                 #
    #################################################
    
    # Define the parser
    parser = argparse.ArgumentParser(description=
        'Stockmapp is a little tool to catalogue arbitrary items \
        and to check them into and out of containers.')
    
    # General arguments
    parser.add_argument('collection', help='relative or absolute \
        path to the collection file, e.g. "foo/bar.json"')
    parser.add_argument('--settings', help='relative or absolute \
        path to a settings file, Default: "settings.json"')
    
    #################################################
    # Parse and process command line arguments      #
    #################################################
    
    # Well... parse them.
    args = parser.parse_args()
    
    # Init ia Stockmapp with the settings
    stockmapp = Stockmapp(args.settings)
