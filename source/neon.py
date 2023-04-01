from FFT import FFT
from Lights import NeonLight
from Microphone import AmazonMicrophone, RazerMicrophone
from Reactor import NeonReactor

microphone = RazerMicrophone()
chunk = microphone.CHUNK

fft = FFT(chunk=chunk)
lights = NeonLight()
reactor = NeonReactor(microphone=microphone, fft=fft, lights=lights)

reactor.start_reacting()