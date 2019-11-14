from pydub import AudioSegment
import os
import argparse
import scipy.io.wavfile as wavfile
import numpy as np

music_dir = "/Users/bassel/Google Drive/CMU/17-728/Sound Assignment/Alarm"


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

# for i in range(1,6):
#     for k in range(20):
#         print(str(i)+",", end="")

b_fs,b_y = wavfile.read(music_dir+"/alarm.wav")

print(b_y.shape)

one=np.array(b_y[0:1440000])
print(one.shape)

wavfile.write(music_dir+"/alarm1.wav", b_fs, one)
start = 0
count = 12
while (start+1440000) < b_y.shape[0]:
    wavfile.write(music_dir+"/alarm"+str(count)+".wav", b_fs, b_y[start:(start+1440000)])
    start += 1440000
    count += 1
