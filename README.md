# Audio Processor

This Streamlit application allows users to process audio files in various ways. Users can upload audio files (WAV, MP3, or M4A), and then choose to either convert the audio to a specific format, append it to a static audio file, or prepend it to a static audio file.

## Features

- Upload audio files (WAV, MP3, M4A)
- Convert audio to mono, 8000 Hz sample rate, 16-bit depth
- Append uploaded audio to a static audio file
- Prepend uploaded audio to a static audio file
- Download processed audio files

## Requirements

- Python 3.7+
- Streamlit
- PyDub
- ffmpeg

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/audio-processor.git
   cd audio-processor
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Ensure you have ffmpeg installed on your system. If not, install it using your system's package manager or download it from the [official ffmpeg website](https://ffmpeg.org/download.html).

## Usage

1. Run the Streamlit app:

   ```
   streamlit run audio_appender.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Upload an audio file using the file uploader.

4. Choose the operation you want to perform (Convert, Append, or Prepend).

5. Click the "Process Audio" button.

6. Download the processed audio file using the download button that appears.

## File Structure

- `audio_appender.py`: Main application file
- `requirements.txt`: List of Python dependencies
- `Main_Line_AA.wav`: Static audio file used for append/prepend operations (not included in repository)

## Deployment

This app can be deployed on Streamlit Cloud or any other Python-compatible hosting platform. Make sure to include all necessary files and set up the environment according to the `requirements.txt` file.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/audio-processor/issues) if you want to contribute.

## Author

Your Name - [Your Email]

Project Link: [https://github.com/yourusername/audio-processor](https://github.com/yourusername/audio-processor)
