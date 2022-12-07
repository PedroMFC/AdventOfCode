
def read_input(file_name: str) -> list[str]:
    datastream = '' 
    
    with open(file_name) as file:
        for line in file:
            datastream += line

    return datastream

def get_marker_start(datastream: str, group_length: int) -> int:
    marker_start = 0


    for i in range(len(datastream)):
        group = datastream[marker_start: marker_start + group_length]
        non_repeated_characters = set([*group])
        if len(non_repeated_characters) == group_length:
            marker_start += group_length
            break
        marker_start +=1

    return marker_start



def main() -> None:
    datastream = read_input('2022/day6/input.txt')

    packet_start = get_marker_start(datastream, 4)

    print(f'characters before the first start-of-packet marker is detected: {packet_start}')

    message_start = get_marker_start(datastream, 14)

    print(f'characters before the first start-of-message marker is detected: {message_start}')

if __name__ == "__main__":
    main()