from dl import Downloader
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)   
        self.init_ui()

    def init_ui(self):
        lbl_url = ttk.Label(self.master, text='Youtube URL')
        lbl_url.pack(pady=5)

        self.txt_url = ttk.Entry(self.master, width=40)
        self.txt_url.pack(padx=10, pady=5, fill='x')

        btn_get_s = ttk.Button(self.master, text ='Get Streams')
        btn_get_s.bind('<Button-1>', self.btn_click)
        btn_get_s.pack(pady=5)

        self.lbl_video_title = ttk.Label(self.master, text='[Title Here...]')
        self.lbl_video_title.pack(pady=5)

        self.table = ttk.Treeview(self.master, 
                                  show='headings', 
                                  columns=('itag', 'mime_type', 'resolution', 'type', 'filesize'))
        
        tbl = self.table
        tbl.bind('<Double-1>', self.row_double_click)
        tbl.heading('itag', text='iTag')
        tbl.heading('mime_type', text='Mine Type')
        tbl.heading('resolution', text='Resolution')
        tbl.heading('type', text='Type')
        tbl.heading('filesize', text='Filesize')
        
        tbl.pack(pady=5, fill='both', expand=True)

    def btn_click(self, event):
        url = self.txt_url.get()
        if url == "":
            #show error message
            messagebox.showerror(title='Error', 
                                 message='URL must not be empty')
            return
        self.downloader = Downloader(self.txt_url.get())
        self.lbl_video_title.config(text=self.downloader.yt.title)
        streams = self.downloader.fetch_streams()
        self.populate_table(streams)

    def populate_table(self, streams):
        for item in self.table.get_children():
              self.table.delete(item)
        for s in streams:
             self.table.insert('', 'end', values=(s.itag, s.mime_type, s.resolution, s.type, s.filesize))

    def row_double_click(self, event):
        children = self.table.get_children()
        if len(self.table.get_children()) == 0:
            messagebox.showwarning(title='No selected stream.',
                                   message='Fetch streams 1st')
            return 
        
        selected_item=self.table.selection()[0]
        values = self.table.item(selected_item, 'values')
        itag = values[0]
        self.downloader.download(itag)


if __name__ == '__main__':

    root = tk.Tk()
    root.title('Youtube Downloader')

    window = MainFrame(root)

    root.mainloop()