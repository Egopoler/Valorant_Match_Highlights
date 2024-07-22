import moviepy.editor




def make_timelines(indexes):
    last_index = indexes[-1]
    timelines = []
    start = indexes[0]
    end = indexes[0]
    for index in indexes:
        if index - end <= 1:
            end = index
        else:
            timelines.append((start, end))
            start = index
            end = index
    return timelines

def make_video(video_path, output_path, time_lines):
    clips = []
    general_clip = moviepy.editor.VideoFileClip(video_path)
    for time_line in time_lines:
        clip = general_clip.subclip(time_line[0], time_line[1])
        clips.append(clip)

    final_clip = moviepy.editor.concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)