import tkinter.ttk as ttk
from tkinter import*

root =Tk()
root.title('Picture Merger')

#file frame()
file_frame = Frame(root)
file_frame.pack(fill = 'x', padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx = 5, pady = 5,
                      width = 12,text = 'Add file')
btn_add_file.pack(side = 'left')

btn_delete_file = Button(file_frame, padx = 5, pady = 5,
                      width = 12, text = 'Delete')
btn_delete_file.pack(side = 'right')

#list frame
list_frame = Frame(root)
list_frame.pack(fill = 'both', padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = 'right', fill = 'y')

list_file = Listbox(list_frame, selectmode = 'extended',
                    height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side = 'left', fill = 'both', expand = True)
scrollbar.config(command = list_file.yview)

#store frame
path_frame = LabelFrame(root,text = 'Store Path')
path_frame.pack(fill = 'x', padx = 5, pady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = 'left', fill = 'x',expand = True,
                   padx=5, pady=5,ipady = 4)

find_btn = Button(path_frame,text = 'Find', width = 10)
find_btn.pack(side = 'right', padx = 5, pady = 5)

#option frame
option_frame = LabelFrame(root, text = 'Options')
option_frame.pack(padx = 5, pady = 5)

#width
lbl_width = Label(option_frame, text = 'Width',width = 8)
lbl_width.pack(side = 'left')

#combobox
opt_width = ['Original','1024','800','640']
cmb_width = ttk.Combobox(option_frame, state = 'readonly',
                         values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side = 'left')

#space
lbl_space = Label(option_frame, text = 'Space', width = 8)
lbl_space.pack(side = 'left', padx = 5, pady = 5)
space_option = ['None','narrow','normal','wide']
cmb_space = ttk.Combobox(option_frame, state = 'readonly',
                         values = space_option,width = 10)
cmb_space.current(0)
cmb_space.pack(side = 'left', padx = 5, pady = 5)

#format
format_space = Label(option_frame, text = 'Format', width = 8)
format_space.pack(side = 'left', padx = 5, pady = 5)

format_option = ['PNG','JPG','BMP']
cmb_format = ttk.Combobox(option_frame, state = 'readonly',
                         values = format_option,width = 10)
cmb_format.current(0)
cmb_format.pack(side = 'left', padx = 5, pady = 5)



#progress bar
frame_progress = LabelFrame(root, text = 'Progress')
frame_progress.pack(fill = 'x', padx = 5, pady = 5)
p_var = DoubleVar
progress_bar = ttk.Progressbar(frame_progress, maximum = 100,
                               variable = p_var)
progress_bar.pack(fill = 'x', padx = 5, pady = 5)

#start and terminate Button
frame_start = Frame(root)
frame_start.pack(fill = 'x', padx = 5, pady = 5)


btn_stop = Button(frame_start, text = 'Terminate',padx = 5, pady = 5,
                  width = 12, command = root.quit)
btn_stop.pack(side = 'right', padx = 5, pady = 5)

btn_start = Button(frame_start, text = 'Start',padx = 5, pady = 5,
                  width = 12)
btn_start.pack(side = 'right', padx = 5, pady = 5)

root.resizable(False, False)
root.mainloop()