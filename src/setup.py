from cx_Freeze import setup, Executable

setup(
    name="SMST",
    version="0.5.2",
    description="Sequential Metadata Sending Tool",
    executables=[Executable("gui.py", base=None, target_name="SMST")]
)



