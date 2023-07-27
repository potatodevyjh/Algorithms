def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [0] * bridge_length

    while bridge:  ##list가 존재할때까지
        answer += 1
        bridge.pop(0)
        if truck_weights: ##truck_weights가 존재할때까지
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))

            else:
                bridge.append(0)

    return answer


from collections import deque

def solution2(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(t for t in truck_weights)
    answer = 0
    bridge_weight = 0
    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))