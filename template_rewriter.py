
{
'filename': "{}",            # ascii name
'class': """

class {0}(Node, SverchCustomTreeNode):

    bl_idname = '{1}'
    bl_label = '{2}'
    bl_icon = 'OUTLINER_OB_EMPTY'

{3}
    def init(self, context):
        # self.inputs.new('VerticesSocket', 'vertices', 'vertices')
        # self.inputs.new('StringsSocket', 'edges', 'edges')
        # self.inputs.new('MatrixSocket', 'matrix', 'matrix')
        pass

    def draw_buttons(self, context, layout):
        #
        #
        #
        #
        pass

    def update(self):
        pass

    def update_socket(self, context):
        self.update()
""",      

"ops": """

class {0}(bpy.types.Operator):

    bl_idname = '{1}'
    bl_label = '{2}'
    bl_options = ...

{3}
    def execute(self, context):
        n = context.node
        
        # if n:
        #     msg = ""
        #     self.report(.., msg)
        return
""",

# svClassName
'operator classes': "{}",    # svOps, ..
'own classes': "{}",         # svxClassName
'defs': "{}",           # fname, ..
'function defaults': '{}',   # fname var def var def .. ..

# imports are configurable
'imports': """
import bpy
import bmesh
import mathutils
from node_s import *
from util import *
import random
import math"""
,

'np': """
import numpy as np
""",

'mathutils*':
"""from mathutils import Vector, Matrix, Euler"""
,

'props': """
from bpy.props import {}"""
,
'proptypes': {
    'int': 'IntProperty',
    'float': 'FloatProperty',
    'str': "StringProperty",
    'bool': "BoolProperty",
    'enum': "EnumProperty",
    'vecf': "FloatVectorProperty",
},
'full_proptypes': {
    'int': 'IntProperty(----)',
    'float': 'FloatProperty(-----)',
    'str': "StringProperty(--)",
    'bool': "BoolProperty(--)",
    'enum': "EnumProperty(-------)",
    'vecf': "FloatVectorProperty(------)",
},


# is added automatically
'registration': {
    'r': """\n\n
def register():
""",
    'rc': """\
    bpy.utils.register_class({0})\n""",
    'u': """\n
def unregister():
""",
    'uc': """\
    bpy.utils.unregister_class({0})\n"""},


# this is optional as last line
'd': """\n
if __name__ == "__main__":
    register()
"""
}
