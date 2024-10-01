"""
Copyright © 2024 Datasciencelabs.org . All rights reserved.

This code is protected under copyright law and may be used under the following conditions:

1. Use, modification, and distribution of this code are permitted for personal or non-commercial purposes only.
2. Commercial use of this code is prohibited without the prior written permission of the copyright holder.
3. Any modified or redistributed versions of this code must retain this copyright notice.
4. The copyright holder is not liable for any damages or issues that arise from the use of this code.

For further inquiries, please contact: sjchun@dau.ac.kr
"""

import networkx as nx

# 클라우드 리소스 네트워크 생성 (각 노드: 데이터 센터, 엣지: 전송 비용)
G = nx.Graph()
edges = [('DataCenter_NY', 'DataCenter_LA', 300),  # 뉴욕에서 LA로 전송 비용: 300
         ('DataCenter_NY', 'DataCenter_Tokyo', 700),  # 뉴욕에서 도쿄로 전송 비용: 700
         ('DataCenter_LA', 'DataCenter_Tokyo', 500),  # LA에서 도쿄로 전송 비용: 500
         ('DataCenter_LA', 'DataCenter_Sydney', 800), # LA에서 시드니로 전송 비용: 800
         ('DataCenter_Tokyo', 'DataCenter_Sydney', 400)] # 도쿄에서 시드니로 전송 비용: 400

G.add_weighted_edges_from(edges)

# 뉴욕에서 시드니까지의 최적 경로와 비용 계산
optimal_path = nx.dijkstra_path(G, source='DataCenter_NY', target='DataCenter_Sydney')
optimal_cost = nx.dijkstra_path_length(G, source='DataCenter_NY', target='DataCenter_Sydney')

print("최적 경로:", optimal_path)
print("최적 비용:", optimal_cost, "단위 비용")

# 예상 결과: ['DataCenter_NY', 'DataCenter_LA', 'DataCenter_Tokyo', 'DataCenter_Sydney'] 경로가 최적, 비용은 1200 단위 비용
