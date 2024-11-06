import PySimpleGUI as sg
import numpy as np
import Game
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
Game.startsimulator()

layout =[ [sg.Text('Number of players'), sg.InputText()],
        [sg.Text('Amount of games'), sg.InputText()],
        [sg.Text('idfk'), sg.InputText()],
        [sg.Button('Normal'), sg.Button('Fast'), sg.Button('Slow')], [sg.Canvas(key='plot')]]

window = sg.Window('window title', layout, finalize=True)

fig,ax=plt.subplots()
x = np.linspace(0,1000,1000)
for idx,data in enumerate(Game.startsimulator()):
    ax.plot(x,data,label='player{}'.format(idx))
plt.legend()
figcan=FigureCanvasTkAgg(fig,window['plot'].TKCanvas)
figcan.draw()
figcan.get_tk_widget().pack(side='top',fill='both',expand=1)

while True:
    event, values  = window.read() # wait here untill somthing happens
    print(event, values)
    # Exit the while loop when the button of close botton is pressed
    if event == "Exit window" or event == sg.WIN_CLOSED:
        break

window.close()