import tkinter as tk

class GUIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python GUI")

        # Create a frame as a container
        self.container_frame = tk.Frame(self.master)
        self.container_frame.pack()

        # Create buttons inside the container frame
        self.button1 = tk.Button(self.container_frame, text="Button 1")
        self.button1.pack(side=tk.LEFT)

        self.button2 = tk.Button(self.container_frame, text="Button 2")
        self.button2.pack(side=tk.LEFT)

        self.button3 = tk.Button(self.container_frame, text="Button 3")
        self.button3.pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
