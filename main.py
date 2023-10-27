import tkinter as tk
import requests
from PIL import Image, ImageTk #pip install pillow

root = tk.Tk()

root.title("Weather App")
root.geometry("600x500")

# Key :- d4f74cf137fb2f8369dbb3eb70a74f7d

# API url :- https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your API key}

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        visibility = weather['visibility']/1000
        pressure = weather['main']['pressure']
        final_str=(f"City:{city}\nCondition:{condition}\nTemperature:{temp}°F\nHumidity:{humidity}%\nVisibility:{visibility}km\nPressure:{pressure}mb")
    except:
        final_str='There is a problem retrieving that information'
    return final_str

def get_weather(city):
    weather_key = 'd4f74cf137fb2f8369dbb3eb70a74f7d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID' : weather_key, 'q':city, 'units':'imperial'}
    response = requests.get(url, params)
    # print(response.json())
    weather=response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon_name):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon_name+'.png').resize((size, size), Image.LANCZOS))
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image=img




img=Image.open('bg.jpg')
img = img.resize((600,500),Image.LANCZOS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl =tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height = 500)

frame_one = tk.Frame(bg_lbl, bg='#42c2f4', bd=5)
frame_one.place(x=80 , y=50, width=450, height=50)

heading_title=tk.Label(bg_lbl, text='Search for over 200,000 cities!', fg='red', bg= 'sky blue', font=("times new roman", 18, 'bold'))
heading_title.place(x=80, y=18)

txt_box = tk.Entry(frame_one, font=("times new roman", 25), width=17)
txt_box.grid(row=0, column=0, sticky='w')

btn=tk.Button(frame_one, text='get weather', fg='green', font=('times new roman', 16, 'bold'), command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two = tk.Frame(bg_lbl, bg='#42c2f4', bd=5)
frame_two.place(x=80 , y=130, width=450, height=300)

result=tk.Label(frame_two, font = 40, bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)


weather_icon=tk.Canvas(result, bg='White', bd = 0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


root.mainloop()

# After 45min