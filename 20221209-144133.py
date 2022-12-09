import tkinter as tk
import requests
import json

def F():
    v = name.get()
    response = requests.get('https://github.com/firehol/blocklist-ipsets')
    f_ = json.loads(response.text)
    y = dict.fromkeys(['company'], f_['company'])
    z = dict.fromkeys(['created_at'], f_['created_at'])
    a = dict.fromkeys(['email'], f_['email'])
    b = dict.fromkeys(['id'], f_['id'])
    c = dict.fromkeys(['name'], f_['name'])
    g = dict.fromkeys(['url'], f_['url'])
    j = (y,z,a,b,c,g)

    if v == 'blocklist-ipsets':
        with open('C:\\Users\\EthanCarter\\Desktop\\vivod.json', 'w') as file:
            json.dump(j,file)       
    else:
        print('Файл не найден')

window = tk.Tk()
window.geometry('400x300')
window.title("json") 
name = tk.Entry(window)
name.grid(padx=120, pady=15)
btn = tk.Button(window, text="click", command=F)
btn.grid(padx=90, pady=15)
window.mainloop()
F()