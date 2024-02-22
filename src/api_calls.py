import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
import time
import helper
import json
import data
from gui import MainTab

def get_arn_by_name(window: MainTab, settings: data.AppSettings) -> str:
    selected_arn_name = window.selected_arn.get()
    selected_arn = settings.arns[selected_arn_name]
    return selected_arn

def send_metadata(window: MainTab, settings: data.AppSettings) -> None:
    window.write_to_log("Started")

    check_interval = 0.1  # Check the stop_flag every 0.1 seconds

    selected_arn = get_arn_by_name(window, settings) # get arn selected in main tab
    send_interval = settings.wait # 'delay' from settings tab
    metadata_index = settings.metadata_start_index # 'index' from settings tab
    message = settings.metadata_message
    credentials = settings.credentials
    cred_values = tuple(credentials.values())[:3] # extracting values for access_key, secret_access_key, session_token

    # Define the access key, secret access key, and session token
    access_key, secret_access_key, session_token = cred_values

    # Define the API endpoint URL
    endpoint_url = data.AppSettings.endpoint_url

    # Define the headers
    headers = data.AppSettings.headers

    if all((access_key, secret_access_key, session_token)):
        # Create an instance of AWSRequestsAuth
        auth = create_auth_instance(access_key, secret_access_key, session_token)

        try:
            print("S----------------")
            # Make the API calls
            while not window.stop_flag: # window.stop_flag = True
                # Define the custom request body
                request_body = {
                    "channelArn": selected_arn,
                    "metadata": f"{message}_{metadata_index}"
                }

                request_time = helper.now_datetime(obj=True) # get request time

                # window.write_to_log(f"Sending: {request_body['metadata']}")

                response = requests.post(endpoint_url, json=request_body, headers=headers, auth=auth)


                response_time = helper.now_datetime(obj=True) # get response time

                # print("Response: ", response_time, response.headers) # use later for delay/wait time correction

                message_from_response = get_message_from_response(response, window)

                window.write_to_log(message_from_response)

                metadata_index += 1

                # Correct send_interval according to request->response delay time
                time_correction = helper.time_correction(request_time, response_time)

                corrected_send_interval = max(send_interval - time_correction, 0) # this also ensures that the result >=0
                print(request_time, response_time)
                print("Time correction: ", time_correction)
                print("Send interval (corrected): ", corrected_send_interval)

                for _ in range(int(corrected_send_interval / check_interval)):
                    if window.stop_flag:
                        break
                    time.sleep(check_interval)

                print("Time after sleep: ", helper.now_datetime())
        finally:
            print("F----------------")
            window.write_to_log("Stopped")
            window.stop_action()

def create_auth_instance(access_key, secret_access_key, session_token):
    auth = AWSRequestsAuth(
        aws_access_key=access_key,
        aws_secret_access_key=secret_access_key,
        aws_token=session_token,
        aws_host="ivs.us-west-2.amazonaws.com",
        aws_region="us-west-2",
        aws_service="ivs"
    )
    return auth

def main(window: MainTab, settings: data.AppSettings) -> None:
    if settings.credentials is not None:
        send_metadata(window, settings)
    else:
        window.write_to_log(f"{data.warning_prefix}Please provide credentials")
        window.stop_action(window.json_entry)

def get_message_from_response(response, window: MainTab) -> str:
    if response.text:
        try:
            response_text_json = json.loads(response.text, strict=False)

            # Convert all keys to lowercase for case-insensitive matching
            lowercase_data = {key.lower(): value for key, value in response_text_json.items()}

            # Try to get the value associated with the key 'message'
            message = lowercase_data.get('message')
            cleared_message = f"{data.warning_prefix}{helper.remove_from_newline(message)}"

            if cleared_message is not None:
                window.stop_action()
                return cleared_message
            else:
                window.stop_action()
                return f"{data.warning_prefix}No message found in the response."
        except json.JSONDecodeError as e:
            window.stop_action()
            return f"{data.warning_prefix}Error decoding response.text JSON: {e}"
    else:
        return f"{json.loads(response.request.body.decode('utf-8'))['metadata']}"


if __name__ == '__main__':
    pass