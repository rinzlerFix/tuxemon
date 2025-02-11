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

from tuxemon.core.components.event import get_npc
from tuxemon.core.components.event.eventaction import EventAction
from tuxemon.core.components.map import dirs2, get_direction


class PlayerFaceAction(EventAction):
    """Makes the player face a certain direction.

    Valid Parameters: direction

    EventAction parameter can be: "left", "right", "up", or "down"
    """
    name = "player_face"
    valid_parameters = [
        (str, "direction"),
    ]

    def start(self):
        # Get the parameters to determine what direction the player will face.
        direction = self.parameters.direction
        if direction not in dirs2:
            target = get_npc(self.game, direction)
            direction = get_direction(self.game.player1.tilepos, target.tilepos)

        # If we're doing a transition, only change the player's facing when we've reached the apex
        # of the transition.
        world_state = self.game.get_state_name("WorldState")
        if world_state.in_transition:
            world_state.delayed_facing = direction
        else:
            self.game.player1.facing = direction
