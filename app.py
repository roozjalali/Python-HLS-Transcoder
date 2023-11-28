import subprocess
import os

def create_vod_hls(source, target):
    if not source:
        raise ValueError("Source file is required")

    renditions = [
        "426x240    400k    128k",
        "640x360    800k     128k",
        "842x480    1400k    128k",
        "1280x720   2800k    128k",
        "1920x1080  5000k    192k"
    ]

    # Generate encryption key
    print('Generating encryption key')
    key_file = f"{target}.key"
    key_info_file = f"{target}.keyinfo"
    with open(key_file, "wb") as f:
        f.write(os.urandom(16))
    key_iv = os.urandom(16).hex()
    key_uri = "key_uri_placeholder"  # Replace with actual key URI if needed
    key_info_content = f"{key_uri}/{key_file}\n{key_file}\n{key_iv}"
    with open(key_info_file, "w") as f:
        f.write(key_info_content)

    static_params = "-keyint_min 96 -x264opts keyint=96:min-keyint=96:no-scenecut -g 96 -r:v 24 -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 3.0 -c:a aac -ac 1 -ar 48000 -b:a 96k -hls_time 4 -hls_playlist_type vod -hls_key_info_file " + key_info_file
    misc_params = "-hide_banner -y"

    master_playlist = "#EXTM3U\n#EXT-X-VERSION:3\n"

    for rendition in renditions:
        resolution, bitrate, audiorate = rendition.split()

        height = resolution.split('x')[1]
        name = f"{height}p"
        bandwidth = int(bitrate.rstrip('k')) * 1000

        cmd = f"{static_params} -s {resolution} -b:v {bitrate} -b:a {audiorate} -hls_segment_filename {target}/{name}_%03d.ts {target}/{name}.m3u8"
        master_playlist += f"#EXT-X-STREAM-INF:BANDWIDTH={bandwidth},RESOLUTION={resolution}\n{name}.m3u8\n"

        print(f"Converting {source} to {name}")
        subprocess.run(f"ffmpeg {misc_params} -i {source} {cmd}", shell=True, check=True)

    with open(f"{target}/playlist.m3u8", "w") as f:
        f.write(master_playlist)

    print(f"Done - encoded HLS is at {target}/")

# Example usage
source_file = "bunny.mp4"
output_name = "output_directory"
create_vod_hls(source_file, output_name)
