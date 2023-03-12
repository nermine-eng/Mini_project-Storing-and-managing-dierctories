# Mini_project-Storing-and-managing-dierctories
The implementation of a shared directory service using a client/server model, where one or more text files will be stored. This will be a standard OSI client-server application.
The application server is responsible for storing and managing directories. Each directory is associated with a user who has an account and contains the following fields: name, first name, mobile phone number, postal address, and email address. (Name, first name, and email address fields are mandatory.)

Directories are organized hierarchically and not in the form of a table or database. They are designed to be consulted, modified, deleted, and created.

Each user's information will be listed in their directory along with their permissions. In this way, a protected file can only be accessed by a user with the necessary permissions. Once authenticated, the user can access the requested resource provided they have the necessary authorizations. For example, to view another directory, permission must be requested from the other user. This is not the case for the administrator, who has the privilege of accessing all accounts without restrictions.

We will develop the code for three Python functions and their unit tests:

    Creation_Compte: function to create a user account by the administrator.

    Ajout_Contact: function to add a contact to the directory by the user.

    Recherche_Contact: function to search for a contact in a user's directory.

