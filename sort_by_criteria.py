# git 연결 여부 확인을 위한 코드입니다.

def sort_by_key(data, key):
    return sorted(data, key=lambda x: x.get(key, 0), reverse=True)

items = [
    {"name": "Cafe A", "genre": "dessert", "price": 7000, "likes": 130},
    {"name": "Cafe B", "genre": "coffee", "price": 5500, "likes": 200},
    {"name": "Cafe C", "genre": "tea", "price": 6000, "likes": 180},
]

print("? 가격순:")
for item in sort_by_key(items, "price"):
    print(item)

print("\n? 추천순:")
for item in sort_by_key(items, "likes"):
    print(item)
