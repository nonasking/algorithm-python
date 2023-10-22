# 캐시(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/17680


def solution(cacheSize, cities):
    result = 0
    cache = {}
    for i in range(len(cities)):
        cities_lowercase = cities[i].lower()
        if cities_lowercase in cache:
            result += 1
        else:
            result += 5
        cache[cities_lowercase] = i
        if len(cache) > cacheSize:
            cache.pop(min(cache, key=cache.get), None)
    return result