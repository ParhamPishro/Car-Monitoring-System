#971813080

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random
import json
import math

cars = []
paths = []
car = {}
position = {}
positions = []
position_fake = []


def donothing():
    pass


def speed_def():
    global speed, max_s, min_s, distance
    speed = []
    max_s = []
    min_s = []
    distance = []
    for i in range (int(car_spin.get())):
        first_point = (cars[i]['position']['lat'] , cars[i]['position']['long'])
        v = []
        up = 0
        down = 2
        d = []
        for j in range (1,int(point_spin.get())):
            a = (position_fake[i][j-1]['lat'] , position_fake[i][j-1]['long'])
            b = (position_fake[i][j]['lat'] , position_fake[i][j]['long'])
            v.append(round(math.dist(a,b) , 3))
            up = max(v[j-1] , up)
            down = min(v[j-1] , down)
            d.append(round(math.dist(first_point,a) , 5))
        speed.append(v)
        max_s.append(up)
        min_s.append(down)
        distance.append(d)


def add_car():
    car['name'] = name_entry.get()
    car['company'] = company_entry.get()
    try:
        car['year'] = int(year_entry.get())
    except ValueError:
        messagebox.showerror('YEAR ERROR!','You must keyboard the integer number...')
    try:
        position['lat'] = float(lat_entry.get())
    except ValueError:
        messagebox.showerror('LAT ERROR!','You must keyboard the integer or float number...')
    else:
        if (position['lat'] > 90 or position['lat'] < -90):
            messagebox.showwarning('LAT ERROR!','The latitude must be between -90 & 90...')
    try:
        position['long'] = float(long_entry.get())
    except ValueError:
        messagebox.showerror('LONG ERROR!','You must keyboard the integer or float number...')
    else:
        if (position['long'] > 180 or position['long'] < -180):
            messagebox.showwarning('LONG ERROR!','The longitude must be between -180 & 180...')

    point = []
    position_real = position.copy()
    positions.append(position_real)
    point.append(position_real.copy())
    position_fake.append(point)
    position_car = position_real.copy()
    car['position'] = position_car
    car_real = car.copy()
    cars.append(car_real)
    
    if len(cars) == int(car_spin.get()):
        create_button.config(state='active')
        add_button.config(state='disable')

    if(position['lat'] <= 90 and position['lat'] >= -90 and position['long'] <= 180 and position['long'] >= -180):
        added_pb.config(var = added_pb.step(1))
    else:
        cars.pop()

def create_database():
    path = []
    for i in range (int(car_spin.get())):
        position = positions[i]
        for j in range (1, int(point_spin.get())):
            rand_x = random.uniform(-1,1)
            rand_y = random.uniform(-1,1)
            position['lat'] += rand_x
            position['long'] += rand_y
            point = {}
            point['lat'] = position_fake[i][j-1]['lat'] + rand_x
            point['long'] = position_fake[i][j-1]['long'] + rand_y
            position_fake[i].append(point)
            
            if (position['lat'] > 90):
                x = position['lat'] - 90
                position['lat'] = 90 - x
                if (position['long'] > 0):
                    position['long'] -= 180
                else:
                    position['long'] += 180

            elif (position['lat'] < -90):
                x = - position['lat'] - 90
                position['lat'] = - 90 + x
                if (position['long'] > 0):
                    position['long'] -= 180
                else:
                    position['long'] += 180

            if (position['long'] > 180):
                y = position['long'] - 180
                position['long'] = -180 + y

            elif (position['long'] < -180):
                y = - position['long'] - 180
                position['long'] = 180 - y

            position_real = position.copy()
            path.append(position_real)
            path_real = path.copy()
            
        paths.append(path_real)
        path = []

    with open('car-dataset.json', 'w+') as file:
        json.dump(cars, file)
        json.dump(paths, file)

    speed_def()
    messagebox.showinfo('Dataset', 'Dataset created successfully')


