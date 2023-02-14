def solution(bridge_length, weight, truck_weights):
    time,weight_sum = 0,0
    bridge_queue = []
    for truck in truck_weights:
        while len(bridge_queue) >= bridge_length or weight_sum + truck > weight:
            if len(bridge_queue) >= bridge_length:
                tmp = bridge_queue.pop(0)
                weight_sum -= tmp
            if weight_sum + truck > weight:
                bridge_queue.append(0)
                time += 1
        bridge_queue.append(truck)
        weight_sum += truck
        time += 1
    
    return time + bridge_length