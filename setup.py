import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent Django are
# still present in site-packages. See #18115.
overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    print(lib_paths)
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "rocky"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break

# version = __import__(PACKAGE_NAME).get_version()

setup(
    name='rocky',
    version='0.0.1',
    url='https://github.com/RockyLiys/',
    author='Pip_test Software Foundation',
    author_email='liys_liys@163.com',
    description=('A high-level Python core  that encourages '),
    license='',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    keywords=["rocky"],

)
if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
"""
)
