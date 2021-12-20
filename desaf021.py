from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("in-the-end.mp3")
play(song)