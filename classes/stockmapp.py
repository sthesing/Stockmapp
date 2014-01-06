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

import sys
import json

class Stockmapp:
    """
    Stockmapp is a little tool to catalogue arbitrary items and to check them into and out of containers.
    """
    def __init__(self, settings='settings.json'):
        # Sometimes, settings can be None, in that case it should be 
        # standard, too.
        if not settings:
            settings = 'settings.json'
        
        # Read settings from JSON-File
        try:
            f = open(settings,'r')
            settings = json.loads(f.read())
            f.close()
        except IOError, e:
            print "## Error ##"
            print "No settings file could not be found."
            print "Please retry and specify a settings file or create the standard 'settings.json' file in the main directory of Stockmapp."
            print "If you want to generate one, use setup.py!"
            sys.exit(e)
        except ValueError, e:
            print "## Error ##"
            print "There is a problem with your settings file."
            print "Please fix it and retry."
            print "If you want to generate one, use setup.py!"
            sys.exit(e)
        
        # Use only what is inside "stockmapp_settings"
        try:
            settings = settings['stockmapp_settings']
        except KeyError, e:
            print "## Error ##"
            print "There is a problem with your settings file."
            print "It seems to be valid JSON, but not a valid Fism settings file."
            print "The key '" + e.message + "' is missing."
            print "Please fix it and retry."
            print "If you want to generate one, use setup.py!"
            sys.exit()

    def load_collection(self, filename):
        try:
            f = open(filename, 'r')
            return json.loads(f.read())['stockmapp_collection']
            f.close()
        except IOError, e:
            print "## Error ##"
            print "File not found."
            print "Please retry and specify a file."
            sys.exit(e)
        except ValueError, e:
            print "## Error ##"
            print "There is a problem with your collection file."
            print "Please fix it and retry."
            sys.exit(e)
    
    def add_item(self, collection, item_id, container='None', tags=[]):
        collection['items'].add({'container': container,
                                 'id': item_id,
                                 'tags': tags})
        
            

