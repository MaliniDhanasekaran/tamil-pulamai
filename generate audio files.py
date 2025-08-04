import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 100)  # Set speech rate

# Tamil letters
uyir_eluthugal = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
mei_eluthugal = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்", "ன்"]
uyirmei_eluthugal = ["க", "கா", "கி", "கீ", "கு", "கூ", "கெ", "கே", "கை", "கொ", "கோ", "கௌ"]

# Folder to save audio
output_folder = "audio_offline"
os.makedirs(output_folder, exist_ok=True)

# Function to save audio
def generate_audio(letter_list, prefix):
    for letter in letter_list:
        filename = os.path.join(output_folder, f"{prefix}_{letter}.mp3")
        print(f"Generating: {filename}")
        engine.save_to_file(letter, filename)

# Generate audio for all types
generate_audio(uyir_eluthugal, "uyir")
generate_audio(mei_eluthugal, "mei")
generate_audio(uyirmei_eluthugal, "uyirmei")

engine.runAndWait()
print("✅ All audio files generated in 'audio_offline/' folder.")
