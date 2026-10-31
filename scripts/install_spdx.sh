#!/bin/bash
# Install SPDX tools for license validation

echo "Installing SPDX tools..."
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install spdx-tools

echo "SPDX tools installed. Verify with: spdx-cli --version"