import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self):
        root = tk.Tk()
        root.title('Simple App')
        root.mainloop()

'''
def main():
    root = tk.Tk()
    root.title('Simple App')

    def add_to_list(event=None):
        text = entry.get()
        if text:
            text_list.insert(tk.END, text)
            entry.delete(0, tk.END)

    def add_to_list2(event=None):  #Created a separate function for frame2
        text = entry2.get()
        if text:
            text_list2.insert(tk.END, text)
            entry2.delete(0, tk.END)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)   #for frame 2
    root.rowconfigure(0, weight=1)

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    entry = ttk.Entry(frame)
    entry.grid(row=0, column=0, sticky='ew')

    entry.bind("<Return>", add_to_list)

    entry_btn = ttk.Button(frame, text='Add', command = add_to_list)
    entry_btn.grid(row=0, column=1)

    text_list = tk.Listbox(frame)
    text_list.grid(row=1, column=0, columnspan=2, sticky='nsew')

    #Frame 2 starts here
    frame2 = tk.Frame(root)
    frame2.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

    frame2.columnconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)

    entry2 = tk.Entry(frame2)
    entry2.grid(row=0, column=0, sticky='ew')

    entry2.bind("<Return>", add_to_list2)

    entry_btn2 = tk.Button(frame2, text='Add', command=add_to_list2)
    entry_btn2.grid(row=0, column=1)

    text_list2 = tk.Listbox(frame2)
    text_list2.grid(row=1, column=0, columnspan=2, sticky='nsew')
    #Frame 2 ends here

    root.mainloop()
'''

if __name__ == "__main__":
    main()