# Copyright 2014 Yummy Melon Software
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Charles Y. Choi

EXEC=nota
INSTALL_DIR=${HOME}/bin

install: ${INSTALL_DIR}
	cp ${EXEC}.py ${INSTALL_DIR}/${EXEC}
	chmod uog+x ${INSTALL_DIR}/${EXEC}

