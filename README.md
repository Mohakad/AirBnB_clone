 AirBnB clone project

Description of the project

	The goal of the project is to deploy on our server a simple copy of the AirBnB website.

	For now the application is composed by A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

	In this task 
		We will put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
		Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
		Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
		Create the first abstracted storage engine of the project: File storage.
		Create all unittests to validate all our classes and storage engine

Description of the command interpreter

	It is exactly the same with shell but limmited to a specific use-case.

	In this task 
		We will Create a new object (ex: a new User or a new Place)
		Retrieve an object from a file, a database etc…
		Do operations on objects (count, compute stats, etc…)
		Update attributes of an object
		Destroy an object

