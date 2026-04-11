from pathlib import Path


class RAGPipeline:
    """
    Simple file-based retrieval from the local data folder.
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        self.base_path = project_root / "data"

    def load_topic_text(self, topic: str) -> list[str]:
        topic = topic.strip().lower()

        topic_to_file = {
            "glaucoma": self.base_path / "glaucoma" / "glaucoma.txt",
            "cataract": self.base_path / "cataract" / "cataract.txt",
            "amd": self.base_path / "amd" / "amd.txt",
            "dry eye": self.base_path / "dry_eye" / "dry_eye.txt",
            "acute red eye": self.base_path / "red_flags" / "red_flags.txt",
        }

        file_path = topic_to_file.get(topic)

        
        if file_path is None:
            return ["No matching knowledge found."]

        if not file_path.exists():
            return [f"File not found: {file_path}"]

        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            return ["The file is empty."]

        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        return paragraphs