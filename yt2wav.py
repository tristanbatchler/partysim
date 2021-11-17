import youtube_dl
import subprocess
import time
import os


def get(url: str, outfile: str = '%(id)s.wav') -> None:
    """
    Downloads the youtube video at the URL provided and saves it in the root directory of this project as a .wav file.
    Provide an optional filename argument, e.g. 'sample.wav' to control the name of the resulting file.
    """

    # For now, we want the intermediary file to be m4a and we'll convert to wav after
    intermediate = f"{outfile}.{time.time()}"

    ydl_opts = {
        'outtmpl': intermediate,
        'format': 'bestaudio/best'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        audio = ydl.extract_info(url)

    print(f"Finished downloading {intermediate}")

    # We now know the real filename
    outfile_name = '.'.join(outfile.split('.')[:-1])
    if outfile_name == '%(id)s':
        outfile_name = audio['id']
    outfile_ext = outfile.split('.')[-1]
    outfile = f"{outfile_name}.{outfile_ext}"

    print(f"Converting {intermediate} to wav and saving as {outfile}")
    process = subprocess.Popen(['ffmpeg', '-i', intermediate, outfile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout, stderr)

    print(f"Cleaning up intermediate file {intermediate}")
    os.remove(intermediate)
