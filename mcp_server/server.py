from pathlib import Path
from fastmcp import FastMCP

mcp = FastMCP("Eyecare MCP Server")

BASE_PATH = Path(__file__).resolve().parent.parent / "data"


def load_text_file(file_path: Path) -> str:
    if not file_path.exists():
        return f"File not found: {file_path}"
    return file_path.read_text(encoding="utf-8").strip()


@mcp.tool
def search_eye_knowledge(topic: str) -> str:
    topic = topic.strip().lower()

    topic_to_file = {
        "glaucoma": BASE_PATH / "glaucoma" / "glaucoma.txt",
        "cataract": BASE_PATH / "cataract" / "cataract.txt",
        "amd": BASE_PATH / "amd" / "amd.txt",
        "dry eye": BASE_PATH / "dry_eye" / "dry_eye.txt",
        "acute red eye": BASE_PATH / "red_flags" / "red_flags.txt",
    }

    file_path = topic_to_file.get(topic)
    if file_path is None:
        return f"No knowledge source found for topic: {topic}"

    return load_text_file(file_path)


@mcp.tool
def get_red_flag_rules() -> str:
    file_path = BASE_PATH / "red_flags" / "red_flags.txt"
    return load_text_file(file_path)


@mcp.tool
def get_patient_education(topic: str) -> str:
    return search_eye_knowledge(topic)


if __name__ == "__main__":
    mcp.run()
