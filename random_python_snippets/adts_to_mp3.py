from pydub import AudioSegment

# Load the .aac file
aac_file = AudioSegment.from_file("audio.aac", format="aac")

# Export the file as an mp3
aac_file.export("audio.mp3", format="mp3")
