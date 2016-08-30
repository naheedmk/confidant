# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name="confidant",
    version="1.1.15",
    packages=find_packages(exclude=["test*"]),
    package_data={
        'confidant': ['confidant/dist/*', 'requirements.txt']
    },
    install_requires=reqs,
    author="Ryan Lane",
    author_email="rlane@lyft.com",
    description="A secret management system and client.",
    license="apache2",
    url="https://github.com/lyft/confidant"
)