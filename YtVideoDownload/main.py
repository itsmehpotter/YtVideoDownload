import tkinter as tk
import pytube

from tkinter import *
from pytube import YouTube
from tkinter import filedialog , messagebox


def createWidget():

    link_label = Label(root, text="Youtube URL: ", bg="#E8D579")
    link_label.grid(row =1, column=0, pady=5, padx=5)



    root.link_text = Entry(root, width=50, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)



    distination_label = Label(root, text="Destination: ", bg="#E8D579")
    distination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1 , pady=3, padx=3)


    browse_put = Button(root, text='Browse', command=browse,width=10, bg='#cccc00')
    browse_put.grid(row=2, column=2, pady=1, padx=3)


    download_put = Button(root , text="[*] Download Video [*]", command=download_video,width=25, bg= '#cccc00' )
    download_put.grid(row=3, column=1, pady=3, padx=3)


def radiobutt():
    R2 = Radiobutton(root, text="mp3", command="")
    R2.pack(anchor=W)


def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    download_path.set(download_dir)


def download_video():
    url = video_link.get()
    folder = download_path.get()
    get_video = YouTube(url)
    get_stream = get_video.streams.get_highest_resolution()
    get_stream.download(folder)
    messagebox.showinfo(title="Succes!!", message= "Download Succes!!!")








root = tk.Tk()


root.geometry("600x120")


root.resizable(FALSE, FALSE)

root.title("Youtube Video Download")

root.config(background="#1a1a00")

video_link = StringVar()
download_path = StringVar()

createWidget()
root.mainloop()