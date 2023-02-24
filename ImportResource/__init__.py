from robotlibcore import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.api import logger
from pathlib import Path
import os

__version__ = 0.2


class ImportResource():
    """ImportResource library provides a wrapper to robotframework so that
    one can use and distribute resource files via python packages.

    For example: if you install python package `foo` via pip that contains a directory `rf-resources`
    you can import all of the resource files into your test suite via

    | `Library` | ImportResource |

    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    resources = []


    def __init__(self):

        try:
            self.rf = BuiltIn()
        except RobotNotRunningError:
            pass

        resource_files = self._find_resources(Path(os.path.dirname(__file__)))
        if resource_files:
            for resource_file in resource_files:
                try:
                    self.rf.import_resource(resource_file)
                except RobotNotRunningError:
                    pass
                self.resources.append(resource_file)
        else:
            logger.warn(f"Module did't contain any resource files")
            
    @keyword
    def external_resources(self):
        """Returns the list of loaded resource file"""
        return [str(item) for item in self.resources]

    def _find_resources(self, module_path):
        return module_path.rglob("*.resource")
