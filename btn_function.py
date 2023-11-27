from tkinter import Frame

from main_page import (pomodoro, vocab_learn, note_taking, video_downloader, progress, book_list, movie_list,
                       journaling, takeaway, saved_later, remainder_tasks, buid_something, entertainment, learn_new)

TITLE_FONT: tuple[str, int, str] = ("Arial", 18, "bold")


def pomodoro_clicked(frame:Frame, content: str = 'This is pomodoro content'):
    # frame.update()
    pomodoro.pomodoro_func(frame, content, title_font=TITLE_FONT)


def english_vocabs(frame, content: str = "English words"):
    vocab_learn.vocabulary_words(frame, content=content, title_font=TITLE_FONT)


def note_taker(frame: Frame):
    note_taking.take_notes(frame, title_font=TITLE_FONT)


def todo_list(frame: Frame):
    note_taking.take_notes(frame, title_font=TITLE_FONT)


def vid_downloader(frame: Frame):
    video_downloader.video_downloader(frame, title_font=TITLE_FONT)


def track_progress_clicked(frame: Frame):
    progress.progress_tracking(frame)


def book_list_clicked(frame: Frame):
    book_list.reading_list(frame)


def watchlist_clicked(frame: Frame):
    movie_list.watching_list(frame)


def journal_clicked(frame: Frame):
    journaling.journal(frame)


def takeaway_clicked(frame: Frame):
    takeaway.take_away(frame)


def save_later_clicked(frame: Frame):
    saved_later.save_for_later(frame)


def remainder_clicked(frame: Frame):
    remainder_tasks.remainder_task(frame)


def build_something(frame: Frame):
    buid_something.build_something_task(frame)


def learn_new_clicked(frame: Frame):
    learn_new.learning_new_daily(frame)


def entertainment_clicked(frame: Frame):
    entertainment.entertainment_2day(frame)


def dummy_click(frame: Frame):
    print('btn clicked')
