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

# def has_selection(self_view, text):
#     return not (text.select_end_line == text.current_line and
#                 text.current_character == text.select_end_character)


# class GistDownloadButton(bpy.types.Operator):
#     """Defines a button"""
#     bl_idname = "scene.download_gist"
#     bl_label = "Download given gist from id only"
 
#     def execute(self, context):
#         # could name this filename instead of gist_id for new .blend text.
#         gist_id = context.scene.gist_id_property
#         bpy.data.texts.new(gist_id)
#         bpy.data.texts[gist_id].write(get_file(gist_id))
#         return{'FINISHED'}


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
        #self.layout.operator("scene.download_gist", text='Download to .blend')


def register():
    bpy.utils.register_class(MantisPropertiesPanel)


def unregister():
    bpy.utils.unregister_class(MantisPropertiesPanel)
