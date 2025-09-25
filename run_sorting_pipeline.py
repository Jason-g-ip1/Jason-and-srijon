def run_sorting_pipeline(recording_file_path, sorter_name, output_folder, remove_existing_folder=True, verbose=True):
    import spikeinterface.extractors as se
    import spikeinterface.sorters as ss

    # Extract recording and ground truth
    recording, ground_truth = se.read_mearec(recording_file_path)
    # Run sorting algorithm
    sorting = ss.run_sorter(
        sorter_name=sorter_name,
        recording=recording,
        folder=output_folder,
        remove_existing_folder=remove_existing_folder,
        verbose=verbose
    )
    return recording, ground_truth, sorting