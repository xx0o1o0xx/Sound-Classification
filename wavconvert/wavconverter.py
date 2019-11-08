from pydub import AudioSegment
import os
import argparse
#
#
# music_dir = "/Users/bassel/Google Drive/CMU/17-728/Sound Assignment/Music"
#
#
# formats_to_convert = ['.m4a']
#
# for (dirpath, dirnames, filenames) in os.walk(music_dir):
#     for filename in filenames:
#         if filename.endswith(tuple(formats_to_convert)):
#
#             filepath = dirpath + '/' + filename
#             (path, file_extension) = os.path.splitext(filepath)
#             file_extension_final = file_extension.replace('.', '')
#             try:
#                 track = AudioSegment.from_file(filepath,
#                         file_extension_final)
#                 wav_filename = filename.replace(file_extension_final, 'wav')
#                 wav_path = dirpath + '/' + wav_filename
#                 print('CONVERTING: ' + str(filepath))
#                 file_handle = track.export(wav_path, format='wav')
#                 os.remove(filepath)
#             except:
#                 print("ERROR CONVERTING " + str(filepath))

for i in range(1,6):
    for k in range(20):
        print(str(i)+",", end="")