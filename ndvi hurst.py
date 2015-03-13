# coding:utf-8
from numpy import *
from numpy.linalg import lstsq
import arcpy

#计算栅格ndvi的hurst指数

seterr(divide='ignore', invalid='ignore')

arcpy.env.workspace = r"H:\RS\年均NDVI"
srcfiles = arcpy.ListRasters()
N = len(srcfiles)
X = [arcpy.RasterToNumPyArray(
    srcfiles[i], nodata_to_value=-100.0) for i in range(N)]
X = array(X)

shape = X.shape

T = array([float(i) for i in xrange(1, N + 1)])
Y = cumsum(X, axis=0)

#Ave_T = Y/T
Ave_T = array([Y[i, :, :] / T[i] for i in range(N)])

S_T = zeros((N, shape[1], shape[2]))
R_T = zeros((N, shape[1], shape[2]))
for i in xrange(N):
    S_T[i, :, :] = std(X[:i + 1, :, :], axis=0)
    X_T = Y - array([T[j] * Ave_T[i, :, :] for j in range(N)])
    R_T[i, :, :] = nanmax(X_T[:i + 1, :, :], axis=0) - \
        nanmin(X_T[:i + 1, :, :], axis=0)

R_S = R_T / S_T
#R_S = array([R_T[i] / S_T[i] for i in range(N)])

R_S = log(R_S)
n = log(T).reshape(N, 1)
R_S = R_S.reshape(N, shape[1] * shape[2])

H = lstsq(n[1:], R_S[1:, :])[0]
hurst = H
hurst = hurst.reshape(755, 1217)

hurst = arcpy.NumPyArrayToRaster(hurst, x_cell_size=0.0059,
                                 y_cell_size=0.0059,
                                 lower_left_corner=arcpy.Point(
                                     104.480773, 21.5954289997),
                                 value_to_nodata=-100.0)
hurst.save(r'H:\RS\hurst\hurst21.img')

print 'done'
