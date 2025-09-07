import os
print("=" * 50)
print("PATH DEBUG INFORMATION")
print("=" * 50)
print("Current working directory:", os.getcwd())
print("BASE_DIR should be:", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("=" * 50)

# Check templates path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_path = os.path.join(base_dir, 'templates')
print("Templates path:", templates_path)
print("Templates exists:", os.path.exists(templates_path))

if os.path.exists(templates_path):
    print("Files in templates folder:", os.listdir(templates_path))
    relationship_app_path = os.path.join(templates_path, 'relationship_app')
    if os.path.exists(relationship_app_path):
        print("Files in relationship_app:", os.listdir(relationship_app_path))
    else:
        print("relationship_app folder does NOT exist!")
else:
    print("Templates folder does NOT exist!")

print("=" * 50)