#!/usr/bin/python
from __future__ import print_function
from getting_midi_from_string import StringConverter
from keras.models import load_model
from text_model import generate_song_stateful
import sys
from os import system

model = load_model('model_dump.h5py')

model.load_weights('text_model_saved.h5py')

divercity = 0.5
file_path = 'out.mid'
if len(sys.argv) > 1:
    print('saving to:', sys.argv[1])
    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        divercity = float(sys.argv[2])
else:
    print("No file path given. Saving to out.mid")


print("Generating song")
converter = StringConverter(generate_song_stateful(divercity))


tmp_path = 'tmp/' + file_path.split('/')[-1].split('.')[0]+'.mid'

if file_path.endswith('.mid'):
    converter.save(file_path)
else:
    converter.save(tmp_path)
    system('./convert_to_mp3.sh ' + tmp_path + ' ' + file_path)
