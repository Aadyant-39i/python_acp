from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()

window.title('My Photo Album')
window.geometry('400x450')


# ---------------------------------------------------------------
# PART 2 - Add a title Label at the top using grid
# ---------------------------------------------------------------

title = Label(window, text='My Photo Album', fg='white', bg='purple',
              width=40)

title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


# ---------------------------------------------------------------
# PART 3 - Add an Image using Pillow (PIL)
# ---------------------------------------------------------------

img_file = Image.open('photo.jpg')
resized_file = img_file.resize((300, 220))
album_photo = ImageTk.PhotoImage(resized_file)

photo_label = Label(window, image=album_photo)
photo_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# ---------------------------------------------------------------
# PART 4 - Button Commands (Actions)
# ---------------------------------------------------------------

def like_photo():
    messagebox.showinfo('Interaction', 'You liked this photo!')

def view_details():
    details_window = Toplevel(window)
    details_window.title('Photo Details')
    details_window.geometry('250x120')
    
    info = Label(details_window, text='File: photo.jpg\nFormat: JPEG\nDate: October 2026')
    info.pack(pady=20)


# ---------------------------------------------------------------
# PART 5 - Add Buttons and run the window
# ---------------------------------------------------------------

like_btn = Button(window, text='Like Photo', bg='purple', fg='white',
                  width=15, command=like_photo)
like_btn.grid(row=2, column=0, padx=10, pady=10)

details_btn = Button(window, text='View Details', bg='purple', fg='white',
                     width=15, command=view_details)
details_btn.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
