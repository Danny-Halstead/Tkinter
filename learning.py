import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Simple App')

    lbl = tk.Label(root, text='Label 1')
    lbl.grid(row = 0, column = 0)

    btn = tk.Button(root, text='Button 1')
    btn.grid(row = 0, column = 1)

    root.mainloop()

if __name__ == "__main__":
    main()