#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Test AEL Mobybgames asset scraper.
# This testing file is intended for scraper development and file dumping.
# For more thorough tests sett the unittest_MobyGames_* scrips.
#

# --- Python standard library ---
from __future__ import unicode_literals
import os
import pprint
import sys

# --- AEL modules ---
if __name__ == "__main__" and __package__ is None:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print('Adding to sys.path {0}'.format(path))
    sys.path.append(path)
from resources.scrap import *
from resources.utils import *

# --- Test data -----------------------------------------------------------------------------------
games = {
    'metroid' : ('Metroid', 'Metroid', 'Nintendo SNES'),
    'mworld' : ('Super Mario World', 'Super Mario World', 'Nintendo SNES'),
    'sonic' : ('Sonic The Hedgehog', 'Sonic The Hedgehog (USA, Europe)', 'Sega MegaDrive'),
    'chakan' : ('Chakan', 'Chakan', 'Sega MegaDrive'),
}

# --- main ----------------------------------------------------------------------------------------
print('*** MobyGames search **********************************************************************')
set_log_level(LOG_DEBUG) # >> LOG_INFO, LOG_VERB, LOG_DEBUG

# --- Create scraper object ---
settings = {
    'scraper_mobygames_apikey' : '', # Do not forget to set the API key.
}
scraper_obj = MobyGames(settings)
scraper_obj.set_verbose_mode(False)
scraper_obj.set_debug_file_dump(True, os.path.dirname(__file__))

# --- Get candidates ---
# candidate_list = scraper_obj.get_candidates(*games['metroid'])
# candidate_list = scraper_obj.get_candidates(*games['mworld'])
candidate_list = scraper_obj.get_candidates(*games['sonic'])
# candidate_list = scraper_obj.get_candidates(*games['chakan'])

# Cases with unknown platform must be tested as well.
# Cases with unknown API key must be tested as well.

# --- Print search results ---
# pprint.pprint(candidate_list)
print_candidate_list(candidate_list)
if not candidate_list:
    print('No candidates found.')
    sys.exit(0)

# --- Print list of assets found ---
print('*** MobyGames game images *****************************************************************')
# --- Get all assets ---
# assets = scraper_obj.get_assets_all(candidate_list[0])
# pprint.pprint(assets)
# print_game_assets(assets)

# --- Get specific assets ---
candidate = candidate_list[0]
print_game_assets(scraper_obj.get_assets(candidate, ASSET_TITLE_ID))
print_game_assets(scraper_obj.get_assets(candidate, ASSET_SNAP_ID))
print_game_assets(scraper_obj.get_assets(candidate, ASSET_BOXFRONT_ID))
print_game_assets(scraper_obj.get_assets(candidate, ASSET_BOXBACK_ID))
print_game_assets(scraper_obj.get_assets(candidate, ASSET_CARTRIDGE_ID))
print_game_assets(scraper_obj.get_assets(candidate, ASSET_FANART_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_BANNER_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_CLEARLOGO_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_FLYER_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_3DBOX_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_MAP_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_MANUAL_ID))
# print_game_assets(scraper_obj.get_assets(candidate, ASSET_TRAILER_ID))
