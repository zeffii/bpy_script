# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you may redistribute it, and/or
# modify it, under the terms of the GNU General Public License
# as published by the Free Software Foundation - either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, write to:
#
#   the Free Software Foundation Inc.
#   51 Franklin Street, Fifth Floor
#   Boston, MA 02110-1301, USA
#
# or go online at: http://www.gnu.org/licenses/ to view license options.
#
# ***** END GPL LICENCE BLOCK *****

'''
roadmap and thoughts:
https://github.com/zeffii/bpy_script/issues/2 

# bpy.ops.text.select_word()
# bpy.ops.text.selection_set()
# bpy.ops.text.cursor_set(x=0, y=0)
# bpy.ops.text.replace()
# bpy.ops.text.run_script()
# bpy.ops.text.selection_set(select=False)  # sets end
# bpy.ops.text.move(type='LINE_BEGIN')   ‘PREVIOUS_WORD’, ‘NEXT_WORD’, 
# bpy.ops.text.replace_set_selected()

'''

import bpy
from bpy.props import FloatProperty, IntProperty

import re
import ast

from . import SliderDraw as SD


settings = {'draw': 'details'}
bpy.types.Text.myIntSlider = IntProperty(name='int_slider', default=10)
bpy.types.Text.myFloatSlider = FloatProperty(name='float_slider', default=1.0)


def find_bounds(idx, k):
    ''' witness extreme lazyness '''

    pattern = '(=| |,|[a-zA-Z_])'
    less = re.sub(pattern, ' ', k)
    left = less[:idx].lstrip().split(' ')[-1]
    right = less[idx:].rstrip().split(' ')[0]
    summed = left + right

    if not summed:
        return
    else:
        begin = idx - len(left)
        end = idx + len(right)
        v = ast.literal_eval(summed)
        return v, begin, end


class TextSelectionOperator(bpy.types.Operator):

    """Defines a Text Op for testing"""
    bl_idname = "text.text_sel_op"
    bl_label = "bladibla"

    def execute(self, context):
        txt = context.edit_text
        idx = txt.current_character
        k = txt.current_line.body
        line_idx = txt.current_line_index

        if not k:
            print('end early')
            return{'FINISHED'}

        found = find_bounds(idx, k)
        if found:
            v, begin, end = found
            print('found:', found)
            bpy.ops.text.move_select(type='NEXT_WORD')
            bpy.ops.text.move_select(type='PREVIOUS_WORD')
        return{'FINISHED'}


class MantisPropertiesPanel(bpy.types.Panel):

    """Creates a Panel in the TextEditor properties window"""
    bl_label = "Mantis replcv"
    bl_idname = "text.somefunction"
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    # bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        scn = bpy.context.scene
        st = context.space_data

        text = bpy.context.edit_text
        if text:
            cc = text.current_character
            sec = text.select_end_character
            selection = not (cc == sec)

            n_id = text.name
            if selection:

                txt = context.edit_text
                idx = txt.current_character
                k = txt.current_line.body

                if not k and idx:
                    SD.callback_disable(n_id)
                    return

                line_idx = txt.current_line_index

                value, n, e = find_bounds(idx, k)

                if isinstance(value, (int, float)):
                    SD.callback_enable(n_id, settings.copy())
                else:
                    SD.callback_disable(n_id)

                if isinstance(value, float):
                    row.prop(text, 'myFloatSlider')
                if isinstance(value, int):
                    row.prop(text, 'myIntSlider')

            else:
                layout.label('no active text')
                SD.callback_disable(n_id)

        self.layout.operator("text.text_sel_op", text='select word')


def register():
    bpy.utils.register_class(TextSelectionOperator)
    bpy.utils.register_class(MantisPropertiesPanel)


def unregister():
    bpy.utils.unregister_class(MantisPropertiesPanel)
    bpy.utils.unregister_class(TextSelectionOperator)
