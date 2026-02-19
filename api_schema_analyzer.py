import json
from swaggerparser import parser

class APISchemaAnalyzer:
    def __init__(self):
        self.parsed_schemas = {}

    def parse_swagger(self, swagger_file_path):
        """Parse a Swagger/OpenAPI file and return its schema representation."""
        try:
            with open(swagger_file_path) as f:
                data = json.load(f)
                parsed_schema = parser.parse(data)
                self.parsed_schemas[swagger_file_path] = parsed_schema
                return parsed_schema
        except Exception as e:
            raise ValueError(f"Failed to parse Swagger file: {e}")

    def get_resource_parameters(self, resource_path):
        """Retrieve parameters for a specific API resource."""
        try:
            if resource_path in self.parsed_schemas:
                return self.parsed_schemas[resource_path].get_operation(resource_path)
            else:
                raise FileNotFoundError("Resource path not found in schema.")
        except Exception as e:
            raise ValueError(f"Error retrieving parameters: {e}")