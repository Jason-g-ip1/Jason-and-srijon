def create_analyzer_and_compute_extensions(
    sorting,
    recording,
    analyzer_folder,
    format="binary_folder",
    overwrite=True,
    extensions=None
):
    import spikeinterface.full as si
    import spikeinterface.widgets as sw
    # Create analyzer
    analyzer = si.create_sorting_analyzer(
        sorting,
        recording,
        format=format,
        folder=analyzer_folder,
        overwrite=overwrite
    )
    # Get computable extensions
    computable = analyzer.get_computable_extensions()
    print("Computable extensions:", computable)
    # Compute specified extensions
    if extensions is None:
        extensions = computable
    else:
        analyzer.compute(extensions)
    # Plot summary
    sw.plot_sorting_summary(analyzer, backend='spikeinterface_gui')
    return analyzer
