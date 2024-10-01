"""
Copyright © 2024 Datasciencelabs.org . All rights reserved.

This code is protected under copyright law and may be used under the following conditions:

1. Use, modification, and distribution of this code are permitted for personal or non-commercial purposes only.
2. Commercial use of this code is prohibited without the prior written permission of the copyright holder.
3. Any modified or redistributed versions of this code must retain this copyright notice.
4. The copyright holder is not liable for any damages or issues that arise from the use of this code.

For further inquiries, please contact: sjchun@dau.ac.kr
"""

# 일대일 함수: 서로 다른 입력을 서로 다른 출력으로 매핑
def injective_function(input_data):
    # 중복 없는 값들의 리스트로 변환 (일대일)
    return {item: index for index, item in enumerate(input_data)}

# 전사 함수: 출력 집합의 모든 값이 적어도 하나의 입력과 매핑되도록 구현
def surjective_function(mapping_dict, input_data):
    # 모든 입력 데이터를 일대일로 변환 후, 해당 출력 값을 다시 원본으로 복원
    inverse_mapping = {v: k for k, v in mapping_dict.items()}
    return [inverse_mapping[mapping_dict[item]] for item in input_data]

# 예시 데이터
input_data = ['apple', 'banana', 'cherry', 'date', 'banana', 'apple']

# 1. 일대일 함수 적용: 중복 없이 데이터를 변환
mapping_dict = injective_function(input_data)
print("일대일 함수에 의한 변환:", mapping_dict)

# 2. 전사 함수 적용: 변환된 데이터로부터 원본 데이터 복원
restored_data = surjective_function(mapping_dict, input_data)
print("복원된 데이터:", restored_data)
