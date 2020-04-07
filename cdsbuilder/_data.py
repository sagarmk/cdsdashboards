"""Get the data files for this package."""


def get_data_files():
    """Walk up until we find share/cdsbuilder"""
    import sys
    from os.path import join, abspath, dirname, exists, split

    path = abspath(dirname(__file__))
    starting_points = [path]
    if not path.startswith(sys.prefix):
        starting_points.append(sys.prefix)
    for path in starting_points:
        # walk up, looking for prefix/share/cdsbuilder
        while path != '/':
            share_cdsbuilder = join(path, 'share', 'cdsbuilder')
            static = join(share_cdsbuilder, 'static')
            if all(exists(join(static, f)) for f in ['components', 'css']):
                return share_cdsbuilder
            path, _ = split(path)
    # didn't find it, give up
    return ''


# Package managers can just override this with the appropriate constant
DATA_FILES_PATH = get_data_files()
