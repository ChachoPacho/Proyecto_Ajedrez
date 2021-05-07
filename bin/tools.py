from PIL import Image, ImageTk
import json

#   game's information's file
ListIMG_PR = {}
ListIMG_SR = {}
with open('config/data.json', 'r') as outfile:
    data = json.load(outfile)


def img_resizer(width):
    global ListIMG_PR, ListIMG_SR

    #   game's images
    _ext = data['element']['ext']
    _dir = data['element']['dir']

    #   filters
    if width < 90:
        width = 90

    def resize(input_list, output_list):
        _iter = 0
        for image in input_list:
            _image = Image.open(_dir + image + _ext)
            _image = _image.resize((int(width), int(width)), Image.ANTIALIAS)
            _image = ImageTk.PhotoImage(_image)
            output_list.update({image: _image})
            _iter += 1

    resize(data['element']['pieces'], ListIMG_PR)
    resize(data['element']['special'], ListIMG_SR)

def data_storage(*search: str):
    extracted_data = data
    for searches in search:
        extracted_data = extracted_data[searches]

    return extracted_data
