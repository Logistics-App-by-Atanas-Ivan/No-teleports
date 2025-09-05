from core.application_data import ApplicationData
from commands.validation_helpers import ValidationHelpers


class BaseCommand(ValidationHelpers):

    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    @property
    def params(self):
        return tuple(self._params)

    @property
    def app_data(self):
        return self.app_data

    def execute(self):
        # override in derived classes
        return ""
    




# from commands.base.base_command import BaseCommand
# from commands.validation_helpers import ValidateParamsCount


# class AddTest (BaseCommand, ValidateParamsCount):
    

#     def __init__(self, params, app_data):
#         self.validate_params_count(params,2)
#         self._group = app_data.find_test_group(params[0])
#         if self._group is None:
#             raise ValueError('Please enter a valid group ID')
#         super().__init__(params, app_data)

    
#     def execute(self):
#         description = self._params[1]
#         test = self.app_data.create_test(self._group, description)
#         return f'Test #{test.id} added to group #{self._group.id}'
    