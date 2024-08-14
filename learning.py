import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Simple App')

    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    entry = tk.Entry(frame)
    entry.grid(row=0, column=0)

    entry_btn = tk.Button(frame, text='Add')
    entry_btn.grid(row=0, column=1)

    root.mainloop()

if __name__ == "__main__":
    main()