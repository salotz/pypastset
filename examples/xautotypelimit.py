#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# --- BEGIN_HEADER ---
#
# xtemplatelimits - default and type casting example xfunction application
# Copyright (C) 2010-2012  The pypastset project lead by Brian Vinter
#
# This file is part of pypastset.
#
# pypastset is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# pypastset is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# -- END_HEADER ---
#

"""Example PastSet application investigating tuple-limits"""

import pastset

entries = [(123, '42', '3.14', 1), (123, ), (123, '42', '3.14', 1, 42),
           (123, '42', '3.14', 1, 42, 43)]
pset = pastset.PastSet()
loose_type = pset.enter(('Test', int, float, str))
strict_type = pset.enter(('Test', int, float, str), 'xtypecast')
for entry in entries:
    try:
        loose_type.move(entry)
        print "loose content: %s" % loose_type.observe()
    except Exception, exc:
        print "loose handling of entry %s failed: %s" % (entry, exc)
    try:
        strict_typet.move(entry)
        print "strict content: %s" % strict_type.observe()
    except Exception, exc:
        print "strict handling of entry %s failed: %s" % (entry, exc)

pset.halt()