def start(delay=1):
    global j, J
    for j in range(J, int(point_spin.get())):
        lat_en1.delete(0,END)
        lat_en1.insert(-1 ,str(paths[0][j-1]['lat']))
        lat_en1.update()
        long_en1.delete(0,END)
        long_en1.insert(-1 ,str(paths[0][j-1]['long']))
        long_en1.update()
        
        lat_en2.delete(0,END)
        lat_en2.insert(-1 ,str(paths[1][j-1]['lat']))
        lat_en2.update()
        long_en2.delete(0,END)
        long_en2.insert(-1 ,str(paths[1][j-1]['long']))
        long_en2.update()
        
        lat_en3.delete(0,END)
        lat_en3.insert(-1 ,str(paths[2][j-1]['lat']))
        lat_en3.update()
        long_en3.delete(0,END)
        long_en3.insert(-1 ,str(paths[2][j-1]['long']))
        long_en3.update()
        
        lat_en4.delete(0,END)
        lat_en4.insert(-1 ,str(paths[3][j-1]['lat']))
        lat_en4.update()
        long_en4.delete(0,END)
        long_en4.insert(-1 ,str(paths[3][j-1]['long']))
        long_en4.update()
        
        lat_en5.delete(0,END)
        lat_en5.insert(-1 ,str(paths[4][j-1]['lat']))
        lat_en5.update()
        long_en5.delete(0,END)
        long_en5.insert(-1 ,str(paths[4][j-1]['long']))
        long_en5.update()
        
        lat_en6.delete(0,END)
        lat_en6.insert(-1 ,str(paths[5][j-1]['lat']))
        lat_en6.update()
        long_en6.delete(0,END)
        long_en6.insert(-1 ,str(paths[5][j-1]['long']))
        long_en6.update()
        
        lat_en7.delete(0,END)
        lat_en7.insert(-1 ,str(paths[6][j-1]['lat']))
        lat_en7.update()
        long_en7.delete(0,END)
        long_en7.insert(-1 ,str(paths[6][j-1]['long']))
        long_en7.update()
        
        lat_en8.delete(0,END)
        lat_en8.insert(-1 ,str(paths[7][j-1]['lat']))
        lat_en8.update()
        long_en8.delete(0,END)
        long_en8.insert(-1 ,str(paths[7][j-1]['long']))
        long_en8.update()
        
        lat_en9.delete(0,END)
        lat_en9.insert(-1 ,str(paths[8][j-1]['lat']))
        lat_en9.update()
        long_en9.delete(0,END)
        long_en9.insert(-1 ,str(paths[8][j-1]['long']))
        long_en9.update()
        
        lat_en10.delete(0,END)
        lat_en10.insert(-1 ,str(paths[9][j-1]['lat']))
        lat_en10.update()
        long_en10.delete(0,END)
        long_en10.insert(-1 ,str(paths[9][j-1]['long']))
        long_en10.update()

        speed_en1.delete(0,END)
        speed_en1.insert(-1, str(speed[0][j-1]))
        speed_en1.update()
        speed_en2.delete(0,END)
        speed_en2.insert(-1, str(speed[1][j-1]))
        speed_en2.update()
        speed_en3.delete(0,END)
        speed_en3.insert(-1, str(speed[2][j-1]))
        speed_en3.update()
        speed_en4.delete(0,END)
        speed_en4.insert(-1, str(speed[3][j-1]))
        speed_en4.update()
        speed_en5.delete(0,END)
        speed_en5.insert(-1, str(speed[4][j-1]))
        speed_en5.update()
        speed_en6.delete(0,END)
        speed_en6.insert(-1, str(speed[5][j-1]))
        speed_en6.update()
        speed_en7.delete(0,END)
        speed_en7.insert(-1, str(speed[6][j-1]))
        speed_en7.update()
        speed_en8.delete(0,END)
        speed_en8.insert(-1, str(speed[7][j-1]))
        speed_en8.update()
        speed_en9.delete(0,END)
        speed_en9.insert(-1, str(speed[8][j-1]))
        speed_en9.update()
        speed_en10.delete(0,END)
        speed_en10.insert(-1, str(speed[9][j-1]))
        speed_en10.update()

        if speed[0][j-1] == max_s[0]:
            max_en1.delete(0,END)
            max_en1.insert(-1, str(max_s[0]))
            max_en1.update()        
        if speed[1][j-1] == max_s[1]:
            max_en2.delete(0,END)
            max_en2.insert(-1, str(max_s[1]))
            max_en2.update()        
        if speed[2][j-1] == max_s[2]:
            max_en3.delete(0,END)
            max_en3.insert(-1, str(max_s[2]))
            max_en3.update()        
        if speed[3][j-1] == max_s[3]:
            max_en4.delete(0,END)
            max_en4.insert(-1, str(max_s[3]))
            max_en4.update()        
        if speed[4][j-1] == max_s[4]:
            max_en5.delete(0,END)
            max_en5.insert(-1, str(max_s[4]))
            max_en5.update()        
        if speed[5][j-1] == max_s[5]:
            max_en6.delete(0,END)
            max_en6.insert(-1, str(max_s[5]))
            max_en6.update()        
        if speed[6][j-1] == max_s[6]:
            max_en7.delete(0,END)
            max_en7.insert(-1, str(max_s[6]))
            max_en7.update()
        if speed[7][j-1] == max_s[7]:
            max_en8.delete(0,END)
            max_en8.insert(-1, str(max_s[7]))
            max_en8.update()
        if speed[8][j-1] == max_s[8]:
            max_en9.delete(0,END)
            max_en9.insert(-1, str(max_s[8]))
            max_en9.update()
        if speed[9][j-1] == max_s[9]:
            max_en10.delete(0,END)
            max_en10.insert(-1, str(max_s[9]))
            max_en10.update()

        if speed[0][j-1] == min_s[0]:
            min_en1.delete(0,END)
            min_en1.insert(-1, str(min_s[0]))
            min_en1.update()        
        if speed[1][j-1] == min_s[1]:
            min_en2.delete(0,END)
            min_en2.insert(-1, str(min_s[1]))
            min_en2.update()        
        if speed[2][j-1] == min_s[2]:
            min_en3.delete(0,END)
            min_en3.insert(-1, str(min_s[2]))
            min_en3.update()        
        if speed[3][j-1] == min_s[3]:
            min_en4.delete(0,END)
            min_en4.insert(-1, str(min_s[3]))
            min_en4.update()        
        if speed[4][j-1] == min_s[4]:
            min_en5.delete(0,END)
            min_en5.insert(-1, str(min_s[4]))
            min_en5.update()        
        if speed[5][j-1] == min_s[5]:
            min_en6.delete(0,END)
            min_en6.insert(-1, str(min_s[5]))
            min_en6.update()        
        if speed[6][j-1] == min_s[6]:
            min_en7.delete(0,END)
            min_en7.insert(-1, str(min_s[6]))
            min_en7.update()
        if speed[7][j-1] == min_s[7]:
            min_en8.delete(0,END)
            min_en8.insert(-1, str(min_s[7]))
            min_en8.update()
        if speed[8][j-1] == min_s[8]:
            min_en9.delete(0,END)
            min_en9.insert(-1, str(min_s[8]))
            min_en9.update()
        if speed[9][j-1] == min_s[9]:
            min_en10.delete(0,END)
            min_en10.insert(-1, str(min_s[9]))
            min_en10.update()
            
        distance_lb1.config(text=str(distance[0][j-1]))
        distance_lb2.config(text=str(distance[1][j-1]))
        distance_lb3.config(text=str(distance[2][j-1]))
        distance_lb4.config(text=str(distance[3][j-1]))
        distance_lb5.config(text=str(distance[4][j-1]))
        distance_lb6.config(text=str(distance[5][j-1]))
        distance_lb7.config(text=str(distance[6][j-1]))
        distance_lb8.config(text=str(distance[7][j-1]))
        distance_lb9.config(text=str(distance[8][j-1]))
        distance_lb10.config(text=str(distance[9][j-1]))

        J = j
        time.sleep(delay)


def start_2X():
    start(0.5)


def start_4X():
    start(0.25)


def start_8X():
    start(0.125)


def start_infinity():
    start(0)

