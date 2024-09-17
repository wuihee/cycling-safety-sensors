#!/bin/bash

# Check if the script is run as root.
if [ "$EUID" -ne 0 ]
then
    echo "Please run the script as root."
    exit
fi

service_name="sensor_autostart"

# Create the systemd service file content.
service_content="[Service]
WorkingDirectory=$(pwd)
ExecStart=/home/pi/.local/bin/poetry run python main.py
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
