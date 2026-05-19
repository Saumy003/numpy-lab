""" Topic 7. Meshgrids """

import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

#ploting 3D graphs

#meshgrid
a = np.linspace(-10, 9, 20)
b = np.linspace(-10, 9, 20)

xx, yy = np.meshgrid(a, b)


plt.scatter(xx, yy)
plt.show()


def func(x, y):
    return x**2 + y**2

zz = func(xx, yy)


# to print 3D graphs we are using plotly

fig = px.scatter_3d()
fig.add_trace(go.Surface(x = xx,y = yy, z = zz))

fig.show()