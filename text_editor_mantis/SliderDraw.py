# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import bpy
import blf
import bgl
import math
import mathutils
from mathutils import Vector, Matrix
import bmesh
from bmesh.types import BMFace

from util import *

TextEditor = bpy.types.SpaceTextEditor
callback_dict = {}
point_dict = {}

## end of util functions

def tag_redraw_all_view2d():
    context = bpy.context

    for window in context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'TEXT_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        region.tag_redraw()


def callback_enable(n_id, settings):
    
    global callback_dict
    if n_id in callback_dict:
        return
    
    handle_pixel = TextEditor.draw_handler_add(
        draw_callback_px, (n_id, settings), 'WINDOW', 'POST_PIXEL')

    callback_dict[n_id] = handle_pixel
    tag_redraw_all_view2d()


def callback_disable(n_id):

    global callback_dict
    handle_pixel = callback_dict.get(n_id, None)
    if not handle_pixel:
        return
    
    TextEditor.draw_handler_remove(handle_pixel, 'WINDOW')

    del callback_dict[n_id]
    tag_redraw_all_view2d()


def callback_disable_all():
    global callback_dict
    temp_list = list(callback_dict.keys())
    for n_id in temp_list:
        if n_id:
            callback_disable(n_id)


def draw_callback_px(n_id, settings):
    context = bpy.context

    region = context.region
    # region2d = context.space_data.region_2d
    
    font_id = 0
    text_height = 13
    blf.size(font_id, text_height, 72)  # should check prefs.dpi

    region_mid_width = region.width / 2.0
    region_mid_height = region.height / 2.0

    rgb2 = (175/255, 228/255, 253/255, 0.4)
    rgb3 = (241/255, 206/255, 123/255, 0.6)

    ''' draw polygon '''
    x = 160
    y = region.height - 70

    polyline = [(0, 0), (200, 0), (200, -40), (0, -40)]
    bgl.glColor4f(*rgb2)
    bgl.glBegin(bgl.GL_POLYGON)
    for pointx, pointy in polyline:
        bgl.glVertex2f(pointx+x, pointy+y)
    bgl.glEnd()

    polyline = [(200, 0), (240, 0), (240, -40), (200, -40)]
    bgl.glColor4f(*rgb3)
    bgl.glBegin(bgl.GL_POLYGON)
    for pointx, pointy in polyline:
        bgl.glVertex2f(pointx+x, pointy+y)
    bgl.glEnd()

    polyline = [(240, 0), (400, 0), (400, -40), (240, -40)]
    bgl.glColor4f(*rgb2)
    bgl.glBegin(bgl.GL_POLYGON)
    for pointx, pointy in polyline:
        bgl.glVertex2f(pointx+x, pointy+y)
    bgl.glEnd()

    # ''' draw text '''
    # txt_width, txt_height = blf.dimensions(0, index)
    # bgl.glColor4f(*rgb)
    # blf.position(0, x - (txt_width / 2), y - (txt_height / 2), 0)
    # blf.draw(0, index)


