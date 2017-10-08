class ReproductorWAV:
    def __init__(self, archivo):
        self.archivo=archivo
        print self.archivo
    
    def Reproducir(self):
        import pyaudio  
        import wave  

        #define stream chunk   
        chunk = 1024
        #open a wav format music  
        f = wave.open(self.archivo,"rb")  
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  

        #paly stream  
        while data != '':  
            stream.write(data)  
            data = f.readframes(chunk)  

        #stop stream  
        stream.stop_stream()  
        stream.close()  

        #close PyAudio  
        p.terminate()
            



          
