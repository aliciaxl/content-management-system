import tkinter as tk
from tkinter import Text, ttk
import json

class ContentManagementSystem():
    def __init__(self, root):
        #main window
        self.root = root
        self.root.title("Content Management System")
        self.root.configure(bg = "gray12")
        self.root.geometry("600x360")
        
        self.create_widgets()

    def create_widgets(self):
        self.greeting = Text(self.root, 
                    bg = "gray12", 
                    fg = "PaleVioletRed1", 
                    font = ('Futura', 16), 
                    borderwidth = 0, 
                    highlightthickness = 0, 
                    width = 36, 
                    height = 1)
        self.greeting.configure(state = 'normal')
        self.greeting.insert('insert', 'Hello friend,')
        self.greeting.configure(state = 'disabled')
        self.greeting.pack(pady = (48, 16))

        self.text = Text(self.root, 
                    bg = "gray12", 
                    fg="bisque1", 
                    font = ('Futura', 16), 
                    borderwidth = 0, 
                    highlightthickness = 0, 
                    width = 36, 
                    height = 4,
                    wrap = 'word')
        self.text.configure(state = 'normal')
        self.text.insert('insert', 'Can\'t wait to see you again later. Until then, have a day as amazing as you are!')
        self.text.configure(state = 'disabled')
        self.text.pack(pady = (0, 48))

        self.edit = tk.Button(self.root,
                        text = "Edit",
                        font = ('Futura', 16),
                        bg = "white",
                        fg = "gray24",
                        command = self.click_edit)
        self.edit.pack(pady = (0, 8))

        self.save = tk.Button(self.root,
                        text = "Save",
                        font = ('Futura', 16),
                        bg = "white",
                        fg = "gray24",
                        command = self.click_save)
        self.save.pack(pady = (0, 8))


    def focus_in(self, event):
        event.widget.config(highlightthickness = 2.8, 
                        highlightcolor = "dark slate gray", 
                        highlightbackground = "gray12")
    def focus_out(self, event):
        event.widget.config(highlightthickness = 0)

    def click_edit(self):
        self.greeting.configure(state = 'normal')
        self.text.configure(state = 'normal')

        self.edit.config(bg = "plum1", fg = "honeydew4")
        self.save.config(bg = "white", fg = "gray24")

        self.greeting.bind("<FocusIn>", self.focus_in)
        self.greeting.bind("<FocusOut>", self.focus_out)
        self.text.bind("<FocusIn>", self.focus_in)
        self.text.bind("<FocusOut>", self.focus_out)

        self.greeting.focus_set()

    def click_save(self):
        self.greeting.unbind("<FocusIn>")
        self.greeting.unbind("<FocusOut>")
        self.text.unbind("<FocusIn>")
        self.text.unbind("<FocusOut>")

        self.save.config(bg = "plum1",  fg = "honeydew4")
        self.edit.config(bg = "white", fg = "gray24")

        self.greeting.configure(state = 'disabled')
        self.text.configure(state = 'disabled')

        self.greeting.config(highlightthickness=0)
        self.text.config(highlightthickness=0)

        title = self.greeting.get("1.0", "end-1c")
        content = self.text.get("1.0", "end-1c")

        page_content_obj = {
                'title' : title, 
                'content' : content
        }

        with open('page_content.json', 'w') as file:
            json.dump(page_content_obj, file, indent=4)
            
        with open('page_content.json', 'r') as f:
            data = json.load(f)
            
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>CIS112 Content Management System</title>
            <link rel="stylesheet" href="hobbies.css">
        </head>
        <body>
            <h1>{data['title']}</h1>
            <p>{data['content']}</p>
        </body>
        </html>
        """

        with open('index.html', 'w') as fh:
            fh.write(html)
    
def main():
    root = tk.Tk()
    app = ContentManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()