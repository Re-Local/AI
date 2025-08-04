from datetime import datetime

# 0. 기본 정렬: 평점*0.6 - 거리*0.4 (평점이 높을수록, 거리가 가까울수록 위에 뜨도록 설계)
def calculate_score_default(content, weight_rating=0.6, weight_distance=0.4):
    return (content.get("rating", 0) * weight_rating) - (content.get("distance_km", 0) * weight_distance)

def sort_by_default(contents):
    return sorted(contents, key=calculate_score_default, reverse=True)

# 1. 사용자 평점 높은 순
def sort_by_rating_high(contents):
    return sorted(contents, key=lambda x: x.get("rating", 0), reverse=True)

# 2. 사용자 평점 낮은 순
def sort_by_rating_low(contents):
    return sorted(contents, key=lambda x: x.get("rating", 0))

# 3. 현재 위치에서 가까운 순
def sort_by_distance(contents):
    return sorted(contents, key=lambda x: x.get("distance_km", float("inf")))

# 4. 최근 등록순 (가장 최근 날짜가 위로)
def sort_by_recent(contents):
    return sorted(contents, key=lambda x: x.get("created_at", ""), reverse=True)

# 5. 인기순 (조회수 or 클릭 수 기준)
def sort_by_popularity(contents):
    return sorted(contents, key=lambda x: x.get("views", 0), reverse=True)

# 6. 체험 시간까지 남은 시간 순 (남은 시간이 적은 순)
def sort_by_time_remaining(contents):
    now = datetime.now()
    return sorted(contents, key=lambda x: (datetime.strptime(x.get("start_time", "2999-12-31 23:59"), "%Y-%m-%d %H:%M") - now).total_seconds())

# 7. 가격 낮은 순
def sort_by_price(contents):
    return sorted(contents, key=lambda x: x.get("price", float("inf")))

# 8. 영어 지원 여부 (영어 설명이 있는 콘텐츠가 먼저)
def sort_by_english_support(contents):
    return sorted(contents, key=lambda x: x.get("has_english", False), reverse=True)

# 9. 개인화 추천 점수 (사용자 선호 태그 기반) → 나중에 구현
def sort_by_personal_recommendation(contents, user_tags):
    def score(item):
        tag_match_count = sum(tag in user_tags for tag in item.get("tags", []))
        return (tag_match_count, item.get("rating", 0))  # 태그 수가 동일하면, 평점이 높은게 위에 가도록 설계.
    return sorted(contents, key=score, reverse=True)


