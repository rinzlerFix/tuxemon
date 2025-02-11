# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from tuxemon.core.components.event.eventaction import EventAction


class WaitForInputAction(EventAction):
    """Pauses the event engine until specified button is pressed

    Valid Parameters: button

    * button (str): pygame key to wait for

    **Examples:**

    >>> action.__dict__
    {
        "type": "wait_for_input",
        "parameters": [
            "K_RETURN"
        ]
    }

    """
    name = "wait_for_input"
    valid_parameters = [
        (str, "button")
    ]

    def start(self):
        self.game.event_engine.button = self.parameters.button
        self.game.event_engine.state = "waiting for input"
        self.game.event_engine.wait = 2
