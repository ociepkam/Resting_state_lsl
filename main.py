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

    if config["send_lsl_triggers"]:
        from pylsl import StreamInfo, StreamOutlet
        lsl_info = StreamInfo(name="TriggerStream", type="Triggers", channel_count=1, nominal_srate=0, channel_format="int32", source_id="myuid34234")
        lsl_outlet = StreamOutlet(info=lsl_info)
    else:
        lsl_outlet = None

    # --------------------------------------- procedure ---------------------------------------
    # instruction
    show_info(win=win, file_name=join("messages", "start.txt"), text_size=config["text_size"], text_color=config["text_color"], screen_res=screen_res)

    # preparation
    fixation.setAutoDraw(True)
    win.callOnFlip(clock.reset)
    if config["send_lsl_triggers"]:
        win.callOnFlip(lsl_outlet.push_sample, x=[1])
    win.flip()

    # mian loop
    while clock.getTime() < config["rest_time"]:
        check_exit(key=config["exit_key"])

    # cleaning
    fixation.setAutoDraw(False)
    if config["send_lsl_triggers"]:
        win.callOnFlip(lsl_outlet.push_sample, x=[1])
    win.flip()

    # end screen
    show_info(win=win, file_name=join("messages", "end.txt"), text_size=config["text_size"], text_color=config["text_color"], screen_res=screen_res)


if __name__ == "__main__":
    main()
