# main_search.py

from pathlib import Path
from search_engine import SearchEngine

# 경로 설정
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INDEX_DIR = ROOT / "index"
INDEX_FILE = INDEX_DIR / "search_index.pkl"

# 인덱스 파일 확인
if not INDEX_FILE.exists():
    raise FileNotFoundError("인덱스 파일이 없습니다. 먼저 build_index.py를 실행하세요.")

# 인덱스 로드
engine = SearchEngine.load(str(INDEX_FILE))  # ✅ 이제 tuple이 아니라 SearchEngine 객체 반환

# 검색 실행
query = input("검색어를 입력하세요: ")
results = engine.search(query)

# 결과 출력
if results:
    print("\n검색 결과:")
    for r in results:
        print("-", r)
else:
    print("검색 결과가 없습니다.")


