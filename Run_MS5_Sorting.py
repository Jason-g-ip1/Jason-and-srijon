# Import spikeinterface things
import spikeinterface.full as si
import spikeinterface.extractors as se
import spikeinterface.sorters as ss
import spikeinterface.widgets as sw
import matplotlib.pyplot as plt
import spikeinterface.comparison as sc
from run_sorting_pipeline import run_sorting_pipeline
from create_analyzer_and_compute_extensions import create_analyzer_and_compute_extensions
#add MEArec recording file path
recording_file_path = "3_20Neuron10SecondRecordingWithLevel3Noise.h5"
sorter_name = "mountainsort5"
#define output fodler
output_folder = "ms5_output"
#run sorting
recording, ground_truth, sorting = run_sorting_pipeline(recording_file_path, sorter_name, output_folder)
#run ground truth comparison
gt_comp = sc.compare_sorter_to_ground_truth(ground_truth, sorting, exhaustive_gt=True)
perf = gt_comp.get_performance()
print(perf)


# Define folder to save analyzer to
analyzer_folder = "/Users/jasonip/Spikeinterface/analyzer"
extensions_to_compute = [
	'random_spikes', 'waveforms', 'templates', 'noise_levels',
	'correlograms', 'spike_amplitudes', 'unit_locations', 'template_similarity'
	# Define extensions to compute; set to None to compute all available extensions
]
analyzer = create_analyzer_and_compute_extensions(
	sorting,
	recording,
	analyzer_folder,
	format="binary_folder",
	overwrite=True,
	extensions=extensions_to_compute
)


