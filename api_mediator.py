import importlib
from .api_schema_analyzer import APISchemaAnalyzer
from .auto_bridge_generator import AutoBridgeGenerator

class APIMediator:
    def __init__(self):
        self.analyzer = APISchemaAnalyzer()
        self.bridges = {}

    def connect_apis(self, api_profile1, api_profile2):
        """Connect two APIs by generating and caching the bridge."""
        try:
            # Load API schemas
            schema1 = self.analyzer.parse_swagger(api_profile1['schema_path'])
            schema2 = self.analyzer.parse_swagger(api_profile2['schema_path'])

            # Generate bridge
            generator = AutoBridgeGenerator(schema1, schema2)
            bridge_func = generator.generate_bridge_code()

            # Cache the bridge
            self.bridges[(api_profile1['id'], api_profile2['id'])] = bridge_func

            return True
        except Exception as e:
            raise ConnectionError(f"Failed to connect APIs: {e}")

    def mediate_request(self, request, source_id, target_id):
        """Mediate a request through the generated bridge."""
        try:
            # Retrieve the appropriate bridge
            bridge = self.bridges.get((source_id, target_id))
            if not bridge:
                raise ValueError("No active bridge found.")

            response = bridge(request)
            return response
        except Exception as e:
            raise RuntimeError(f"Mediation failed: {e}")