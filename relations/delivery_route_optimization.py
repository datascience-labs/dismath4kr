import networkx as nx

# 도시 간 경로 생성 및 이동 시간(가중치) 추가
G = nx.Graph()
edges = [('Seoul', 'Incheon', 30),   # 30분 거리
         ('Seoul', 'Daejeon', 100),  # 100분 거리
         ('Incheon', 'Daejeon', 120), # 120분 거리
         ('Incheon', 'Busan', 300),  # 300분 거리
         ('Daejeon', 'Busan', 150)]  # 150분 거리
G.add_weighted_edges_from(edges)

# 서울에서 부산까지의 최단 경로 계산 (Dijkstra 알고리즘 사용)
shortest_path = nx.dijkstra_path(G, source='Seoul', target='Busan')
shortest_distance = nx.dijkstra_path_length(G, source='Seoul', target='Busan')

print("최단 경로:", shortest_path)
print("최단 시간:", shortest_distance, "분")

# 예상 결과: ['Seoul', 'Daejeon', 'Busan'] 경로가 최단 경로, 시간은 250분
