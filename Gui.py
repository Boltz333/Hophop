import PySimpleGUI as sg
import numpy as np
import Game
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

figlist=[]
Fast = False
Slow = False
#layot og the window

layout =[ [sg.Text('Number of players'), sg.InputText(key = 'input Number of players')],
        [sg.Text('Amount of games'), sg.InputText(key = 'input Amount of games')],
        [sg.Button('Normal'), sg.Button('Fast'), sg.Button('Slow'),
         sg.Button('Redraw graph')], [sg.Canvas(key='plot')]]



window = sg.Window('window title', layout, finalize=True)

#the graph
def Graph(Numer_players, Number_of_simulations, Fast, Slow):
    fig,ax=plt.subplots()
    x = np.linspace(0,Number_of_simulations,Number_of_simulations)
    for idx,data in enumerate(Game.startsimulator(Fast, Slow, Numer_players, Number_of_simulations)):
        ax.plot(x,data,label=f'player {idx +1}')
    plt.legend()
    figcan=FigureCanvasTkAgg(fig,window['plot'].TKCanvas)
    figcan.draw()
    figcan.get_tk_widget().pack(side='top',fill='both',expand=1)
    figlist.append(figcan)

#gamemode control if you press button and redraw graphs
while True:
    event, values  = window.read()
    print(event, values)
    match event:
        case 'Fast':
            Fast = not Fast
        case 'Normal':
            Fast = False
            Slow = False
        case 'Slow':
            Slow = not Slow
       

    if event == 'Redraw graph':
            try:
                Numer_players = int(values['input Number of players'])
                Number_of_simulations = int(values['input Amount of games'])
            except ValueError:
                sg.popup('Type correct')
                continue
            if figlist:
                figlist[0].get_tk_widget().forget()
                figlist.clear()
            Graph(Numer_players, Number_of_simulations, Fast, Slow)

    print(values['input Amount of games'])



window.close()