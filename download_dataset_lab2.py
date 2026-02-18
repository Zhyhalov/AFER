import kagglehub

# Download latest version
path = kagglehub.dataset_download("developerghost/water-potability")

print("Path to dataset files:", path)