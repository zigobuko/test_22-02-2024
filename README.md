![main_tab_demo.png](images%2Fmain_tab_demo.png)
## Introduction

Sequential Metadata Sending Tool (SMST) is a standalone GUI application, designed for Twitch IVS-player-core project QEs  
to speed up and simplify the test setup and execution process for regression tests that involve sending metadata to an IVS Live channel.  
This tool eliminates the need to use Postman for this purpose, and allows the test engineer to focus on player testing,  
rather than performing manual actions to send metadata, significantly reducing test execution time.

## Features

- Few-click startup
- Super simple and easy to use interface
- Ability to customize parameters (if needed)
- Displays credential expiration time
- Logs field to monitor sent messages and other info
- Shows server response messages in case of errors instead of response codes (more human friendly)
- Save multiple ARNs and choose which one to use in session
- Automatic saving of user settings

## Getting Started

### Installation

Download the application:

#### macOS

Run in Terminal.app

```bash
curl -sSL https://raw.githubusercontent.com/zigobuko/test_22-02-2024/main/download_latest_release.sh | bash
```

The latest application version will be downloaded to your Downloads folder.  
You can run the application directly from the Downloads folder or move it to your preferred location (e.g. desktop).

### How to use

#### Pre-requisites
Live-streaming IVS channel is required.  
The corresponding test documentation provides detailed information, but in short, you need to have an AWS account,  
create an IVS channel, and run a live stream on that channel for testing.

#### First-time open
![first_open_settings_tab.png](images%2Ffirst_open_settings_tab.png)
The first time you open the application, you will be taken to the Settings tab. 
You need to add channel to send metadata to.

- Enter channel ARN to the corresponding field
- Enter a name for the ARN in the 'Channel Name' field. You may choose any name you prefer
- Click "Add Item" button to save ARN
- Navigate to the Main tab
 
#### Sending metadata
![main_tab.png](images%2Fmain_tab.png)
Make sure your IVS channel is broadcasting.
- Copy the JSON string containing temporary credentials for your AWS account from the Isengard AWS Console Access
- On the SMST Main tab, paste the JSON string into the 'Credentials JSON string' field and click 'Submit'.
- Click "Start" to start sending metadata.



#### Additional information

