from cx_Freeze import setup, Executable

version_nr = "0.5.7"

setup(
    name="SMST",
    version=version_nr,
    description="Sequential Metadata Sending Tool",
    executables=[Executable("gui.py", base=None, target_name="SMST "+version_nr)],
)
