import PySimpleGUI as sg
import numpy as np
import Game
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

figlist=[]
Fast = False

layout =[ [sg.Text('Number of players'), sg.InputText()],
        [sg.Text('Amount of games'), sg.InputText()],
        [sg.Text('idfk'), sg.InputText()],
        [sg.Button('Normal'), sg.Button('Fast'), sg.Button('Slow'),
         sg.Button('Redraw graph')], [sg.Canvas(key='plot')]]

window = sg.Window('window title', layout, finalize=True)
def Graph():
    fig,ax=plt.subplots()
    x = np.linspace(0,1000,1000)
    for idx,data in enumerate(Game.startsimulator(Fast)):
        ax.plot(x,data,label='player{}'.format(idx))
    plt.legend()
    figcan=FigureCanvasTkAgg(fig,window['plot'].TKCanvas)
    figcan.draw()
    figcan.get_tk_widget().pack(side='top',fill='both',expand=1)
    figlist.append(figcan)

Graph()
while True:
    event, values  = window.read()
    print(event, values)
    match event:
        case 'Fast':
            Fast = not Fast
        case 'Redraw graph':
            figlist[0].get_tk_widget().forget()
            figlist.remove(figlist[0])
            Graph()
        case 'Normal':
            Fast = False
        case 'Exit window' | sg.WIN_CLOSED:
            break


window.close()