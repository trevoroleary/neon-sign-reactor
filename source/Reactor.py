from FFT import FFT
from Microphone import Microphone
from Lights import NeonLight

class NeonReactor:
    def __init__(self, microphone: Microphone, fft: FFT, lights: NeonLight):
        self.microphone = microphone
        self.fft = fft
        self.lights = lights

    def start_reacting(self):
        while True:
            self.react()
    
    def react(self):
        audio_data = self.microphone.listen()
        fft_data = self.fft.get_frequency_data(audio_data=audio_data)

        self.instant_volume_react(fft_data)
    
    def instant_volume_react(self, fft_data):
        # Constants
        high_thresh = 0.3e6
        low_thresh = 0.05e6
        rest_level = 0.02

        sense_range = fft_data[1:10]
        max_all = max(sense_range)
        offset = rest_level * (1 - (max_all - low_thresh) / high_thresh)

        if max_all > high_thresh: # If the max of all frequencies in the range is very high
            self.lights.loud_reaction(highest_frequency_power=max_all, offset=offset)
        
        if max_all > low_thresh:
            self.lights.volume_reaction(highest_frequency_power=max_all, offset=offset)
        else:
            self.lights.quiet_reaction()

    def old_reactive_calc(self, fft_data):
        # trigger_thresh = 0.3e6
        # sense_range = fft_data[1:25]
        # if any(y > trigger_thresh for y in sense_range):
            # _thread.start_new_thread(pulse, ())
        pass

    def volume_reactive_calc(self, fft_data):
        # global LEVELS
        # high_thresh = 0.3e6
        # low_thresh = 0.1e6
        # sense_range = fft_data[1:10]
        # max_all = max(sense_range)
        # if max_all > low_thresh:
            # level_append = (max_all - low_thresh)/(high_thresh - low_thresh)
        # else:
            # level_append = 0
        # LEVELS.append(level_append/WINDOW_SIZE)
        # LEVELS.pop(0)
        # logger.info(f"Sum of Levels is {sum(LEVELS)}")
        # set_level(sum(LEVELS))
        pass
