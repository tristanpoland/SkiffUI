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

from setuptools import setup, find_packages

setup(
    name='shiphelm',
    version='0.2.1',
    author='Gameplex Software',
    author_email='info@gameplexsoftware.com',
    description='A Python library built for the SkiffUI project used for interacting with Docker containers more easily',
    url='https://github.com/gameplex-software/shiphelm',
    packages=find_packages(),
    install_requires=['docker'],
)
