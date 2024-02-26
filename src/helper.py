import json
import re
from datetime import datetime
import data
from gui import MainTab


def is_valid_json(json_string: str) -> bool:
    try:
        _ = json.loads(json_string)
        if isinstance(_, (dict, list)):
            return True
    except json.JSONDecodeError:
        return False


def get_credentials_form_json_string(string: str, window: MainTab) -> json or None:
    if is_valid_json(string):
        json_obj = json.loads(string)
        if 'credentials' in json_obj:
            expiration = json_obj["credentials"]["expiration"]
            expiration_converted = str(datetime.fromtimestamp(int(expiration) / 1000))
            json_obj["credentials"]["expiration"] = expiration_converted
            return json_obj["credentials"]
        else:
            window.write_to_log(f'{data.WARNING_PREFIX}Not valid JSON string!')
            return None
    else:
        window.write_to_log(f'{data.WARNING_PREFIX}Not valid JSON string!')
        return None


def credentials_to_str_for_display(creds: dict) -> str:
    """Prepares a string with the access key, secret access key, and session token for Main tab"""
    if creds is not None:
        access_key, secret_access_key, session_token, expiration = creds.values()
        credentials_string = (f"<<Expiration>>: {expiration}\n\n"
                              f"<<AccessKeyID>>: {access_key}\n\n"
                              f"<<SecretAccessKey>>: {secret_access_key}\n\n"
                              f"<<SessionToken>>:\n{session_token}")
        return credentials_string
    else:
        return ""


def now_datetime(obj: bool = False) -> datetime or str:
    """Returns now datetime in datetime object (obj=True) or str type"""
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
    if obj:
        return now
    else:
        return dt_string


def remove_from_newline(text: str) -> str:
    # Pattern to match everything after \n
    pattern = r'\n.*'

    # Substitute the pattern with an empty string
    result = re.sub(pattern, '', text)

    return result


def convert_datetime_str_to_object(datetime_str: str, str_format="%Y-%m-%d %H:%M:%S") -> datetime:
    return datetime.strptime(datetime_str, str_format)


def credentials_expired(datetime_to_check: datetime) -> bool:
    now = datetime.now()
    if now > datetime_to_check:
        return True
    else:
        return False


def time_correction(request_time: datetime, response_time: datetime) -> float:
    """The function returns the delta of two datetime objects."""
    datetime_delta = response_time - request_time
    return round(float(datetime_delta.total_seconds()), 3)


def existing_arn(name, arn) -> bool:
    res = False
    if data.AppSettings.arns:
        if (name in data.AppSettings.arns) or (arn in data.AppSettings.arns.values()):
            res = True
    return res
