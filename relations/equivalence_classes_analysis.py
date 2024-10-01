"""
Copyright © 2024 Datasciencelabs.org . All rights reserved.

This code is protected under copyright law and may be used under the following conditions:

1. Use, modification, and distribution of this code are permitted for personal or non-commercial purposes only.
2. Commercial use of this code is prohibited without the prior written permission of the copyright holder.
3. Any modified or redistributed versions of this code must retain this copyright notice.
4. The copyright holder is not liable for any damages or issues that arise from the use of this code.

For further inquiries, please contact: sjchun@dau.ac.kr
"""

# 동치 관계를 정의하는 함수
def equivalence_relation(a, b):
    # 예시: 길이가 같으면 같은 동치류로 간주
    return len(a) == len(b)

# 주어진 집합을 동치 관계에 따라 유사한 그룹(동치류)으로 분류하는 함수
def find_equivalence_classes(data_set, relation):
    equivalence_classes = []

    # 이미 처리한 항목을 기록하는 리스트
    processed = set()

    for item in data_set:
        if item in processed:
            continue

        # 동치 관계를 만족하는 그룹(동치류)을 찾음
        equivalence_class = [x for x in data_set if relation(item, x)]
        equivalence_classes.append(equivalence_class)

        # 해당 그룹의 모든 항목을 처리된 것으로 표시
        processed.update(equivalence_class)

    return equivalence_classes

# 예시 집합
data_set = ['apple', 'banana', 'grape', 'kiwi', 'mango', 'pear']

# 동치류 찾기
equivalence_classes = find_equivalence_classes(data_set, equivalence_relation)

# 결과 출력
print("동치 관계에 따른 유사성 분석 결과 (동치류):")
for idx, eq_class in enumerate(equivalence_classes, 1):
    print(f"동치류 {idx}: {eq_class}")
