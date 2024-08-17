import FreeSimpleGUI as fsg
from extract import extract_archive


fsg.theme("Black")

label1 = fsg.Text("Select Archive: ")
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse("Choose", key="archive")

label2 = fsg.Text("Select dest dir: ")
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose", key="folder")

extract_button = fsg.Button("Extract")
output_label = fsg.Text(key="output", text_color="green")

window = fsg.Window("Archive Extractor", 
                    layout=[[label1, input1, choose_button1], 
                            [label2, input2, choose_button2], 
                            [extract_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archivepath = values["archive"]
            folderpath = values["folder"]
            extract_archive(archivepath=archivepath, dest_dir=folderpath)
            window["output"].update(value="Extraction Completed", text_color="Green", background_color="White")
            print(event, values)
        case fsg.WIN_CLOSED:
            break
window.close()
