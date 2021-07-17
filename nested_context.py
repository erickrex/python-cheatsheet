def copy(src, dst):
    """Copy the contents of one file to another.

    Args:
        src (str): File name of the file to be copied.
        dst (str): Where to write the new file.
    """

    # Open both files
    with open(src) as f_src:
        with open(dst, 'w') as f_dst:
            # Read and write each line, one at a time
            for line in f_src:
                f_dst.write(line)
