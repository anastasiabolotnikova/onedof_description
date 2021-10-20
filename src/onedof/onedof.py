import sys; sys.path.append('..')

import rbdyn as rbd

import OneDoF


mb, mbc, mbg, limits, visual_tf, collision_tf =\
  OneDoF.readUrdf('OneDoF', OneDoF.rootBody,
                       OneDoF.virtualJoints, [],
                       OneDoF.halfSitting)


def robot(fixed=False):
  if not fixed:
    return mb, mbc, mbg
  else:
    mbF = mbg.makeMultiBody(mbg.bodyIdByName(OneDoF.rootBody), True)
    mbcF = rbd.MultiBodyConfig(mbF)
    mbcF.zero(mbF)
    return mbF, mbcF, mbg

'''
def convexHull():
  fileByBodyName = OneDoF.stdCollisionsFiles(mb)
  return OneDoF.convexHull(fileByBodyName, mb)


def stpbvHull():
  fileByBodyName = OneDoF.stdCollisionsFiles(mb)
  return OneDoF.stpbvHull(fileByBodyName, mb)


def collisionTransforms():
  return collision_tf


def bounds():
  return OneDoF.nominalBounds(limits)


def stance():
  return OneDoF.halfSittingPose(mb), ('LeftFoot', 'RightFoot')


def forceSensors():
  return OneDoF.forceSensors


def accelerometerBody():
  return OneDoF.accelBody
'''
