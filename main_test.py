import json
from sort_by_criteria import (
    sort_by_default,
    sort_by_rating_high,
    sort_by_rating_low,
    sort_by_distance,
    sort_by_recent,
    sort_by_popularity,
    sort_by_time_remaining,
    sort_by_price,
    sort_by_english_support,
    sort_by_personal_recommendation
)

# sample_data.json에서 콘텐츠 불러오기
with open("sample_data.json", "r", encoding="utf-8") as f:
    contents = json.load(f)

# user_tags.json에서 사용자 태그 불러오기
with open("user_tags.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)
    user_tags = user_data.get("user_tags", [])

# 사용자 선택 기준
print("정렬 기준을 선택하세요:")
print("0: 기본 정렬 (평점*0.6 - 거리*0.4)")
print("1: 사용자 평점 높은 순")
print("2: 사용자 평점 낮은 순")
print("3: 현재 위치에서 가까운 순")
print("4: 최근 등록순")
print("5: 인기순")
print("6: 체험 시작 시간까지 남은 시간 순")
print("7: 가격순")
print("8: 영어 지원 여부")
print("9: 개인화 추천 순")

try:
    choice = int(input("정렬 번호를 입력하세요 (0-9): "))
except ValueError:
    print("유효한 숫자를 입력해주세요.")
    exit()

# 정렬 함수 매핑
sort_functions = {
    0: sort_by_default,
    1: sort_by_rating_high,
    2: sort_by_rating_low,
    3: sort_by_distance,
    4: sort_by_recent,
    5: sort_by_popularity,
    6: sort_by_time_remaining,
    7: sort_by_price,
    8: sort_by_english_support,
    9: lambda contents: sort_by_personal_recommendation(contents, user_tags)
}

# 정렬 수행
if choice not in sort_functions:
    print("0부터 9 사이의 숫자를 입력해주세요.")
else:
    sorted_contents = sort_functions[choice](contents)

    print("\n정렬 결과:")
    for item in sorted_contents:
        print(f"- {item['name']} | 평점: {item['rating']} | 거리: {item['distance_km']}km | 태그: {item['tags']}")

