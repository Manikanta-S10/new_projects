from tkinter import * 
import requests

def get_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(current_quote,text=data['quote'])


window = Tk()
window.title('Kanye Quotes')
window.config(padx=50,pady=50)

canvas = Canvas(width=300, height=414)
bg_image = PhotoImage(file='API/kanye_quotes/background.png')
canvas.create_image(150,207,image=bg_image)
current_quote = canvas.create_text(150,190,text="The thought police want to suppress freedom of thought",width=250,font=('courier',28,'bold'))
canvas.grid(row=0,column=0)

kanye_img = PhotoImage(file='API/kanye_quotes/kanye.png')
kanye = Button(image=kanye_img,command=get_quote)
kanye.grid(row=1,column=0)

window.mainloop()

