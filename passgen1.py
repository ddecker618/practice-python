from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry('500x300')


# Generate Random Password
def new_rand():
    # Clear Our Entry Box
    pw_entry.delete(0, END)

    # Get PW Length and convert to integer
    pw_length = int(my_entry.get())

    # create a variable to hold our Password
    my_password = ''

    # Loop through Password Length
    for x in range(pw_length):
        my_password += chr(randint(33,126))


    # Output password to the screen
    pw_entry.insert(0, my_password)



def clipper():
    # Clear the clipboard
	root.clipboard_clear()
	# Copy to clipboard
	root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text= 'How many characters?')
lf.pack(pady=20)

# Create Entry Box To Designate Numbers of Characters
my_entry =Entry(lf, font=('Helvetica', 24))
my_entry.pack(pady=20, padx=20)

# Create Entry Box For Our Returned Password
pw_entry = Entry(root, text='', font=('Helvetica', 24))
pw_entry.pack(pady=20)

# Create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#Our buttons
my_button = Button(my_frame, text='Generate Strong Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button =Button(my_frame, text='Copy To Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()
