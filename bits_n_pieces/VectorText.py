def font_map(ch, fontdict):
    remapable = fdict.get(ch, None)
    if remapable:
        return fontdict[remapable]
    else:
        print(repr(ch), 'not fond in charmap')
    
    return 


def generate_greasepencil(text, col, pxwide, pos, fontdict):

    line_height = 38
    char_width = pxwide

    spaces = 0
    yof = 0
    xof = 0
    bcx, bcy = pos
    
    nt = bpy.data.node_groups['NodeTree.002']
    gp = nt.grease_pencil = bpy.data.grease_pencil.new('temp')
    layer = gp.layers.new('damzel')
    layer.line_width = 1
    layer.frames.new(1)

    for ch in text:
        if ch == "\n":
            yof -= line_height
            xof = 0
            continue
        
        if ch == " ":
            xof += char_width
            continue
        
        # ch = ch.tolower()

        v = font_map(ch, fontdict)
        if not v:
            xof += char_width
            continue

        for chain in v:
            s = layer.frames[0].strokes.new()
            s.draw_mode = '2DSPACE'
            s.points.add(len(chain))
            for idx, p in enumerate(chain):
                ap = Vector(p)*25
                x, y = ap[:2]
                xyz = ((x+bcx+xof), (y+bcy+yof), 0)
                s.points[idx].co = xyz

        xof += char_width


'''
- current usage, 3 spaces in a row will drop line, else it continues
- no case sensitivity yet, use all lowercase for now. it will output title case.

'''

text = """
this text was generated by grease pencil   
here as vectors    
{1, 3, 5}   
(var1, var2, var3)
@vectorized

"""

col = []
pxwide = 28
pos = 50, 50

generate_greasepencil(text, col, pxwide, pos, fontdict)