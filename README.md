![main_tab_demo_.png](images%2Fmain_tab_demo_.png)
## Introduction

The Sequential Metadata Sending Tool (SMST) is a standalone graphical user interface (GUI) application designed for Twitch IVS player core project QEs.  
Its purpose is to speed up and simplify the test setup and execution process for regression tests that involve sending metadata to an IVS live channel.  
This tool eliminates the need to use Postman and allows test engineers to focus on player testing instead of performing manual actions to send metadata. The result is a significant reduction in test execution time.

## Features

- Few clicks to start
- Super simple and easy to use interface
- Ability to customize parameters (if required)
- Displays the expiration time of the credentials
- Logs field to monitor sent messages and other info
- Displays server response messages in case of errors instead of response codes (more human friendly)
- Save multiple channels and choose which one to use in session
- Automatic saving of user settings

<br/><br/>

## Getting Started

### Download the application:

#### macOS

Run in Terminal.app:

```bash
curl -sSL https://raw.githubusercontent.com/zigobuko/test_22-02-2024/main/download_latest_release.sh | bash
```

The latest version of the application will be downloaded to your Downloads folder.  
You can run the application directly from the Downloads folder or move it to your preferred location (e.g. desktop).

<br/><br/>

## How to use

### Pre-requisites
Live-streaming IVS channel is required.  
The corresponding test documentation provides detailed information, but in short, you need to have an AWS account, create an IVS channel, and run a live stream on that channel for testing.
<br/><br/>
### First-time open (Settings tab)
![settings_tab_first_open.png](images%2Fsettings_tab_first_open.png)

The first time you open the application, you will be taken to the Settings tab.  
You need to add a channel to send metadata to (see the appropriate QA documentation for where to find your IVS channel ARN).

- Enter your channel ARN to the "Channel ARN" field
- Enter a name for the ARN in the 'Channel Name' field. You may choose any name you prefer
- Click "Add Item" button to save ARN

The channel will be saved, and the next time you open the application, you won't need to add the channel again.
<br/><br/>
### Sending metadata (Main tab)
![main_tab_.png](images%2Fmain_tab_.png)

Make sure your IVS channel is broadcasting.
- Copy the JSON string containing temporary credentials for your AWS account from the Isengard AWS Console Access (see the appropriate QA documentation for details)
- On the SMST Main tab, paste the JSON string into the 'Credentials JSON string' field and click 'Submit'.
- Click "Start" to start sending metadata.
<br/><br/>
### Other options

#### Main Tab
![main_tab_warnings.png](images%2Fmain_tab_warnings.png)
- If you have saved multiple channels in the application settings, you can choose which channel to send metadata to from the Channel drop-down list.
- In Credentials field you can see credentials + their expiration time. You can scroll this field up/down.
- You can clear credentials. After that you'll need to provide credentials to SMST again.
- Logs field displays sent metadata messages, application messages and server response messages in case of error. You can scroll this field up and down.
- When you open the application, if the credentials you used in the previous session have not expired, they will be automatically loaded into the application. In this case, you don't need to do anything else, just click the Start button to send the metadata. 

#### Settings Tab
![settings_tab.png](images%2Fsettings_tab.png)
- In the Message field, you can change the message you want to send 
- Incremental index is added to each metadata message. You can change the start index in the Start index field.
- In the Delay field you can set the time between metadata messages (2-10 sec)
- You can save several channels in the application. Saved channels are available in the Channel drop-down list on the Main tab.
- Click the channel in the table to move it up/down in the list or remove it using the corresponding buttons.
- All your settings are saved and will be available the next time you open the application.
