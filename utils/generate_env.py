import os

def generate_env_file():
    env_file_content = """SECRET_KEY=
DB_HOST=
DB_PORT=
DB_USERNAME=
DB_PASSWORD=
FLASK_ENV=production
FLASK_RUN_PORT=6000
FLASK_RUN_HOST=localhost
FLASK_DEBUG=0
"""
    root_path = os.path.dirname(os.path.abspath(__file__))  
    env_file_path = os.path.join(root_path, '..', '.env') 

    with open(env_file_path, 'w') as env_file:
        env_file.write(env_file_content)

if __name__ == "__main__":
    generate_env_file()
