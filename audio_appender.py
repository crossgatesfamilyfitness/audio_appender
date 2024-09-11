import sys
print(sys.executable)

import streamlit as st
from pydub import AudioSegment
import os
import tempfile
from datetime import datetime
import io
import shutil

print(f"FFmpeg path: {shutil.which('ffmpeg')}")
print(f"FFprobe path: {shutil.which('ffprobe')}")
print(f"Current PATH: {os.environ.get('PATH')}")

class AudioProcessor:
    def __init__(self):
        self.static_audio_path = "Main_Line_AA.wav"
        self._check_ffmpeg()

    def _check_ffmpeg(self):
        if not shutil.which("ffmpeg"):
            st.error("FFmpeg is not installed or not in the system PATH. Please install FFmpeg to use this application.")
            st.stop()

    def generate_output_filename(self, operation):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{operation}_{timestamp}.wav"

    def process_audio(self, uploaded_audio, file_type, operation):
        output_filename = self.generate_output_filename(operation)
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_type}') as temp_file:
            temp_path = temp_file.name
            temp_file.write(uploaded_audio.getvalue())
        
        if file_type == 'wav':
            uploaded_audio = AudioSegment.from_wav(temp_path)
        elif file_type == 'mp3':
            uploaded_audio = AudioSegment.from_mp3(temp_path)
        elif file_type == 'm4a':
            uploaded_audio = AudioSegment.from_file(temp_path, format='m4a')
        
        # Convert to mono, set sample rate to 8000 Hz, and ensure 16-bit depth
        uploaded_audio = uploaded_audio.set_channels(1).set_frame_rate(8000).set_sample_width(2)

        if operation == "convert":
            processed_audio = uploaded_audio
        else:  # append or prepend
            static_audio = AudioSegment.from_wav(self.static_audio_path)
            static_audio = static_audio.set_channels(1).set_frame_rate(8000).set_sample_width(2)
            
            if operation == "append":
                processed_audio = uploaded_audio + static_audio
            elif operation == "prepend":
                processed_audio = static_audio + uploaded_audio

        # Export to a BytesIO object
        output_buffer = io.BytesIO()
        processed_audio.export(
            output_buffer,
            format="wav",
            parameters=["-acodec", "pcm_s16le", "-ar", "8000", "-ac", "1"]
        )
        
        os.unlink(temp_path)  # Remove the temporary file
        
        return output_buffer, output_filename

def main():
    st.title("Audio Processor")

    processor = AudioProcessor()

    uploaded_file = st.file_uploader("Choose an audio file", type=['wav', 'mp3', 'm4a'])
    
    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1].lower()
        
        operation = st.radio(
            "Choose operation",
            ("Convert", "Append to Main Line", "Prepend to Main Line")
        )
        
        if st.button("Process Audio"):
            operation_map = {
                "Convert": "convert",
                "Append to Main Line": "append",
                "Prepend to Main Line": "prepend"
            }
            output_buffer, output_filename = processor.process_audio(
                uploaded_file, 
                file_type, 
                operation_map[operation]
            )
            
            st.download_button(
                label="Download Processed Audio",
                data=output_buffer,
                file_name=output_filename,
                mime="audio/wav"
            )

if __name__ == "__main__":
    main()
