"""
This script will take the users name, destination, origin, and date of flight.

It will make an email based on this data.

A discount will only be granted if the flight is not tomorrow.

The discount will be the % of seats remaining, capped at 45%

"""

import tkinter as tk


root = tk.Tk()
root.geometry('500x500')
font = 'Arial'


def fixed_items():
    """
    This def will take no arguments
    
    It will set up the gui screen with boxes for adding 
    name, origin, destination, and date.
    
    """
    #init variables
    destChoices = ['Hamilton', 'Rotorua', 'Auckland']
    name = tk.StringVar()
    origin = tk.StringVar()
    dest = tk.StringVar()
    date = tk.StringVar()
    
    #title    
    title = tk.Label(root, text='Flight details', font=(font, 17))
    
    #name label and entry
    nameL = tk.Label(root, text='Flyer Name:', font=(font, 12))
    nameE = tk.Entry(root, textvariable=name, font=(font, 12))
    
    #origin and dest entries
    insideO = tk.StringVar()
    insideD = tk.StringVar()
    insideO.set('Select Location')
    insideD.set('Select Location')
    
    #'to' label
    tk.Label(root, text='to').grid(row=2, column=1, padx=5)
    
    originE = tk.OptionMenu(root, insideO, *destChoices)
    destE = tk.OptionMenu(root, insideD, *destChoices)
    
    
    originE.grid(row=2, column=0)

    destE.grid(row=2, column=2, sticky='W')

    
    
    
    
    
    title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
    nameL.grid(row=1, column=0, padx=10, pady=5)    
    nameE.grid(row=1, column=2, pady=5)


fixed_items()
root.mainloop()
