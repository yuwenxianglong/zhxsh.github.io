# -*- coding: utf-8 -*-
"""
@Project : plotDosBS
@Author  : Xu-Shan Zhao
@Filename: plotDosBS202005081358.py
@IDE     : PyCharm
@Time1   : 2020-05-08 13:58:56
@Time2   : 2020/5/8 13:58
@Month1  : 5月
@Month2  : 五月
"""

from pymatgen.io.vasp import Vasprun, BSVasprun
from pymatgen.electronic_structure.core import Spin, OrbitalType

import chart_studio.plotly as pltly
import chart_studio.tools as tls
import plotly.graph_objs as go

# chart_studio.tools.set_credentials_file(username='yuwenxianglong', api_key='YbYbBzHWn0IVxHZyLM73')

dosrun = Vasprun('AlEuO3_Perovskite_DOS/vasprun.xml')
spd_dos = dosrun.complete_dos.get_spd_dos()

trace_tdos = go.Scatter(
    y=dosrun.tdos.densities[Spin.up],
    x=dosrun.tdos.energies - dosrun.efermi,
    mode='lines',
    name='Total DOS',
    line=dict(
        color='#444444'
    ),
    fill='tozeroy'
)

# 3s contribution to the total DOS
trace_3s = go.Scatter(
    y=spd_dos[OrbitalType.s].densities[Spin.up],
    x=dosrun.tdos.energies - dosrun.efermi,
    mode="lines",
    name="3s",
    line=dict(color="red")
)

# 3p contribution to the total DOS
trace_3p = go.Scatter(
    y=spd_dos[OrbitalType.p].densities[Spin.up],
    x=dosrun.tdos.energies - dosrun.efermi,
    mode="lines",
    name="3p",
    line=dict(color="green")
)

# 3d contribution to the total DOS
trace_3d = go.Scatter(
    y=spd_dos[OrbitalType.d].densities[Spin.up],
    x=dosrun.tdos.energies - dosrun.efermi,
    mode="lines",
    name="3d",
    line=dict(color="blue")
)

# dosdata = go.Data([trace_tdos, trace_3s, trace_3p])
dosdata = [trace_tdos, trace_3s, trace_3p, trace_3d]

dosyaxis = go.layout.YAxis(
    title="<b> Density of states <b>",
    titlefont=dict(
        size=22,
        family="Times New Roman"
    ),
    showgrid=True,
    showline=True,
    # range=[.01, 3],
    mirror="ticks",
    ticks="inside",
    tickfont=dict(
        size=22,
        family='Times New Roman'
    ),
    linewidth=2,
    tickwidth=2
)
dosxaxis = go.layout.XAxis(
    title="$E - E_f \quad / \quad \\text{eV}$",
    titlefont=dict(
        size=20,
        family='Times New Roman'
    ),
    showgrid=True,
    showline=True,
    ticks="inside",
    tickfont=dict(
        size=22,
        family='Times New Roman'
    ),
    mirror='ticks',
    linewidth=2,
    tickwidth=2,
    zerolinewidth=2
)
doslayout = go.Layout(
    title="<b> Density of states of AlEuO3 <b>",
    titlefont=dict(
        size=26,
        family='Times New Roman'
    ),
    xaxis=dosxaxis,
    yaxis=dosyaxis,
    width=1920,
    height=600
)

dosfig = go.Figure(data=dosdata, layout=doslayout)
dosfig.update_layout(legend=dict(
    x=0.88,
    y=0.88,
    traceorder="normal",
    font=dict(
        family="Times New Roman",
        size=22,
        color='black'
    ),
    bgcolor='LightSteelBlue',  # set backgroud color
    bordercolor='yellow',  # set border color 框线颜色
    borderwidth=2,
))
plot_url = pltly.plot(dosfig, filename="DOS_AlEuO3", auto_open=True)
print(tls.get_embed(plot_url))

import plotly
plotly.io.write_image(dosfig, 'DOS_AlEuO3.jpeg')
