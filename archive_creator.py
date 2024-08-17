import FreeSimpleGUI as fsg
from archive import make_archive


label1 = fsg.Text("Selct files to compress: ")
input1 = fsg.Input()
choose_button1 = fsg.FilesBrowse(button_text="Choose", button_color=("Black", "White"), key="files")

label2 = fsg.Text("Selct destination folder: ")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse(button_text="Choose", button_color=("Black", "White"), key="folder")

compress_button = fsg.Button(button_text="Compress")
output_label = fsg.Text(key="output", text_color="Green")

window = fsg.Window(title="Files Compressor", 
                    layout=[[label1, input1, choose_button1], 
                            [label2, input2, choose_button2], 
                            [compress_button, output_label]])

while True:
    event, values = window.read()

    match event:
        case "Compress":
            filepaths = values["files"].split(';')
            folderpath = values["folder"]
            make_archive(filepaths=filepaths, dest_dir=folderpath)
            window["output"].update(value="Compression Completed", text_color="Green", background_color="White")
            print(event, values)
        case fsg.WIN_CLOSED:
            break

window.read()
window.close()
