from core.command_factory import CommandFactory
from core.application_data import ApplicationData


class Engine:
    def __init__(self, factory: CommandFactory, appdata:ApplicationData,file_path):
        self._command_factory = factory
        self._app_data = appdata
        self._file_path = file_path

    def start(self):

        output = []
        
        print('available operations')

        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':

                    break

                command = self._command_factory.create(input_line)

                print(command.execute())
                
                self._app_data.save_state(self._file_path) 
                
            except ValueError as err:
                # output.append(err.args[0])
                print(err.args[0])

        # print('\n'.join(output))
