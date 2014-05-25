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
'''

import bpy
import re

# def has_selection(self_view, text):
#     return not (text.select_end_line == text.current_line and
#                 text.current_character == text.select_end_character)

def find_bounds(idx, k):
    ''' witness extreme lazyness '''

    pattern = '(=| |,|[a-zA-Z_])'
    less = re.sub(pattern, ' ', k)
    left = less[:idx].lstrip().split(' ')[-1]
    right = less[idx:].rstrip().split(' ')[0]
    summed = left + right
    return summed or None


class TextSelectionOperator(bpy.types.Operator):
    """Defines a Text Op for testing"""
    bl_idname = "text.text_sel_op"
    bl_label = "bladibla"
 
    def execute(self, context):
        # bpy.ops.text.select_word()
        txt = context.edit_text        
        idx = txt.current_character
        k = txt.current_line.body

        if not k:
            print('end early')
            return{'FINISHED'}

        print(idx, dir(idx))

        found = find_bounds(idx, k)
        if found:
            print(found)
        return{'FINISHED'}

# bpy.ops.text.line_number()
# bpy.ops.text.cursor_set(x=0, y=0)
# bpy.ops.text.select_line()
# txt.current_line_index
# bpy.ops.text.replace()
# bpy.ops.text.run_script()
# bpy.ops.text.select_word()  <- this fails to select float types
# bpy.ops.text.selection_set(select=False)
# bpy.ops.text.move(type='LINE_BEGIN')   ‘PREVIOUS_WORD’, ‘NEXT_WORD’, 

class MantisPropertiesPanel(bpy.types.Panel):
    """Creates a Panel in the TextEditor properties window"""
    bl_label = "Mantis replcv"
    bl_idname = "TEXT_OT_somefunction"
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_context = "object"
 
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        scn = bpy.context.scene

        text = bpy.context.edit_text
        if text:
            no_selection = (text.current_character == text.select_end_character)
            tk = 'has select' if not no_selection else 'good, no selection'
            layout.label(tk)
            print("updated")
        else:
            layout.label('no active text')

        # display stringbox and download button
        #self.layout.prop(scn, "gist_id_property")
        self.layout.operator("text.text_sel_op", text='select word')


def register():
    bpy.utils.register_class(TextSelectionOperator)
    bpy.utils.register_class(MantisPropertiesPanel)


def unregister():
    bpy.utils.unregister_class(MantisPropertiesPanel)
    bpy.utils.unregister_class(TextSelectionOperator)
