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

import logging
import os.path

from tuxemon.constants import paths
from tuxemon.core import prepare
from tuxemon.core.components.event.eventaction import EventAction
from tuxemon.core.platform import mixer

logger = logging.getLogger(__name__)


class PlayMusicAction(EventAction):
    """Plays a music file from "resources/music/"

    Valid Parameters: filename
    """
    name = "play_music"
    valid_parameters = [
        (str, "filename"),
    ]

    def start(self):
        filename = self.parameters.filename

        try:
            mixer.music.load(os.path.join(paths.BASEDIR, prepare.DATADIR, "music", filename))
            mixer.music.set_volume(prepare.CONFIG.music_volume)
            mixer.music.play(-1)
        except Exception as e:
            logger.error(e)
            logger.error('unable to play music')

        # Keep track of what song we're currently playing
        self.game.current_music["status"] = "playing"
        self.game.current_music["song"] = filename
