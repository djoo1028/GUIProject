import os
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tkinter import*
from tkinter import filedialog
from PIL import Image

root =Tk()
root.title('Picture Merger')

#add file
def add_file():
    files = filedialog.askopenfilenames(
        title = 'Select image file', filetypes = (('PNG file','*.png'),('All files','*.*')),
        initialdir = 'C:/Users/12537/PycharmProjects/PythonGUIFinalproject') # it shows default path

    # selected file
    for file in files:
        list_file.insert(END, file)

def del_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#Store path
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0,folder_selected)

#merge image
def merge_image():
    try:
        # print('width:', cmb_width.get())
        # print('space:', cmb_space.get())
        # print('format:', cmb_format.get())

        #width option
        img_width = cmb_width.get()
        if img_width == 'Original':
            img_width = -1 # return original

        else:
            img_width = int(img_width)

        #space
        #'None','narrow','normal','wide'
        img_space = cmb_space.get()
        if img_space == 'narrow':
            img_space = 30
        elif img_space == 'normal':
            img_space = 60
        elif img_space == 'wide':
            img_space = 90
        else:
            img_space = 0

        #format
        img_format = cmb_format.get().lower() #PNG, JPG, BMP to lower case





        ####################################
        images = [Image.open(x) for x in list_file.get(0,END)]

        #image size
        image_sizes = [] #(width1, height1), (width2,height2)....
        if img_width > - 1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]
        # if original width : original height = after width : after height
        #         100       :      60         =  80          :   x            ?
        #          60 * 80                    =     100x
        #              x     =    60 * 80 / 100



        #size[0] : width, / size[1] = height
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]
        # print('widths:', widths)
        # print('heights:', heights)

        widths, heights = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(heights)
        # print('max width:', max_width)
        # print('total height:', total_height)

        #Create scatch paper
        if img_space > 0:
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new('RGB',(max_width, total_height), (255,255,255))
        y_offset = 0 # y location

        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1]

        for idx, img in enumerate(images):
            # if it is not original
            if img_width > - 1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = ((idx + 1) / len(images)) * 100# Actual percentage
            p_var.set(progress)
            progress_bar.update()


        #format option
        file_name = 'Nan_photo.' + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msg.showinfo('notice', 'DONE')
    except Exception as err:
        msg.showerror('Error', err)


def start():
    # print('width:', cmb_width.get())
    # print('space:', cmb_space.get())
    # print('format:', cmb_format.get())
    if list_file.size() == 0:
        msg.showwarning('Warning','Select Image File')
        return
    #dest path check
    if len(txt_dest_path.get()) == 0:
        msg.showwarning('Warning', 'Select Store Path')
        return

    merge_image()
    #merge image



#file frame()
file_frame = Frame(root)
file_frame.pack(fill = 'x', padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx = 5, pady = 5,
                      width = 12,text = 'Add file', command = add_file)
btn_add_file.pack(side = 'left')

btn_delete_file = Button(file_frame, padx = 5, pady = 5,
                      width = 12, text = 'Delete',command = del_file)
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

find_btn = Button(path_frame,text = 'Find', width = 10, command = browse_dest_path)
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

p_var = DoubleVar()
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
                  width = 12, command = start)
btn_start.pack(side = 'right', padx = 5, pady = 5)

root.resizable(False, False)
root.mainloop()