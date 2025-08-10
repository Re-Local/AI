# search_engine.py
from __future__ import annotations
from typing import List, Dict, Any, Tuple
import pickle


class SearchEngine:
    """아주 단순한 자연어(부분 문자열) 검색 엔진"""

    def __init__(self) -> None:
        self.items: List[Dict[str, Any]] = []

    # ---------- 인덱스 구축 ----------
    def build(self, items: List[Dict[str, Any]]) -> None:
        """메모리에 검색 대상(items)을 저장"""
        normalized: List[Dict[str, Any]] = []
        for it in items:
            name = str(it.get("name", ""))
            tags_raw = it.get("tags", [])
            if isinstance(tags_raw, list):
                tags = [str(t) for t in tags_raw]
            else:
                tags = [str(tags_raw)] if tags_raw is not None else []
            normalized.append({**it, "name": name, "tags": tags})
        self.items = normalized

    # ---------- 저장 ----------
    def save(self, path: str) -> None:
        """현재 엔진 인스턴스를 피클로 저장"""
        with open(path, "wb") as f:
            pickle.dump(self, f)

    # ---------- 로드 ----------
    @classmethod
def load(cls, path: str) -> "SearchEngine":
    import pickle
    with open(path, "rb") as f:
        data = pickle.load(f)

    # 새 포맷: 엔진 인스턴스를 그대로 저장한 경우
    if isinstance(data, cls):
        return data

    # 옛 포맷 1: (items, vectorizer, matrix, ...) 형태의 튜플
    if isinstance(data, tuple) and len(data) >= 1:
        maybe_items = data[0]
        if isinstance(maybe_items, list) and (not maybe_items or isinstance(maybe_items[0], dict)):
            inst = cls()
            inst.build(maybe_items)
            return inst

    # 옛 포맷 2: 단순히 items 리스트만 저장된 경우
    if isinstance(data, list) and (not data or isinstance(data[0], dict)):
        inst = cls()
        inst.build(data)
        return inst

    raise TypeError(f"Unexpected data type in pickle: {type(data)}")

    # ---------- 검색 ----------
    def search(self, query: str, k: int | None = None) -> List[Dict[str, Any]]:
        """부분 문자열 기반 간단 검색"""
        q = (query or "").strip().lower()
        if not q:
            return []

        results: List[Tuple[float, Dict[str, Any]]] = []

        for it in self.items:
            score = 0.0
            if q in it["name"].lower():
                score += 2.0
            for t in it["tags"]:
                if q in t.lower():
                    score += 1.0
            if score > 0:
                results.append((score, {**it, "_score": score}))

        results.sort(key=lambda x: x[0], reverse=True)
        ranked = [enriched for _, enriched in results]
        return ranked[:k] if k is not None else ranked