def pause():
    global j, J
    for i in range(J, 1000 * int(point_spin.get())):
        lat_en1.delete(0,END)
        lat_en1.insert(-1 ,str(paths[0][j-1]['lat']))
        lat_en1.update()
        long_en1.delete(0,END)
        long_en1.insert(-1 ,str(paths[0][j-1]['long']))
        long_en1.update()
        
        lat_en2.delete(0,END)
        lat_en2.insert(-1 ,str(paths[1][j-1]['lat']))
        lat_en2.update()
        long_en2.delete(0,END)
        long_en2.insert(-1 ,str(paths[1][j-1]['long']))
        long_en2.update()
        
        lat_en3.delete(0,END)
        lat_en3.insert(-1 ,str(paths[2][j-1]['lat']))
        lat_en3.update()
        long_en3.delete(0,END)
        long_en3.insert(-1 ,str(paths[2][j-1]['long']))
        long_en3.update()
        
        lat_en4.delete(0,END)
        lat_en4.insert(-1 ,str(paths[3][j-1]['lat']))
        lat_en4.update()
        long_en4.delete(0,END)
        long_en4.insert(-1 ,str(paths[3][j-1]['long']))
        long_en4.update()
        
        lat_en5.delete(0,END)
        lat_en5.insert(-1 ,str(paths[4][j-1]['lat']))
        lat_en5.update()
        long_en5.delete(0,END)
        long_en5.insert(-1 ,str(paths[4][j-1]['long']))
        long_en5.update()
        
        lat_en6.delete(0,END)
        lat_en6.insert(-1 ,str(paths[5][j-1]['lat']))
        lat_en6.update()
        long_en6.delete(0,END)
        long_en6.insert(-1 ,str(paths[5][j-1]['long']))
        long_en6.update()
        
        lat_en7.delete(0,END)
        lat_en7.insert(-1 ,str(paths[6][j-1]['lat']))
        lat_en7.update()
        long_en7.delete(0,END)
        long_en7.insert(-1 ,str(paths[6][j-1]['long']))
        long_en7.update()
        
        lat_en8.delete(0,END)
        lat_en8.insert(-1 ,str(paths[7][j-1]['lat']))
        lat_en8.update()
        long_en8.delete(0,END)
        long_en8.insert(-1 ,str(paths[7][j-1]['long']))
        long_en8.update()
        
        lat_en9.delete(0,END)
        lat_en9.insert(-1 ,str(paths[8][j-1]['lat']))
        lat_en9.update()
        long_en9.delete(0,END)
        long_en9.insert(-1 ,str(paths[8][j-1]['long']))
        long_en9.update()
        
        lat_en10.delete(0,END)
        lat_en10.insert(-1 ,str(paths[9][j-1]['lat']))
        lat_en10.update()
        long_en10.delete(0,END)
        long_en10.insert(-1 ,str(paths[9][j-1]['long']))
        long_en10.update()

        speed_en1.delete(0,END)
        speed_en1.insert(-1, str(speed[0][j-1]))
        speed_en1.update()
        speed_en2.delete(0,END)
        speed_en2.insert(-1, str(speed[1][j-1]))
        speed_en2.update()
        speed_en3.delete(0,END)
        speed_en3.insert(-1, str(speed[2][j-1]))
        speed_en3.update()
        speed_en4.delete(0,END)
        speed_en4.insert(-1, str(speed[3][j-1]))
        speed_en4.update()
        speed_en5.delete(0,END)
        speed_en5.insert(-1, str(speed[4][j-1]))
        speed_en5.update()
        speed_en6.delete(0,END)
        speed_en6.insert(-1, str(speed[5][j-1]))
        speed_en6.update()
        speed_en7.delete(0,END)
        speed_en7.insert(-1, str(speed[6][j-1]))
        speed_en7.update()
        speed_en8.delete(0,END)
        speed_en8.insert(-1, str(speed[7][j-1]))
        speed_en8.update()
        speed_en9.delete(0,END)
        speed_en9.insert(-1, str(speed[8][j-1]))
        speed_en9.update()
        speed_en10.delete(0,END)
        speed_en10.insert(-1, str(speed[9][j-1]))
        speed_en10.update()

        if speed[0][j-1] == max_s[0]:
            max_en1.delete(0,END)
            max_en1.insert(-1, str(max_s[0]))
            max_en1.update()        
        if speed[1][j-1] == max_s[1]:
            max_en2.delete(0,END)
            max_en2.insert(-1, str(max_s[1]))
            max_en2.update()        
        if speed[2][j-1] == max_s[2]:
            max_en3.delete(0,END)
            max_en3.insert(-1, str(max_s[2]))
            max_en3.update()        
        if speed[3][j-1] == max_s[3]:
            max_en4.delete(0,END)
            max_en4.insert(-1, str(max_s[3]))
            max_en4.update()        
        if speed[4][j-1] == max_s[4]:
            max_en5.delete(0,END)
            max_en5.insert(-1, str(max_s[4]))
            max_en5.update()        
        if speed[5][j-1] == max_s[5]:
            max_en6.delete(0,END)
            max_en6.insert(-1, str(max_s[5]))
            max_en6.update()        
        if speed[6][j-1] == max_s[6]:
            max_en7.delete(0,END)
            max_en7.insert(-1, str(max_s[6]))
            max_en7.update()
        if speed[7][j-1] == max_s[7]:
            max_en8.delete(0,END)
            max_en8.insert(-1, str(max_s[7]))
            max_en8.update()
        if speed[8][j-1] == max_s[8]:
            max_en9.delete(0,END)
            max_en9.insert(-1, str(max_s[8]))
            max_en9.update()
        if speed[9][j-1] == max_s[9]:
            max_en10.delete(0,END)
            max_en10.insert(-1, str(max_s[9]))
            max_en10.update()

        if speed[0][j-1] == min_s[0]:
            min_en1.delete(0,END)
            min_en1.insert(-1, str(min_s[0]))
            min_en1.update()        
        if speed[1][j-1] == min_s[1]:
            min_en2.delete(0,END)
            min_en2.insert(-1, str(min_s[1]))
            min_en2.update()        
        if speed[2][j-1] == min_s[2]:
            min_en3.delete(0,END)
            min_en3.insert(-1, str(min_s[2]))
            min_en3.update()        
        if speed[3][j-1] == min_s[3]:
            min_en4.delete(0,END)
            min_en4.insert(-1, str(min_s[3]))
            min_en4.update()        
        if speed[4][j-1] == min_s[4]:
            min_en5.delete(0,END)
            min_en5.insert(-1, str(min_s[4]))
            min_en5.update()        
        if speed[5][j-1] == min_s[5]:
            min_en6.delete(0,END)
            min_en6.insert(-1, str(min_s[5]))
            min_en6.update()        
        if speed[6][j-1] == min_s[6]:
            min_en7.delete(0,END)
            min_en7.insert(-1, str(min_s[6]))
            min_en7.update()
        if speed[7][j-1] == min_s[7]:
            min_en8.delete(0,END)
            min_en8.insert(-1, str(min_s[7]))
            min_en8.update()
        if speed[8][j-1] == min_s[8]:
            min_en9.delete(0,END)
            min_en9.insert(-1, str(min_s[8]))
            min_en9.update()
        if speed[9][j-1] == min_s[9]:
            min_en10.delete(0,END)
            min_en10.insert(-1, str(min_s[9]))
            min_en10.update()
            
        distance_lb1.config(text=str(distance[0][j-1]))
        distance_lb2.config(text=str(distance[1][j-1]))
        distance_lb3.config(text=str(distance[2][j-1]))
        distance_lb4.config(text=str(distance[3][j-1]))
        distance_lb5.config(text=str(distance[4][j-1]))
        distance_lb6.config(text=str(distance[5][j-1]))
        distance_lb7.config(text=str(distance[6][j-1]))
        distance_lb8.config(text=str(distance[7][j-1]))
        distance_lb9.config(text=str(distance[8][j-1]))
        distance_lb10.config(text=str(distance[9][j-1]))

        J = j
    

