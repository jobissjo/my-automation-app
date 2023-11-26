from tkinter import Frame

from main_page import pomodoro, vocab_learn, note_taking, video_downloader

TITLE_FONT: tuple[str, int, str] = ("Arial", 18, "bold")


def pomodoro_clicked(frame, content: str = 'This is pomodoro content'):
    pomodoro.pomodoro_func(frame, content, title_font=TITLE_FONT)


def english_vocabs(frame, content: str = "English words"):
    vocab_learn.vocabulary_words(frame, content=content, title_font=TITLE_FONT)


def note_taker(frame: Frame):
    note_taking.take_notes(frame, title_font=TITLE_FONT)


def vid_downloader(frame: Frame):
    video_downloader.video_downloader(frame, title_font=TITLE_FONT)


def dummy_click(frame:Frame):
    print('btn clicked')
