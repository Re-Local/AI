from pathlib import Path
import json
from search_engine import SearchEngine

HERE = Path(__file__).resolve().parent
DATA = HERE / "sample_data.json"
ROOT = HERE.parent  # 프로젝트 루트
INDEX_DIR = ROOT / "index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)

with open(DATA, "r", encoding="utf-8") as f:
    items = json.load(f)

engine = SearchEngine()
engine.build(items)
engine.save(str(INDEX_DIR / "search_index.pkl"))

print(f"✅ 인덱스 생성 완료: {INDEX_DIR / 'search_index.pkl'}")
