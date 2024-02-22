warning_prefix = '@!' # Used as a formatting tag to identify server warning messages when printing in app log window

import json
import os
import sys
from dataclasses import dataclass  #, fields

@dataclass
class AppSettings:
    metadata_message: str = "testMetadata"
    metadata_start_index: int = 1
    wait: int = 5
    arns: dict = None
    credentials: dict = None
    endpoint_url = "http://ivs.us-west-2.amazonaws.com/PutMetadata"
    headers = {"Content-Type": "application/json"}

    # @classmethod
    # def to_file(cls, filename="settings.json") -> None:
    #     with open(filename, 'w') as file:
    #         settings_dict = {
    #             key: getattr(cls, key) for key in cls.__annotations__
    #         }
    #         json.dump(settings_dict, file, indent=4)
    #
    #
    # @classmethod
    # def from_file(cls, filename="settings.json") -> None:
    #     try:
    #         with open(filename, 'r') as file:
    #             data = json.load(file)
    #
    #         for key, value in data.items():
    #             setattr(cls, key, value)
    #
    #     except FileNotFoundError:
    #         print(f"File not found: {filename}")
    #     except json.JSONDecodeError:
    #         print(f"Error decoding JSON file: {filename}")

    @classmethod
    def get_settings_path(cls, filename="settings.json"):
        if getattr(sys, 'frozen', False):
            # Running as bundled application
            bundle_dir = os.path.dirname(sys.executable)
            return os.path.join(bundle_dir, filename)
        else:
            # Running as script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            return os.path.join(script_dir, filename)

    @classmethod
    def to_file(cls, filename="settings.json") -> None:
        filepath = cls.get_settings_path(filename)
        with open(filepath, 'w') as file:
            settings_dict = {
                key: getattr(cls, key) for key in cls.__annotations__
            }
            json.dump(settings_dict, file, indent=4)

    @classmethod
    def from_file(cls, filename="settings.json") -> None:
        filepath = cls.get_settings_path(filename)
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)

            for key, value in data.items():
                setattr(cls, key, value)

        except FileNotFoundError:
            print(f"File not found: {filename}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON file: {filename}")


