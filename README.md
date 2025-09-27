# No-teleports

The application will be used by employees of a large Australian company aiming to expand its
activities to the freight industry. The app will be used to manage the delivery of packages between
hubs in major Australian cities. An employee of the company must be able to record the details of a
delivery package, create or search for suitable delivery routes, and inspect the current state of
delivery packages, transport vehicles and delivery routes.

```
Login manager1@telerikacademy.com 123456
CreateUser regular1@telerikacademy.com Gosho Goshev 123456 Regular
Logout
Login regular1@telerikacademy.com 123456
CreateCustomer John Doe john_doe@gmail.com
CreateCustomer Petar Petrov p_petrov@gmail.com
CreatePackage Brisbane Sydney 500 john_doe@gmail.com
CreatePackage Brisbane Melbourne 5000 p_petrov@gmail.com
ViewUnassignedPackagesAtLocation Brisbane
CreateRoute Brisbane Sydney Melbourne
FindTruck 1
AssignTruck 1001 1
BulkAssignAtLocation 1 Brisbane
CreatePackage Sydney Melbourne 45 john_doe@gmail.com
FindSuitableRoute 3
AddPackage 3 1
CreatePackage Brisbane Melbourne 10000 p_petrov@gmail.com
FindPackage 1
FindPackage 2
FindPackage 3
FindPackage 4
ViewDeliveryRoutes
Logout
Login manager1@telerikacademy.com 123456
ViewDeliveryRoutes




Login manager1@telerikacademy.com 123456
CreateCustomer John Doe john_doe@gmail.com
CreatePackage Brisbane Sydney 500 john_doe@gmail.com
FindPackage 1