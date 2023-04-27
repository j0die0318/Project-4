import tkinter as tk
import subprocess 

def dl():
    url = txt_url.get()
    
    command = f"youtube-dl {url}"

    subprocess.run(command,
                   shell=True, 
                   text=True, 
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)


root = tk.Tk()
root.wm_title('Youtube Video Dowloader')
#root.geometry("400x300") 

lbl_url = tk.Label(root, text='URL')
txt_url = tk.Entry(root)
btn_dl = tk.Button(root, text='Download', command=dl)

lbl_url.grid(row=0, column=0, padx=10, pady=10)
txt_url.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')
btn_dl.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()