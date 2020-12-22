prnt = 'parent_ns'
vs = 'vars'
namespaces = {'global': {prnt: '', vs: []}}

def create(ns, parent):
    if ns not in namespaces:
        namespaces[ns] = {prnt: parent, vs: []}

def add(ns, var):
    if ns in namespaces:
        namespaces[ns][vs].append(var)

def get(ns, var):
    if ns == 'global':
        print('None' if var not in namespaces[ns][vs] else ns)
    elif var in namespaces[ns][vs]:
        print(ns)
    else:
        get(namespaces[ns][prnt], var)

funcs = {'create': create, 'add': add, 'get': get}
n = int(input())
for _ in range(n):
    cmd, p1, p2 = input().split()
    funcs[cmd](p1, p2)