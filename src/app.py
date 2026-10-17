from src.extract import extract_data
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_data

def run_pipeline(file_path):
    data=extract_data(file_path)
    data=transform_data(data)
    validate_data(data)
    load_data(data)
    
    return {
        "status": "success",
        "filename": file_path.name,
        "records_processed": len(data)
    }