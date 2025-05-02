# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import copy
import datetime
from typing import Any, Dict
import dateutil.relativedelta
import sympy
import numpy
import uuid

import subprocess


class GenericRuntime:
    GLOBAL_DICT = {}
    LOCAL_DICT = None
    HEADERS = []
    def __init__(self):
        self._global_vars = copy.copy(self.GLOBAL_DICT)
        self._local_vars = copy.copy(self.LOCAL_DICT) if self.LOCAL_DICT else None
        
        for c in self.HEADERS:
            self.exec_code(c)
        
    def exec_code(self, code_piece: str) -> None:
        exec(code_piece, self._global_vars)
        
    def eval_code(self, expr: str) -> Any:
        return eval(expr, self._global_vars)
    
    def inject(self, var_dict: Dict[str, Any]) -> None:
        for k, v in var_dict.items():
            self._global_vars[k] = v
    
    @property
    def answer(self):
        return self._global_vars['answer']

    
class PythonRuntime(GenericRuntime):
    GLOBAL_DICT = {
        'datetime': datetime.datetime, 
        'timedelta': dateutil.relativedelta.relativedelta,
        'relativedelta': dateutil.relativedelta.relativedelta,
        'sympy': sympy,
        'numpy': numpy
    }


class JavaRuntime(GenericRuntime):
    GLOBAL_DICT = {}
    LOCAL_DICT = None
    HEADERS = []

    IMPORTS = ["java.util.ArrayList",
               "java.util.Comparator",
               "java.util.HashMap",
               "java.time.LocalDateTime",
               "java.time.format.DateTimeFormatter"]

    def __init__(self):
        pass
        
    def exec_code(self, code_piece: str) -> None:

        random_uuid = uuid.uuid1()

        subprocess.run(["mkdir", "-p", str(random_uuid)])

        # Setup imports
        code = "\n".join(["import " + i + ";" for i in self.IMPORTS]) + code_piece

        subprocess.run(["cp", "/dev/stdin", f"{str(random_uuid)}/Solution.java"], input=code, text=True)
        subprocess.run(["javac", f"{str(random_uuid)}/Solution.java"])
        result = subprocess.run(["java", "-cp", f"{str(random_uuid)}", "Solution"], capture_output=True)

        # Print to stdout so we can grab it in Python
        print(result.stdout.decode(), end="")
        subprocess.run(["rm", "-rf", str(random_uuid)])

    def eval_code(self, expr: str) -> Any:
        raise NotImplementedError()
    
    def inject(self, var_dict: Dict[str, Any]) -> None:
        raise NotImplementedError()
    
    @property
    def answer(self):
        raise NotImplementedError()
    
    @property
    def _global_vars(self):
        raise NotImplementedError()
    
    @property
    def _local_vars(self):
        raise NotImplementedError()
    

RUNTIME_DICT = {
    "Python": PythonRuntime,
    "Java": JavaRuntime
}