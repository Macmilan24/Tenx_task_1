import json
import os


def validate_mcp_config(file_path: str):
    """Checks if the mcp.json is formatted correctly for Tenx."""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        data = json.load(f)
        if "tenxfeedbackanalytics" in data.get("servers", {}):
            print("✅ Tenx server found in configuration.")
            headers = data["servers"]["tenxfeedbackanalytics"].get("headers", {})
            if "X-Device" in headers and "X-Coding-Tool" in headers:
                print("✅ Required headers are present.")
            else:
                print("❌ Missing required headers.")
        else:
            print("❌ Tenx server configuration missing.")


if __name__ == "__main__":
    validate_mcp_config(".vscode/mcp.json")
