# !/usr/bin/env python
"""This is the main driver file."""

from scripts.preprocess import PrepareData
from scripts.sound_source_localization import SoundSourceLocation
from scripts.determine_source import DetermineSourceLocation


def main():
    head = '/home/akhil/Heart-Sounds-Localization/data/heart sound/raw/'
    method_name = 'SRP'

    test_data = PrepareData(head).load_file()

    for _ in range(2):
        sample_mic_signal_loc_dict, s1_or_not, sound_cycle = next(test_data)
        source_estimates = SoundSourceLocation(method_name,
                                               s1_bool=s1_or_not).run_estimates(sample_mic_signal_loc_dict)
        ts1 = DetermineSourceLocation(method_name, sound_cycle,
                                      *source_estimates,
                                      s1_bool=s1_or_not).sprint()


if __name__ == '__main__':
    main()
