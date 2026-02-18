import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/weather-data")

print("Path to dataset files:", path)