def restart():
    global j, J
    j = 1
    J = 1
    for j in range(J, int(point_spin.get())):
        lat_en1.delete(0,END)
        lat_en1.insert(-1 ,str(paths[0][j-1]['lat']))
        lat_en1.update()
        long_en1.delete(0,END)
        long_en1.insert(-1 ,str(paths[0][j-1]['long']))
        long_en1.update()
        
        lat_en2.delete(0,END)
        lat_en2.insert(-1 ,str(paths[1][j-1]['lat']))
        lat_en2.update()
        long_en2.delete(0,END)
        long_en2.insert(-1 ,str(paths[1][j-1]['long']))
        long_en2.update()
        
        lat_en3.delete(0,END)
        lat_en3.insert(-1 ,str(paths[2][j-1]['lat']))
        lat_en3.update()
        long_en3.delete(0,END)
        long_en3.insert(-1 ,str(paths[2][j-1]['long']))
        long_en3.update()
        
        lat_en4.delete(0,END)
        lat_en4.insert(-1 ,str(paths[3][j-1]['lat']))
        lat_en4.update()
        long_en4.delete(0,END)
        long_en4.insert(-1 ,str(paths[3][j-1]['long']))
        long_en4.update()
        
        lat_en5.delete(0,END)
        lat_en5.insert(-1 ,str(paths[4][j-1]['lat']))
        lat_en5.update()
        long_en5.delete(0,END)
        long_en5.insert(-1 ,str(paths[4][j-1]['long']))
        long_en5.update()
        
        lat_en6.delete(0,END)
        lat_en6.insert(-1 ,str(paths[5][j-1]['lat']))
        lat_en6.update()
        long_en6.delete(0,END)
        long_en6.insert(-1 ,str(paths[5][j-1]['long']))
        long_en6.update()
        
        lat_en7.delete(0,END)
        lat_en7.insert(-1 ,str(paths[6][j-1]['lat']))
        lat_en7.update()
        long_en7.delete(0,END)
        long_en7.insert(-1 ,str(paths[6][j-1]['long']))
        long_en7.update()
        
        lat_en8.delete(0,END)
        lat_en8.insert(-1 ,str(paths[7][j-1]['lat']))
        lat_en8.update()
        long_en8.delete(0,END)
        long_en8.insert(-1 ,str(paths[7][j-1]['long']))
        long_en8.update()
        
        lat_en9.delete(0,END)
        lat_en9.insert(-1 ,str(paths[8][j-1]['lat']))
        lat_en9.update()
        long_en9.delete(0,END)
        long_en9.insert(-1 ,str(paths[8][j-1]['long']))
        long_en9.update()
        
        lat_en10.delete(0,END)
        lat_en10.insert(-1 ,str(paths[9][j-1]['lat']))
        lat_en10.update()
        long_en10.delete(0,END)
        long_en10.insert(-1 ,str(paths[9][j-1]['long']))
        long_en10.update()

        speed_en1.delete(0,END)
        speed_en1.insert(-1, str(speed[0][j-1]))
        speed_en1.update()
        speed_en2.delete(0,END)
        speed_en2.insert(-1, str(speed[1][j-1]))
        speed_en2.update()
        speed_en3.delete(0,END)
        speed_en3.insert(-1, str(speed[2][j-1]))
        speed_en3.update()
        speed_en4.delete(0,END)
        speed_en4.insert(-1, str(speed[3][j-1]))
        speed_en4.update()
        speed_en5.delete(0,END)
        speed_en5.insert(-1, str(speed[4][j-1]))
        speed_en5.update()
        speed_en6.delete(0,END)
        speed_en6.insert(-1, str(speed[5][j-1]))
        speed_en6.update()
        speed_en7.delete(0,END)
        speed_en7.insert(-1, str(speed[6][j-1]))
        speed_en7.update()
        speed_en8.delete(0,END)
        speed_en8.insert(-1, str(speed[7][j-1]))
        speed_en8.update()
        speed_en9.delete(0,END)
        speed_en9.insert(-1, str(speed[8][j-1]))
        speed_en9.update()
        speed_en10.delete(0,END)
        speed_en10.insert(-1, str(speed[9][j-1]))
        speed_en10.update()

        if speed[0][j-1] == max_s[0]:
            max_en1.delete(0,END)
            max_en1.insert(-1, str(max_s[0]))
            max_en1.update()        
        if speed[1][j-1] == max_s[1]:
            max_en2.delete(0,END)
            max_en2.insert(-1, str(max_s[1]))
            max_en2.update()        
        if speed[2][j-1] == max_s[2]:
            max_en3.delete(0,END)
            max_en3.insert(-1, str(max_s[2]))
            max_en3.update()        
        if speed[3][j-1] == max_s[3]:
            max_en4.delete(0,END)
            max_en4.insert(-1, str(max_s[3]))
            max_en4.update()        
        if speed[4][j-1] == max_s[4]:
            max_en5.delete(0,END)
            max_en5.insert(-1, str(max_s[4]))
            max_en5.update()        
        if speed[5][j-1] == max_s[5]:
            max_en6.delete(0,END)
            max_en6.insert(-1, str(max_s[5]))
            max_en6.update()        
        if speed[6][j-1] == max_s[6]:
            max_en7.delete(0,END)
            max_en7.insert(-1, str(max_s[6]))
            max_en7.update()
        if speed[7][j-1] == max_s[7]:
            max_en8.delete(0,END)
            max_en8.insert(-1, str(max_s[7]))
            max_en8.update()
        if speed[8][j-1] == max_s[8]:
            max_en9.delete(0,END)
            max_en9.insert(-1, str(max_s[8]))
            max_en9.update()
        if speed[9][j-1] == max_s[9]:
            max_en10.delete(0,END)
            max_en10.insert(-1, str(max_s[9]))
            max_en10.update()

        if speed[0][j-1] == min_s[0]:
            min_en1.delete(0,END)
            min_en1.insert(-1, str(min_s[0]))
            min_en1.update()        
        if speed[1][j-1] == min_s[1]:
            min_en2.delete(0,END)
            min_en2.insert(-1, str(min_s[1]))
            min_en2.update()        
        if speed[2][j-1] == min_s[2]:
            min_en3.delete(0,END)
            min_en3.insert(-1, str(min_s[2]))
            min_en3.update()        
        if speed[3][j-1] == min_s[3]:
            min_en4.delete(0,END)
            min_en4.insert(-1, str(min_s[3]))
            min_en4.update()        
        if speed[4][j-1] == min_s[4]:
            min_en5.delete(0,END)
            min_en5.insert(-1, str(min_s[4]))
            min_en5.update()        
        if speed[5][j-1] == min_s[5]:
            min_en6.delete(0,END)
            min_en6.insert(-1, str(min_s[5]))
            min_en6.update()        
        if speed[6][j-1] == min_s[6]:
            min_en7.delete(0,END)
            min_en7.insert(-1, str(min_s[6]))
            min_en7.update()
        if speed[7][j-1] == min_s[7]:
            min_en8.delete(0,END)
            min_en8.insert(-1, str(min_s[7]))
            min_en8.update()
        if speed[8][j-1] == min_s[8]:
            min_en9.delete(0,END)
            min_en9.insert(-1, str(min_s[8]))
            min_en9.update()
        if speed[9][j-1] == min_s[9]:
            min_en10.delete(0,END)
            min_en10.insert(-1, str(min_s[9]))
            min_en10.update()
            
        distance_lb1.config(text=str(distance[0][j-1]))
        distance_lb2.config(text=str(distance[1][j-1]))
        distance_lb3.config(text=str(distance[2][j-1]))
        distance_lb4.config(text=str(distance[3][j-1]))
        distance_lb5.config(text=str(distance[4][j-1]))
        distance_lb6.config(text=str(distance[5][j-1]))
        distance_lb7.config(text=str(distance[6][j-1]))
        distance_lb8.config(text=str(distance[7][j-1]))
        distance_lb9.config(text=str(distance[8][j-1]))
        distance_lb10.config(text=str(distance[9][j-1]))

        J = j
        time.sleep(1)


