from models.package import Package

# from models.test_group import TestGroup


class ModelsFactory:
    def __init__(self):
        self._route_id = 1
        self._package_id = 1
        self._trucks = self._create_truck()

    def create_package(self, start_location, end_location, weight, user):
        package_id = self._package_id
        self._package_id += 1
        return Package(package_id, start_location, end_location, weight, user)

    def create_route(self):
        pass 

    def create_user(self, email):
        pass

    def create_truck(self):
        pass

    # def create_group(self, name: str):
    #     group_id = self._test_group_id
    #     self._test_group_id += 1

    #     return TestGroup(group_id, name)

    # def create_test(self, description: str):
    #     test_id = self._test_id
    #     self._test_id += 1

    #     return Test(test_id, description)
