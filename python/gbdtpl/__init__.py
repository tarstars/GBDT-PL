try:
    from Booster import *
    from DataMat import *
except Exception as ex:
    print ('python2-3 compatability problem: ', ex)
    from .Booster import *
    from .DataMat import *
