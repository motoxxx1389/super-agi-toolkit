from bubble import Toolkit

class AppBuilder(Toolkit):
    def __init__(self):
        super().__init__()
        self.name = "App Builder"
        self.description = "A tool for building apps"
        self.version = "1.0"
        self.author = "Your Name"
        self.author_email = "your_email@example.com"
        self.category = "Development"
        self.Tags = ["app", "builder", "development"]

    def get_tools(self):
        return [{'name': 'App Builder',
                'description': 'A tool for building apps',
                'version': '1.0',
                'author': 'Your Name',
                'author_email': 'your_email@example.com',
                'category': 'Development',
                'tags': ['app', 'builder', 'development'],
                'points': [{'name': 'Point 1', 'description': 'This is point 1'},
                            {'name': 'Point 2', 'description': 'This is point 2'}]}]