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

class Item:
    """
    Item represents an arbitrary item that can be checked into and out 
    of containers.
    """
    def __init__(self, id, container, tags):
		self.id 		= id
		self.container 	= container
		self.tags		= tags
