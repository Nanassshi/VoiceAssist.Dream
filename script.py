from subprocess import Popen
from speech_recognition import (Recognizer, AudioFile)
from speech_recognition import (UnknownValueError, RequestError)

import random

from pydub import AudioSegment
from pydub.playback import play

import webbrowser
import os
import pathlib

from tkinter import *


count = 0


def listen(count, time):
    import pyaudio
    import wave
    count += 1
    filename = f"command_{count}_{random.randint(1, 100000)}.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = time
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    audio_to_text(filename)


def audio_to_text(filename):
    class SpeechOggAudioFileToText:
        def __init__(self):
            self.recognizer = Recognizer()

        def ogg_to_wav(self, file):
            args = ['ffmpeg','-i', file, filename]
            process = Popen(args)
            process.wait()
        @property
        def text(self):
            AUDIO_FILE = filename
            with AudioFile(AUDIO_FILE) as source:
                audio = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio, language='RU')
                return text
            except UnknownValueError:
                print("Не удаётся распознать аудио файл")
                listen(count, 3)
            except RequestError as error:
                print("Не удалось запросить результаты: {0}".format(error))
                listen(count, 3)

    def main():
        speech_ogg = SpeechOggAudioFileToText()
        text = speech_ogg.text
        print(speech_ogg.text)
        time = 2
        get_commands(text, time, filename)
    if __name__ == '__main__':
        main()


def get_commands(text, time, filename):
    if "нямка" in text or "Нямка" in text or "Привет" in text or "Прив" in text or "Даров" in text or "Хай" in text:
        if "как дела" in text or "как ты" in text or "Как у тебя дела" in text or "Как дела" in text:
            DIR = 'mood'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)
        elif "расскажи анекдот" in text or "насмеши" in text or "шутка" in text or "пошути" in text:
            DIR = 'anecdot'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)
        elif "ВК" in text or "ВКонтакте" in text or "в контакте" in text or "VK" in text or "vk" in text:
            webbrowser.open('https://vk.com', new=2)
            DIR = 'vk'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)
        elif "Что такое" in text or "это что" in text or "Кто такой" in text:
            text_list = text.split()
            if text_list[0] == "Дрим" or text_list[0] == "Dream":
                text_list[0] = ""
                text = " ".join(text_list)
            else:
                text = " ".join(text_list)
            webbrowser.open('http://www.google.com/search?q=' + text)
            DIR = 'finding'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)
        elif "осу" in text or "osu" in text or "Osu" in text or "Осу" in text:
            DIR = 'osu'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)
            os.startfile('game')
        elif "Спасибо" in text or "Благодарю" in text or "Спасибки" in text or "Благодарочка" in text:
            DIR = 'welcome'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)
        elif "php" in text or "PHP" in text or "шторм" in text or "storm" in text:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PhpStorm 2020.1.4.lnk')
            DIR = 'codding'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)

        else:
            DIR = 'hello'
            song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
            play(song)

    elif "как дела" in text or "как ты" in text or "Как у тебя дела" in text:
        DIR = 'mood'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "Расскажи анекдот" in text or "насмеши" in text or "шутка" in text or "пошути" in text:
        DIR = 'anecdot'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "ВК" in text or "ВКонтакте" in text or "в контакте" in text or "VK" in text or "vk" in text:
        webbrowser.open('https://vk.com', new=2)
        DIR = 'vk'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "Что такое" in text or "это что" in text or "Кто такой" in text:
        text_list = text.split()
        if text_list[0] == "Дрим" or text_list[0] == "Dream":
            text_list[0] = ""
            text = " ".join(text_list)
        else:
            text = " ".join(text_list)
        webbrowser.open('http://www.google.com/search?q=' + text)
        DIR = 'finding'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "осу" in text or "osu" in text or "Osu" in text or "Осу" in text:
        DIR = 'osu'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)
        os.startfile('game')

    elif "Спасибо" in text or "Благодарю" in text or "Спасибки" in text or "Благодарочка" in text:
        DIR = 'welcome'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "php" in text or "PHP" in text or "шторм" in text or "storm" in text:
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PhpStorm 2020.1.4.lnk')
        DIR = 'codding'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "понятно" in text or "Ага" in text or "Ясно" in text:
        DIR = 'ye'
        song = AudioSegment.from_mp3((os.path.join(DIR, random.choice(os.listdir(DIR)))))
        play(song)

    elif "Спасибо" in text or "Благодарю" in text or "Спасибки" in text or "Благодарочка" in text:
        DIR = 'welcome'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "как дела" in text or "как ты" in text or "Как у тебя дела" in text or "Как дела" in text:
        DIR = 'mood'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    elif "почисти" in text or "очисти" in text and "файлы" in text or "записи" in text:
        for file in os.listdir():
            if file.endswith(".wav"):
                os.remove(file)

        DIR = 'welcome'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    else:
        DIR = 'mistake'
        song = AudioSegment.from_mp3(os.path.join(DIR, random.choice(os.listdir(DIR))))
        play(song)

    time = 3
    listen(count, time)


while True:
    listen(count, 2)




