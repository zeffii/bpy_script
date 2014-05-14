# ez writer.
import ast


def write_class(nfile, sfile, cname, tk, type_class):
    g = next(nfile)
    if g.strip().startswith('idname'):
        idname = g.strip().split(' ')[1]
    else:
        print('line directly following op declaration must have idname')
        print('--ending early')
        return

    g = next(nfile)
    if g.strip().startswith('label'):
        label = g.strip().split(' ', 1)[1]
    else:
        print("label must follow idname on the next line")
        print('--ending early')
        return

    # expecting an empty line here
    g = next(nfile)
    if not len(g.strip()) == 0:
        print("must place empty line after label")
        return

    write_string = tk[type_class].format(cname, idname, label, "{}")

    tcount = 0
    prop_list = []
    while True:
        g = next(nfile)
        if g.strip() == "/":
            print('done parsing class {}'.format(cname))
            break
        if g.strip().split(' ')[0] in tk['proptypes']:
            ptype, pname = g.strip().split(' ')
            prop_list.append([ptype, pname])

        # prevent endess loop, if possible
        tcount += 1
        if tcount > 100:
            break

    # assemble properties as class props
    rw = []
    indent = "    "
    for prop in prop_list:
        ptype, pname = prop
        ptype = tk['full_proptypes'][ptype]
        rw.append(indent + '{0} = {1}\n'.format(pname, ptype))
    props_as_ml_string = ''.join(rw)

    w = write_string.format(props_as_ml_string)
    sfile.write(w)


def line_parser(tk, sfile, nfile):
    output_cache = {}
    store_references = {}
    output_cache['classes'] = []

    for line in nfile:
        k = line.strip()

        defining = "token"
        if k.startswith("imports"):
            sfile.write(tk['imports'])
        elif k.startswith("np"):
            sfile.write('\n' + tk['np'])
        elif k.startswith('mathutils*'):
            sfile.write(tk.get(k.strip(), ""))
        elif k.startswith("class"):

            f = k.split(' ')
            classname = f[1]
            output_cache['classes'].append(classname)

            write_class(nfile, sfile, classname, tk, 'class')

        elif line.startswith('props'):
            l = k.split()[1:]
            tstr = ""
            plist = [tk['proptypes'][prop] for prop in l]
            plist_str = ", ".join(plist)
            sfile.write(tk['props'].format(plist_str))

        elif line.startswith('op '):
            opname = line.strip().split(' ')[1]
            output_cache['classes'].append(opname)

            write_class(nfile, sfile, opname, tk, 'ops')

        elif (len(k.strip()) == 1):

            # find classnames and register in order
            if k.startswith('r'):
                sfile.write(tk['registration']['r'])
                for cl in output_cache['classes']:
                    sfile.write(tk['registration']['rc'].format(cl))

                sfile.write(tk['registration']['u'])
                for cl in output_cache['classes']:
                    sfile.write(tk['registration']['uc'].format(cl))

            if k == 'd':
                sfile.write(tk['d'])


def do_write(input_name, output_name):

    filename = "template_rewriter.py"
    script = output_name + ".py"

    with open(filename) as rfile:
        file_str = "".join(rfile.readlines())
        tk = ast.literal_eval(file_str)

        with open(script, "w") as sfile:
            with open(input_name) as nfile:
                line_parser(tk, sfile, nfile)


def get_script(input_name):
    with open(input_name) as ifile:

        # skip all initial comments
        fn = "#"
        while fn.startswith("#") or len(fn.strip()) == 0:
            fn = next(ifile)

        if 'filename' in fn:
            a = fn.replace("filename", "")
            output_name = a.strip()

        do_write(input_name, output_name)

get_script("node_Demo.temp_node")
