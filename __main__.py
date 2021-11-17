from pysndfx import AudioEffectsChain
import yt2wav

if __name__ == '__main__':
    yt2wav.get("https://www.youtube.com/watch?v=d_XOcqur-XU", 'bigcheese.wav')

    fx = (
        AudioEffectsChain()
        .reverb(reverberance=100)
    )

    infile = 'bigcheese.wav'
    outfile = 'my_processed_audio_file.wav'

    # Apply reverb directly to an audio file
    print("Applying reverb to bigcheese.wav and saving as my_processed_audio_file.wav")
    fx(infile, outfile)
