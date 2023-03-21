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

import glob, os, threading, time
from threading import Timer

def scriptloop(): 
    abs_path = os.path.abspath(__file__)
    dirs = abs_path.split(os.path.sep)
    truncated_path = os.path.sep.join(dirs)
    script_dir = os.path.abspath(truncated_path)

    globpath = os.path.join(script_dir + "/nodes/containerinstances/*_script.py")
    script_files = glob.glob(globpath, recursive=False)
    for script_file in script_files:
        try:
            os.system(f"python {script_file}")
        except:
            print("Error while running script", script_file)
    t = threading.Timer(10, scriptloop, args=[])
    t.daemon = True # stop if the program exits
    t.start()