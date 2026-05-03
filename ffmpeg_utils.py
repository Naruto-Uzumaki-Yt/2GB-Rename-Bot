# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_path, output_path,
                 title="", author="", artist="",
                 audio="", subtitle="", video=""):

    try:
        stream = ffmpeg.input(input_path)

        metadata = {}

        if title: metadata["title"] = title
        if author: metadata["artist"] = author
        if artist: metadata["album_artist"] = artist
        if audio: metadata["comment"] = audio
        if subtitle: metadata["subtitle"] = subtitle
        if video: metadata["description"] = video

        out = ffmpeg.output(
            stream,
            output_path,
            vcodec="copy",
            acodec="copy",
            **{f"metadata:g": f"{k}={v}" for k, v in metadata.items()}
        )

        ffmpeg.run(out, overwrite_output=True, quiet=True)

        return output_path

    except Exception as e:
        print("FFmpeg Error:", e)
        return input_path

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
