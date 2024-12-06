from psychopy import visual, event, core
from os.path import join

from src.screen_misc import get_screen_res
from src.check_exit import check_exit
from src.load_data import load_config
from src.show_info import show_info


def main():

    config = load_config()

    screen_res = dict(get_screen_res())
    win = visual.Window(list(screen_res.values()), fullscr=True, monitor='testMonitor', units='pix', screen=0,
                        color=config["screen_color"])
    event.Mouse(visible=False)
    clock = core.Clock()
    fixation = visual.TextStim(win, color=config["fixation_color"], text=config["fixation_text"],
                               height=config["fixation_size"])

    # --------------------------------------- procedure ---------------------------------------
    show_info(win=win, file_name=join("messages", "start.txt"), text_size=config["text_size"], text_color=config["text_color"], screen_res=screen_res)
    fixation.setAutoDraw(True)
    win.callOnFlip(clock.reset)
    win.flip()

    while clock.getTime() < config["rest_time"]:
        check_exit(key=config["exit_key"])

    fixation.setAutoDraw(False)
    show_info(win=win, file_name=join("messages", "end.txt"), text_size=config["text_size"], text_color=config["text_color"], screen_res=screen_res)


if __name__ == "__main__":
    main()