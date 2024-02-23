#!/bin/bash

# Define GitHub repository owner and name
owner="zigobuko"
repo="test_22-02-2024"

# Create temp folder
temp_folder=$(mktemp -d)

# Get the latest release information
release_info=$(curl -s "https://api.github.com/repos/$owner/$repo/releases/latest")

# Extract download URL for the zip file containing "SMST" in its name
download_url=$(echo "$release_info" | grep -o '"browser_download_url": ".*SMST.*\.zip"' | cut -d '"' -f 4)

# Check if download URL is empty (i.e., if no matching zip file was found)
if [ -z "$download_url" ]; then
    echo "No zip file containing 'SMST' in its name found in the latest release."
    exit 1
fi

# Extract file name from the download URL
filename=$(basename "$download_url")

# Download the zip file to the temp folder within the Downloads folder
curl -sSL "$download_url" -o "$temp_folder/$filename"

# Unzip the downloaded file to the temp folder
unzip -q -d "$temp_folder" "$temp_folder/$filename"

# Remove the downloaded zip file
rm "$temp_folder/$filename"

# Find the file with ".app" extension in the temp folder
app_file=$(find "$temp_folder" -maxdepth 1 -type d -name "*.app")

if [ -z "$app_file" ]; then
    echo "No .app file found in the downloaded zip."
    rm -rf "$temp_folder"
    exit 1
fi

# Check if the same file exists in the Downloads folder
if [ -e ~/Downloads/"$(basename "$app_file")" ]; then
    echo "File $(basename "$app_file") already exists in Downloads."
    # Delete the temp folder
    rm -rf "$temp_folder"
    exit
else
    # Move the .app file from temp folder to Downloads folder
    mv "$app_file" ~/Downloads/
fi

# Delete the temp folder
rm -rf "$temp_folder"

echo "Downloaded and extracted successfully."
