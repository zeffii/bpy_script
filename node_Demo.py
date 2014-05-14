
import bpy
import bmesh
import mathutils
from node_s import *
from util import *
import random
import math

import numpy as np
from mathutils import Vector, Matrix, Euler
from bpy.props import IntProperty, FloatProperty, StringProperty
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty

class svNodeDemo(Node, SverchCustomTreeNode):

    bl_idname = 'node.BmeshViewerNode'
    bl_label = 'Bmesh Viewer Draw'
    bl_icon = 'OUTLINER_OB_EMPTY'

    demo_range = IntProperty(----)
    demo_ratio = FloatProperty(-----)
    some_value = StringProperty(--)
    some_options = EnumProperty(-------)

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


class NDop1(bpy.types.Operator):

    bl_idname = 'node.svDemoOpOne'
    bl_label = 'Bmesh Viewer Draw'
    bl_options = ...

    demo_range = IntProperty(----)

    def execute(self, context):
        n = context.node
        
        # if n:
        #     msg = ""
        #     self.report(.., msg)
        return


class NDop2(bpy.types.Operator):

    bl_idname = 'node.svDemoOpTwo'
    bl_label = 'Bmesh Viewer Draw'
    bl_options = ...

    print_message = StringProperty(--)
    print_message2 = StringProperty(--)

    def execute(self, context):
        n = context.node
        
        # if n:
        #     msg = ""
        #     self.report(.., msg)
        return



def register():
    bpy.utils.register_class(svNodeDemo)
    bpy.utils.register_class(NDop1)
    bpy.utils.register_class(NDop2)


def unregister():
    bpy.utils.unregister_class(svNodeDemo)
    bpy.utils.unregister_class(NDop1)
    bpy.utils.unregister_class(NDop2)


if __name__ == "__main__":
    register()
