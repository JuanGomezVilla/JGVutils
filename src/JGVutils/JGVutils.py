# Main libraries
import sqlite3, json, os

# Class for useful methods
class Utils:
    # Method to use input in a more orderly way
    # A message, the type of result, return by default and an error message can be provided
    @staticmethod
    def input(message="", type=str, default=None, error_message=None):
        # Try to convert
        try:
            # Display a message on the screen for the user to type
            # Try to convert the content to the passed format
            # Returns the result
            return type(input(message))
        except:
            # If the error message is not null, it prints it
            if error_message is not None:
                # Print the message passed by the user
                print(error_message)
        # A default value is returned
        return default

    # Returns a dictionary or an array in JSON format, formatted, with indent, and without ordering
    @staticmethod
    def return_json(array, format=True, indent=4, sort_keys=False):
        # Format the JSON if requested
        if format:
            # Returns the formatted JSON
            return json.dumps(array, indent=indent, sort_keys=sort_keys)
        # Print the JSON without formatting
        return json.dumps(array, separators=(",", ":"), sort_keys=sort_keys)
        
# Class to create connections with a SQLite database
class SQLiteConnection:
    # Constructor to save settings
    def __init__(self, path):
        # Save settings
        self.path = path

    # Method to return if there is a connection to the database
    def is_database_connection(self):
        # Check if exists database file
        return os.path.isfile(self.path)
    
    # Carga un conjunto de comandos desde un archivo
    def load_commands(self, path_file):
        # Si existe conexión con la base de datos
        if self.is_database_connection():
            # Crea una conexión a partir de la ruta proporcionada por el usuario
            connection = sqlite3.connect(self.path)
            # Crea un cursor con la conexión
            cursor = connection.cursor()
            with open(path_file, "r") as f:
                comandos = f.read()
            cursor.executescript(comandos)
            connection.commit()
            connection.close()
            return "Correct"
        # Devuelve error si no existe conexión con la base de datos
        return "Error"

    def execute_query(self, query, args=[], type_fetch="dict", commit=False):
        try:
            connection = sqlite3.connect(self.path)
            if self.is_database_connection():
                if type_fetch == "dict":
                    connection.row_factory = sqlite3.Row
                cursor = connection.cursor()
                connection.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
                cursor.execute(query, args)
                if commit:
                    connection.commit()
                rows = cursor.fetchall()
                cursor.close()

                if type_fetch == "dict":
                    return [dict(row) for row in rows]
                return rows
        except Exception:
            pass
        return None