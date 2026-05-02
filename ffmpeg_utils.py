# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_path, output_path, title="", author="", description=""):
    try:
        stream = ffmpeg.input(input_path)

        stream = ffmpeg.output(
            stream,
            output_path,
            codec="copy",
            metadata=f"title={title}",
            metadata=f"artist={author}",
            metadata=f"description={description}"
        )

        ffmpeg.run(stream, overwrite_output=True)
        return output_path

    except Exception as e:
        print("FFmpeg error:", e)
        return input_path

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