def map_win():
    top = Toplevel()
    top.title('Map')
    top.geometry('760x400')
    top.maxsize(width=760, height=400)
    global map0
    map0 = Canvas(top, width=760, height=400)
    map0.pack()
    for i in range(37):
        x_line = map0.create_line(i*20+20, 20, i*20+20, 380, fill='gray') 
    for i in range(19):
        y_line = map0.create_line(20, i*20+20, 740, i*20+20, fill='gray')
    x_graph = map0.create_line(10, 200, 750, 200, fill='black', width=3)
    y_graph = map0.create_line(380, 10, 380, 390, fill='black', width=3)
    x_finger1 = map0.create_line(745, 195, 750, 200, fill='black', width=3)
    x_finger2 = map0.create_line(745, 205, 750, 200, fill='black', width=3)
    y_finger1 = map0.create_line(375, 15, 380, 10, fill='black', width=3)
    y_finger2 = map0.create_line(385, 15, 380, 10, fill='black', width=3)


def map1():
    map_win()
    map_points = []
    map_points.append (2* cars[0]['position']['long']+380)
    map_points.append (-2* cars[0]['position']['lat']+200)
    map_points.append (2* paths[0][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[0][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='red')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)


def map2():
    map_win()
    map_points = []
    map_points.append (2* cars[1]['position']['long']+380)
    map_points.append (-2* cars[1]['position']['lat']+200)
    map_points.append (2* paths[1][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[1][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='orange')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map3():
    map_win()
    map_points = []
    map_points.append (2* cars[2]['position']['long']+380)
    map_points.append (-2* cars[2]['position']['lat']+200)
    map_points.append (2* paths[2][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[2][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='yellow')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map4():
    map_win()
    map_points = []
    map_points.append (2* cars[3]['position']['long']+380)
    map_points.append (-2* cars[3]['position']['lat']+200)
    map_points.append (2* paths[3][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[3][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='lime')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map5():
    map_win()
    map_points = []
    map_points.append (2* cars[4]['position']['long']+380)
    map_points.append (-2* cars[4]['position']['lat']+200)
    map_points.append (2* paths[4][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[4][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='green')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map6():
    map_win()
    map_points = []
    map_points.append (2* cars[5]['position']['long']+380)
    map_points.append (-2* cars[5]['position']['lat']+200)
    map_points.append (2* paths[5][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[5][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='cyan')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map7():
    map_win()
    map_points = []
    map_points.append (2* cars[6]['position']['long']+380)
    map_points.append (-2* cars[6]['position']['lat']+200)
    map_points.append (2* paths[6][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[6][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='blue')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map8():
    map_win()
    map_points = []
    map_points.append (2* cars[7]['position']['long']+380)
    map_points.append (-2* cars[7]['position']['lat']+200)
    map_points.append (2* paths[7][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[7][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='pink')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map9():
    map_win()
    map_points = []
    map_points.append (2* cars[8]['position']['long']+380)
    map_points.append (-2* cars[8]['position']['lat']+200)
    map_points.append (2* paths[8][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[8][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='magenta')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)

    
def map10():
    map_win()
    map_points = []
    map_points.append (2* cars[9]['position']['long']+380)
    map_points.append (-2* cars[9]['position']['lat']+200)
    map_points.append (2* paths[9][int(point_spin.get())-2]['long']+380)
    map_points.append (-2* paths[9][int(point_spin.get())-2]['lat']+200)
    line = map0.create_line(map_points, fill='purple')
    map0.itemconfig(line, width=5, arrow=LAST, joinstyle=ROUND, smooth=TRUE)
    
    
def open_playback():
    car_hd = Label(root, text='Car')
    car_hd.config(font=('Times',20,'bold'))
    car_hd.place(x=50, y=120)
    coordinates = Label(root, text='Coordinates')
    coordinates.config(font=('Times',20,'bold'))
    coordinates.place(x=135, y=120)
    speed_hd = Label(root, text='Speed')
    speed_hd.config(font=('Times',20,'bold'))
    speed_hd.place(x=320, y=120)
    max_hd = Label(root, text='-MAX')
    max_hd.config(font=('Times',18,'bold'))
    max_hd.place(x=400, y=105)
    min_hd = Label(root, text='-min')
    min_hd.config(font=('Times',18,'bold'))
    min_hd.place(x=400, y=135)
    origin_hd = Label(root, text='Origin')
    origin_hd.config(font=('Times',20,'bold'))
    origin_hd.place(x=590, y=120)
    arrow_hd = Label(root, text='===============>')
    arrow_hd.config(font=('Times',18,'bold'))
    arrow_hd.place(x=700, y=125)
    dist_hd = Label(root, text='Distance')
    dist_hd.config(font=('Times',20,'bold'))
    dist_hd.place(x=760, y=100)
    dest_hd = Label(root, text='Destination')
    dest_hd.config(font=('Times',20,'bold'))
    dest_hd.place(x=960, y=120)
    map_hd = Label(root, text='Map')
    map_hd.config(font=('Times',20,'bold'))
    map_hd.place(x=1200, y=120)
    
    for i in range (int(car_spin.get())):
        num_frame = LabelFrame(root)
        if i == 9:
            num_frame.place(x=1 , y=70*(i+1)+125)
        else:
            num_frame.place(x=8 , y=70*(i+1)+125)
        num_label = Label(num_frame, text=str(i+1))
        num_label.config(font=('mitra',16,'bold'))
        num_label.pack()
        
        name_label = Label(root, text=cars[i]['name'])
        name_label.place(x=35, y=70*(i+1)+110)

        company_label = Label(root, text=cars[i]['company'])
        company_label.place(x=35, y=70*(i+1)+130)

        year_label = Label(root, text=cars[i]['year'])
        year_label.place(x=35, y=70*(i+1)+150)

        arrow_label = Label(root, text='====================>')
        arrow_label.config(fg='blue', font=('parham',20))
        arrow_label.place(x=650, y=70*(i+1)+125)
        
        origin_label = Label(root, text='(%f,\n%f)'%(cars[i]['position']['lat'],cars[i]['position']['long']))
        origin_label.place(x=600, y=70*(i+1)+118)

        destination_label = Label(root, text='(%f,\n%f)'%(paths[i][-1]['lat'],paths[i][-1]['long']))
        destination_label.place(x=1000, y=70*(i+1)+125)

    
    position_fr1 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr1.place(x=150, y=70*1+115)
    position_fr2 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr2.place(x=150, y=70*2+115)
    position_fr3 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr3.place(x=150, y=70*3+115)
    position_fr4 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr4.place(x=150, y=70*4+115)
    position_fr5 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr5.place(x=150, y=70*5+115)
    position_fr6 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr6.place(x=150, y=70*6+115)
    position_fr7 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr7.place(x=150, y=70*7+115)
    position_fr8 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr8.place(x=150, y=70*8+115)
    position_fr9 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr9.place(x=150, y=70*9+115)
    position_fr10 = LabelFrame(root, text=' ', labelanchor='e')
    position_fr10.place(x=150, y=70*10+115)

    global lat_en1,long_en1
    lat_en1 = Entry(position_fr1, cursor='hand2')
    lat_en1.insert(-1, cars[0]['position']['lat'])
    lat_en1.pack(side='top')
    long_en1 = Entry(position_fr1, cursor='hand2')
    long_en1.insert(-1, cars[0]['position']['long'])
    long_en1.pack(side='bottom')
    global lat_en2,long_en2
    lat_en2 = Entry(position_fr2, cursor='hand2')
    lat_en2.insert(-1, cars[1]['position']['lat'])
    lat_en2.pack(side='top')
    long_en2 = Entry(position_fr2, cursor='hand2')
    long_en2.insert(-1, cars[1]['position']['long'])
    long_en2.pack(side='bottom')
    global lat_en3,long_en3
    lat_en3 = Entry(position_fr3, cursor='hand2')
    lat_en3.insert(-1, cars[2]['position']['lat'])
    lat_en3.pack(side='top')
    long_en3 = Entry(position_fr3, cursor='hand2')
    long_en3.insert(-1, cars[2]['position']['long'])
    long_en3.pack(side='bottom')
    global lat_en4,long_en4
    lat_en4 = Entry(position_fr4, cursor='hand2')
    lat_en4.insert(-1, cars[3]['position']['lat'])
    lat_en4.pack(side='top')
    long_en4 = Entry(position_fr4, cursor='hand2')
    long_en4.insert(-1, cars[3]['position']['long'])
    long_en4.pack(side='bottom')
    global lat_en5,long_en5
    lat_en5 = Entry(position_fr5, cursor='hand2')
    lat_en5.insert(-1, cars[4]['position']['lat'])
    lat_en5.pack(side='top')
    long_en5 = Entry(position_fr5, cursor='hand2')
    long_en5.insert(-1, cars[4]['position']['long'])
    long_en5.pack(side='bottom')
    global lat_en6,long_en6
    lat_en6 = Entry(position_fr6, cursor='hand2')
    lat_en6.insert(-1, cars[5]['position']['lat'])
    lat_en6.pack(side='top')
    long_en6 = Entry(position_fr6, cursor='hand2')
    long_en6.insert(-1, cars[5]['position']['long'])
    long_en6.pack(side='bottom')
    global lat_en7,long_en7
    lat_en7 = Entry(position_fr7, cursor='hand2')
    lat_en7.insert(-1, cars[6]['position']['lat'])
    lat_en7.pack(side='top')
    long_en7 = Entry(position_fr7, cursor='hand2')
    long_en7.insert(-1, cars[6]['position']['long'])
    long_en7.pack(side='bottom')
    global lat_en8,long_en8
    lat_en8 = Entry(position_fr8, cursor='hand2')
    lat_en8.insert(-1, cars[7]['position']['lat'])
    lat_en8.pack(side='top')
    long_en8 = Entry(position_fr8, cursor='hand2')
    long_en8.insert(-1, cars[7]['position']['long'])
    long_en8.pack(side='bottom')
    global lat_en9,long_en9
    lat_en9 = Entry(position_fr9, cursor='hand2')
    lat_en9.insert(-1, cars[8]['position']['lat'])
    lat_en9.pack(side='top')
    long_en9 = Entry(position_fr9, cursor='hand2')
    long_en9.insert(-1, cars[8]['position']['long'])
    long_en9.pack(side='bottom')
    global lat_en10,long_en10
    lat_en10 = Entry(position_fr10, cursor='hand2')
    lat_en10.insert(-1, cars[9]['position']['lat'])
    lat_en10.pack(side='top')
    long_en10 = Entry(position_fr10, cursor='hand2')
    long_en10.insert(-1, cars[9]['position']['long'])
    long_en10.pack(side='bottom')

    global max_en1,max_en2,max_en3,max_en4,max_en5
    global max_en6,max_en7,max_en8,max_en9,max_en10
    max_en1 = ttk.Entry(root, cursor='hand2')
    max_en1.insert(-1, '---')
    max_en1.place(x=410, y=70*1+113)
    max_en2 = ttk.Entry(root, cursor='hand2')
    max_en2.insert(-1, '---')
    max_en2.place(x=410, y=70*2+113)
    max_en3 = ttk.Entry(root, cursor='hand2')
    max_en3.insert(-1, '---')
    max_en3.place(x=410, y=70*3+113)
    max_en4 = ttk.Entry(root, cursor='hand2')
    max_en4.insert(-1, '---')
    max_en4.place(x=410, y=70*4+113)
    max_en5 = ttk.Entry(root, cursor='hand2')
    max_en5.insert(-1, '---')
    max_en5.place(x=410, y=70*5+113)
    max_en6 = ttk.Entry(root, cursor='hand2')
    max_en6.insert(-1, '---')
    max_en6.place(x=410, y=70*6+113)
    max_en7 = ttk.Entry(root, cursor='hand2')
    max_en7.insert(-1, '---')
    max_en7.place(x=410, y=70*7+113)
    max_en8 = ttk.Entry(root, cursor='hand2')
    max_en8.insert(-1, '---')
    max_en8.place(x=410, y=70*8+113)
    max_en9 = ttk.Entry(root, cursor='hand2')
    max_en9.insert(-1, '---')
    max_en9.place(x=410, y=70*9+113)
    max_en10 = ttk.Entry(root, cursor='hand2')
    max_en10.insert(-1, '---')
    max_en10.place(x=410, y=70*10+113)

    global min_en1,min_en2,min_en3,min_en4,min_en5
    global min_en6,min_en7,min_en8,min_en9,min_en10
    min_en1 = ttk.Entry(root, cursor='hand2')
    min_en1.insert(-1, '---')
    min_en1.place(x=410, y=70*1+138)
    min_en2 = ttk.Entry(root, cursor='hand2')
    min_en2.insert(-1, '---')
    min_en2.place(x=410, y=70*2+138)
    min_en3 = ttk.Entry(root, cursor='hand2')
    min_en3.insert(-1, '---')
    min_en3.place(x=410, y=70*3+138)
    min_en4 = ttk.Entry(root, cursor='hand2')
    min_en4.insert(-1, '---')
    min_en4.place(x=410, y=70*4+138)
    min_en5 = ttk.Entry(root, cursor='hand2')
    min_en5.insert(-1, '---')
    min_en5.place(x=410, y=70*5+138)
    min_en6 = ttk.Entry(root, cursor='hand2')
    min_en6.insert(-1, '---')
    min_en6.place(x=410, y=70*6+138)
    min_en7 = ttk.Entry(root, cursor='hand2')
    min_en7.insert(-1, '---')
    min_en7.place(x=410, y=70*7+138)
    min_en8 = ttk.Entry(root, cursor='hand2')
    min_en8.insert(-1, '---')
    min_en8.place(x=410, y=70*8+138)
    min_en9 = ttk.Entry(root, cursor='hand2')
    min_en9.insert(-1, '---')
    min_en9.place(x=410, y=70*9+138)
    min_en10 = ttk.Entry(root, cursor='hand2')
    min_en10.insert(-1, '---')
    min_en10.place(x=410, y=70*10+138)

    speed_fr1 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr1.place(x=280, y=70*1+121)
    speed_fr2 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr2.place(x=280, y=70*2+121)
    speed_fr3 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr3.place(x=280, y=70*3+121)
    speed_fr4 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr4.place(x=280, y=70*4+121)
    speed_fr5 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr5.place(x=280, y=70*5+121)
    speed_fr6 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr6.place(x=280, y=70*6+121)
    speed_fr7 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr7.place(x=280, y=70*7+121)
    speed_fr8 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr8.place(x=280, y=70*8+121)
    speed_fr9 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr9.place(x=280, y=70*9+121)
    speed_fr10 = LabelFrame(root, text=' ', labelanchor='w', cursor='hand2')
    speed_fr10.place(x=280, y=70*10+121)

    global speed_en1,speed_en2,speed_en3,speed_en4,speed_en5
    global speed_en6,speed_en7,speed_en8,speed_en9,speed_en10
    speed_en1 = Entry(speed_fr1, cursor='hand2')
    speed_en1.insert(-1, '---')
    speed_en1.pack()
    speed_en2 = Entry(speed_fr2, cursor='hand2')
    speed_en2.insert(-1, '---')
    speed_en2.pack()
    speed_en3 = Entry(speed_fr3, cursor='hand2')
    speed_en3.insert(-1, '---')
    speed_en3.pack()
    speed_en4 = Entry(speed_fr4, cursor='hand2')
    speed_en4.insert(-1, '---')
    speed_en4.pack()
    speed_en5 = Entry(speed_fr5, cursor='hand2')
    speed_en5.insert(-1, '---')
    speed_en5.pack()
    speed_en6 = Entry(speed_fr6, cursor='hand2')
    speed_en6.insert(-1, '---')
    speed_en6.pack()
    speed_en7 = Entry(speed_fr7, cursor='hand2')
    speed_en7.insert(-1, '---')
    speed_en7.pack()
    speed_en8 = Entry(speed_fr8, cursor='hand2')
    speed_en8.insert(-1, '---')
    speed_en8.pack()
    speed_en9 = Entry(speed_fr9, cursor='hand2')
    speed_en9.insert(-1, '---')
    speed_en9.pack()
    speed_en10 = Entry(speed_fr10, cursor='hand2')
    speed_en10.insert(-1, '---')
    speed_en10.pack()

    global distance_lb1,distance_lb2,distance_lb3,distance_lb4,distance_lb5
    global distance_lb6,distance_lb7,distance_lb8,distance_lb9,distance_lb10
    distance_lb1 = Label(root, text='---')
    distance_lb1.place(x=800, y=70*1+115)
    distance_lb2 = Label(root, text='---')
    distance_lb2.place(x=800, y=70*2+115)
    distance_lb3 = Label(root, text='---')
    distance_lb3.place(x=800, y=70*3+115)
    distance_lb4 = Label(root, text='---')
    distance_lb4.place(x=800, y=70*4+115)
    distance_lb5 = Label(root, text='---')
    distance_lb5.place(x=800, y=70*5+115)
    distance_lb6 = Label(root, text='---')
    distance_lb6.place(x=800, y=70*6+115)
    distance_lb7 = Label(root, text='---')
    distance_lb7.place(x=800, y=70*7+115)
    distance_lb8 = Label(root, text='---')
    distance_lb8.place(x=800, y=70*8+115)
    distance_lb9 = Label(root, text='---')
    distance_lb9.place(x=800, y=70*9+115)
    distance_lb10 = Label(root, text='---')
    distance_lb10.place(x=800, y=70*10+115)

    map1_button = Button(root, text='Map', bg='red', command=map1, padx=5, pady=5)
    map1_button.place(x=1210, y=70*1+120)
    map2_button = Button(root, text='Map', bg='orange', command=map2, padx=5, pady=5)
    map2_button.place(x=1210, y=70*2+120)
    map3_button = Button(root, text='Map', bg='yellow', command=map3, padx=5, pady=5)
    map3_button.place(x=1210, y=70*3+120)
    map4_button = Button(root, text='Map', bg='lime', command=map4, padx=5, pady=5)
    map4_button.place(x=1210, y=70*4+120)
    map5_button = Button(root, text='Map', bg='green', command=map5, padx=5, pady=5)
    map5_button.place(x=1210, y=70*5+120)
    map6_button = Button(root, text='Map', bg='cyan', command=map6, padx=5, pady=5)
    map6_button.place(x=1210, y=70*6+120)
    map7_button = Button(root, text='Map', bg='blue', command=map7, padx=5, pady=5)
    map7_button.place(x=1210, y=70*7+120)
    map8_button = Button(root, text='Map', bg='pink', command=map8, padx=5, pady=5)
    map8_button.place(x=1210, y=70*8+120)
    map9_button = Button(root, text='Map', bg='magenta', command=map9, padx=5, pady=5)
    map9_button.place(x=1210, y=70*9+120)
    map10_button = Button(root, text='Map', bg='purple', command=map10, padx=5, pady=5)
    map10_button.place(x=1210, y=70*10+120)

    start2X_button = Button(root, text='2x', command=start_2X)
    start2X_button.config(padx=23, pady=4, bg='lime', fg='forestgreen')
    start2X_button.place(x=200, y=900)

    start8X_button = Button(root, text='8x', command=start_8X)
    start8X_button.config(padx=23, pady=4, bg='forestgreen', fg='lime')
    start8X_button.place(x=400, y=900)

    start4X_button = Button(root, text='4x', command=start_4X)
    start4X_button.config(padx=23, pady=4, bg='limegreen', fg='green')
    start4X_button.place(x=300, y=900)
    
    start_i_button = Button(root, text='Infinity', command=start_infinity)
    start_i_button.config(padx=20, pady=4, bg='darkgreen', fg='greenyellow')
    start_i_button.place(x=500, y=900)
    
    start_button = Button(root, text='Start', command=start)
    start_button.config(padx=20, pady=4, bg='greenyellow', fg='darkgreen')
    start_button.place(x=100, y=900)
    
    pause_button = Button(root, text='Pause', command=pause)
    pause_button.config(padx=20, pady=3, bg='red')
    pause_button.place(x=800, y=900)

    restart_button = Button(root, text='Restart', command=restart)
    restart_button.config(padx=20, pady=3, bg='gold')
    restart_button.place(x=900, y=900)

    global J
    J = 1


root = Tk()
root.title ('Car Monitoring System')
root.geometry ('1400x950')
root.option_add('*tearOff', False)
menubar = Menu()
root.config(menu=menubar)

data_menu = Menu(menubar)
menubar.add_cascade(label = 'Dataset', menu=data_menu)
data_menu.add_command(label='Add Car', command=add_car, accelerator='Ctrl+A')
data_menu.add_command(label='Create Dataset', command=create_database, accelerator='Ctrl+C')
data_menu.add_separator()
data_menu.add_command(label='Quit', command=root.destroy, accelerator='Alt+F4')

play_menu = Menu(menubar)
menubar.add_cascade(label = 'Playback', menu=play_menu)
play_menu.add_command(label='Open', command=open_playback, accelerator='Ctrl+O')
play_menu.add_separator()
start_menu = Menu(play_menu)
play_menu.add_cascade(label='Start', menu=start_menu)
start_menu.add_command(label='1X', command=start, accelerator='Ctrl+S')
start_menu.add_command(label='2X', command=start_2X)
start_menu.add_command(label='4X', command=start_4X)
start_menu.add_command(label='8X', command=start_8X)
start_menu.add_command(label='Infinity', command=start_infinity)
play_menu.add_command(label='Pause', command=pause, accelerator='Ctrl+P')
play_menu.add_command(label='Restart', command=restart, accelerator='Ctrl+R')

car_label = Label(root, text='Number of Cars:')
car_label.place(x=10, y=5)
car_spin = ttk.Spinbox (root, from_=10, to=10)
car_spin.config(state = 'readonly', justify='center', width=10)
car_spin.place(x=105, y=5)

point_label = Label(root, text='Number of Points:')
point_label.place(x=220, y=5)
point_spin = ttk.Spinbox (root, from_=1000, to=6000)
point_spin.config(state = 'readonly', justify='center', increment=100, width=10)
point_spin.place(x=325, y=5)

var = DoubleVar()
added_frame = Frame(root)
added_frame.place(x=40, y=40)
added_Label = Label(added_frame, text='Number of Added Cars-> ')
added_Label.pack(side='left')
added_pb = ttk.Progressbar(added_frame)
added_pb.config(length=750, mode='determinate', maximum=10, variable=var)
added_pb.pack(side='left')

name_label = Label(root, text ='Name: ')
name_label.place(x=520, y=5)
name_entry = Entry(root, width=10)
name_entry.place(x=562, y=5)

company_label = Label(root, text ='Company: ')
company_label.place(x=670, y=5)
company_entry = Entry(root, width=10)
company_entry.place(x=732, y=5)

year_label = Label(root, text ='Year: ')
year_label.place(x=830, y=5)
year_entry = Entry(root, width=10)
year_entry.place(x=862, y=5)
    
lat_label = Label(root, text ='Latitude: ')
lat_label.place(x=970, y=5)
lat_entry = Entry(root, width=20)
lat_entry.place(x=1020, y=5)

long_label = Label(root, text ='Longitude: ')
long_label.place(x=1205, y=5)
long_entry = Entry(root, width=20)
long_entry.place(x=1270, y=5)

add_button = ttk.Button(root, text='Add Car', command=add_car)
add_button.place(x=1000, y=38)

create_button = ttk.Button(root, text='Create Dataset', command=create_database)
create_button.place(x=1090, y=38)
create_button.config(state='disable')

playback_button = Button(root, text='Playback Window', command=open_playback)
playback_button.place(x=1200, y=38)
playback_button.config(background='black', foreground='white', padx=20)

separator = Label(root, text=150*'=-')
separator.place(x=0, y=70)

quit_button = Button(root, text='Quit', command=root.destroy)
quit_button.place(x=1300, y=910)
quit_button.config(background='red', padx=20)

root.bind('<Control-a>', lambda event: add_car())
root.bind('<Control-c>', lambda event: create_database())
root.bind('<Alt-F4>', lambda event: root.destroy())
root.bind('<Control-o>', lambda event: open_playback())
root.bind('<Control-s>', lambda event: start())
root.bind('<Control-p>', lambda event: pause())
root.bind('<Control-r>', lambda event: restart())

root.mainloop()
