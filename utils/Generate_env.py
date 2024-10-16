import os

def generate_env_file():
    env_file_content = """SECRET_KEY=
DB_HOST=
DB_PORT=5432
DB_USERNAME=
DB_PASSWORD=
"""
    root_path = os.path.dirname(os.path.abspath(__file__))  
    env_file_path = os.path.join(root_path, '..', '.env') 

    with open(env_file_path, 'w') as env_file:
        env_file.write(env_file_content)

if __name__ == "__main__":
    generate_env_file()
