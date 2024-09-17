#!/bin/bash

# Check if the script is run as root.
if [ "$EUID" -ne 0 ]
then
    echo "Please run the script as root."
    exit
fi

$service_name="sensor-autostart"
$script_path="$(pwd)/main.py"

# Verify that the provided script path exists.
if [ ! -f "$script_path" ]
then
    echo "The provided path doesn't exist."
    exit
fi

# Create the systemd service file content.
service_content="[Service]
ExecStart=/usr/bin/poetry run python $script_path
User=$SUDO_USER

[Install]
WantedBy=multi-user.target"

# Define the service file path.
service_file_path="/usr/lib/systemd/system/$service_name.service"

# Write the content to the service file.
echo "$service_content" > "$service_file_path"

# Reload systemd to recognize new service.
systemctl daemon-reload

# Enable the service.
systemctl enable $service_name.service

echo "Service '$service_name' created and enabled successfully!"
