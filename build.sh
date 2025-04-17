#!/bin/bash

# Install dependencies for ta-lib
apt-get update
apt-get install -y build-essential wget

# Download and install ta-lib
TA_LIB_VERSION="0.4.0"
wget https://github.com/mrjbq7/ta-lib/releases/download/v${TA_LIB_VERSION}/ta-lib-${TA_LIB_VERSION}-src.tar.gz
tar -xvzf ta-lib-${TA_LIB_VERSION}-src.tar.gz
cd ta-lib-${TA_LIB_VERSION}
./configure
make
make install
