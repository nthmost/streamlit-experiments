import os
import sys

CMD = "say -v {voice} -o '{title}.wav' --file-format WAVE --data-format I16 {content}"

def text_to_wav(title, content, voice="Moira"):
    title = title.strip()
    content = content.strip()
    print(f"Generating {title}.wav")
    os.popen(CMD.format(title=title, content=content, voice=voice))


if __name__=='__main__':
    try:
        fname = sys.argv[1]
    except:
        print("Supply a filename as the first argument to this script.")
        sys.exit()
    try:
        voice = sys.argv[2]
    except:
        voice = None

    #skip the top line containing the column headings.
    lines = open(fname).readlines()[1:]
    for line in lines:
        line = line.strip()
        title, content = line.split(',', 1)
        if voice:
            text_to_wav(title, content, voice)
        else:
            text_to_wav(title, content)

