from src.load_data import read_text_from_file
from psychopy import visual, gui, event


def show_info(win, file_name, text_size, text_color, screen_res, insert=''):
    msg = read_text_from_file(file_name, insert=insert)
    msg = visual.TextStim(win, color=text_color, text=msg, height=text_size, wrapWidth=screen_res['width'])
    msg.draw()
    win.flip()
    key = event.waitKeys(keyList=['f7', 'return', 'space'])
    if key == ['f7']:
        raise Exception('Experiment finished by user on info screen! F7 pressed.')
    win.flip()


def show_image(win, file_name, size, key='f7'):
    print(size)
    image = visual.ImageStim(win=win, image=file_name, interpolate=True, size=size)
    image.draw()
    win.flip()
    clicked = event.waitKeys(keyList=[key, 'return', 'space'])
    if clicked == [key]:
        exit(0)
    win.flip()

