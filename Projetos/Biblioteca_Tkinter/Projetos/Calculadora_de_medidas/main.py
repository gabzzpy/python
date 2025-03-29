from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

# Colors
black = '#000000'
white = '#FFFFFF'
red = '#FF0000'
hyper_light_red = '#f5e9e9'
green = '#00FF00'
blue = '#0000FF'
light_blue = '#3967c4'
light_gray = '#464f6b'
yellow = '#FFFF00'
gray = '#a8b1bf'
orange = '#ff9f73'
purple = '#800080'

# Window
window = Tk()
window.title('Calculator')
# window.iconphoto()
window.geometry('800x450')
window.config(bg=white)
window.resizable(False,False)

# Functions
convertion = {
    'mass': [['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'], [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
    'time': [], #[['year', 'month', 'day', 'hour', 'minute', 'second'], [1, 12, 365, 8760, 525600, 31536000]],
    'length': [['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'], [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
    'area': [['km2', 'hm2', 'dam2', 'm2', 'dm2', 'cm2', 'mm2'], [0.000001, 0.0001, 0.01, 1, 100, 10000, 1000000]],
    'quantity': [['kl', 'hl', 'dal', 'l', 'dl', 'cl', 'ml'], [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
    'speed': [['m/s', 'km/h'], [1, 3.6]],
    'temperature': [['kg', 'hg', 'dag', 'g', 'dg', 'cg', 'mg'], [0.001, 0.01, 0.1, 1, 10, 100, 1000]],
        #'energy': {},
        #'pressure': {}
    }

def main(information_unit):
    def calculate():
        if entrance_value.get() == 'tesao':
            label_result['text'] = '+ de 8000.0'
        else:
            list_of_numbers = convertion[f'{information_unit}'][1]
            list_of_units = convertion[f'{information_unit}'][0]

            index_from = list_of_units.index(combox_from.get())   
            index_to = list_of_units.index(combox_to.get())  

            result = int(entrance_value.get()) / list_of_numbers[index_from] * list_of_numbers[index_to]

            label_result['text']=f'{result:.6f} {combox_to.get()}'

    calculate_button = Button(frame_right,text='Calculate',fg=black,bg=orange,font='Ivy 15 bold',command=calculate)
    calculate_button.place(x=160, y=265)


    global convertion

    frame_right.place(x=530,y=0)

    top_label_right['text'] = f'{information_unit.title()}'
    combox_from['values'] = combox_to['values'] = convertion[f'{information_unit}'][0]


# Frame's Layout
frame_left = Frame(bg=light_gray,width=530,height=450)
frame_left.place(x=0,y=0)

frame_right= Frame(bg=white,width=270,height=450)

# Label's Organization
top_label_left = Label(frame_left,bg=white,text='Unit Conversion Calculator',width=25,height=2,font='Ivy 26 bold',anchor=CENTER,fg=light_gray,relief=SOLID)
top_label_left.place(x=0,y=0)

top_label_right = Label(frame_right,bg=white,text='',width=13,height=2,font='Ivy 26 bold',anchor=CENTER,fg=light_gray,relief='sunken')
top_label_right.place(x=0,y=0)

label_result = Label(frame_right,bg=white,text='',width=13,height=2,font='Ivy 18 bold',anchor=CENTER,fg=light_gray,relief='ridge')
label_result.place(x=30,y=340)

word_from = Label(frame_right,bg=white,text='From',width=5,height=1,font='Ivy 11 bold',anchor=CENTER,fg=light_gray,relief='ridge')
word_from.place(x=5,y=140)

word_to = Label(frame_right,bg=white,text='to',width=5,height=1,font='Ivy 11 bold',anchor=CENTER,fg=light_gray,relief='ridge')
word_to.place(x=140,y=140)

# Images
list_pngs = ['Projetos/Calculadora_de_medidas/mass.png',
    'Projetos/Calculadora_de_medidas/time.png',
    'Projetos/Calculadora_de_medidas/temperature.png',
    'Projetos/Calculadora_de_medidas/speed.png',
    'Projetos/Calculadora_de_medidas/quantity.png',
    'Projetos/Calculadora_de_medidas/pressure.png',
    'Projetos/Calculadora_de_medidas/lenght.png',
    'Projetos/Calculadora_de_medidas/energy.png',
    'Projetos/Calculadora_de_medidas/area.png']

list_names=['mass','time','temperature','speed','quantity','pressure','length','energy','area']
all_in_one = {}
for value in list_pngs:
    img = Image.open(value)
    img = img.resize((50,50), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    all_in_one[list_names[list_pngs.index(value)]] = img


# Button's Organization
mass_button = Button(frame_left,width=150,height=60,bg=light_blue,image=all_in_one['mass'],text='Mass',font='Ivy 16 bold',compound=LEFT,relief=SOLID,fg=white,command=lambda:main('mass'))
mass_button.place(x=15,y=120)

time_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Time',image=all_in_one['time'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:main('time'))
time_button.place(x=185,y=120)

length_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Length',image=all_in_one['length'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:main('length'))
length_button.place(x=355,y=120)

area_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Area',image=all_in_one['area'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:main('area'))
area_button.place(x=15,y=240)

quantity_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Quantity',image=all_in_one['quantity'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:main('quantity'))
quantity_button.place(x=185,y=240)

speed_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Speed',image=all_in_one['speed'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:main('speed'))
speed_button.place(x=355,y=240)

#temperature_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Temperature',image=all_in_one['temperature'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:main('temperature'))
#temperature_button.place(x=15,y=360)

#energy_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Energy',image=all_in_one['energy'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:)
#energy_button.place(x=185,y=360)

#pressure_button = Button(frame_left,width=150,height=60,bg=light_blue,text='Pressure',image=all_in_one['pressure'],compound=LEFT,font='Ivy 16 bold',relief=SOLID,fg=white,command=lambda:)
#pressure_button.place(x=355,y=360)


# Entry's Layout
entrance_value = Entry(frame_right,font='Ivy 15 bold',width=10,relief='raised')
entrance_value.place(x=30, y=275)

# Combox's Layout

combox_from = ttk.Combobox(frame_right,font='Ivy 11 bold',width=5)
combox_from.place(x=65,y=140)

combox_to = ttk.Combobox(frame_right,font='Ivy 11 bold',width=5)
combox_to.place(x=200,y=140)

# Loop
window.mainloop()