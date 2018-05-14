from pkg_resources import resource_filename

def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    import pkg_resources

    with open(resource_filename('ety', 'package_data.dat'), 'r') as f:
        print(f.read())

