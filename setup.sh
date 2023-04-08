# ----------------------------------------------------------------------------
# SkiffUI Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

# Install curl and git
sudo apt-get install curl git

# Install Python3.9 and pip as well as other deps
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
sudo apt-get install python3.9-distutils
sudo apt-get install libgtk-3-dev gettext python3.9-dev build-essential

# Install the required pip dependancies
python3.9 build.py

# Move to src directory
cd ./src/

# Install the customized gsnodegraph library
python3.9 -m pip install -r ./gsnodegraph/

# Start the app
python3.9 ./main.py