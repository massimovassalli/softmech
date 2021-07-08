from ..importer import listModules,getModule

MODULE = 'protocols.cpoint'

def list():
    return listModules(__path__[0],MODULE)

def get(name):
    mod = getModule(name,MODULE)
    return mod.CP()