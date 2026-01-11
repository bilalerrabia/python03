import math


def parse_coordinates(coordinate_str: str, origin=(0, 0, 0)):
    try:
        coords = [int(c) for c in coordinate_str.split(",")]
        if len(coords) != 3:
            raise IndexError("Coordinate must have exactly 3 values")
        x1, y1, z1 = coords
        x2, y2, z2 = origin
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        coordinate_tuple = tuple(coords)
        print(f'Parsing coordinates: "{coordinate_str}"')
        print(f"Parsed position: {coordinate_tuple}")
        print(
            f"Distance between {origin} and"
            f"{coordinate_tuple}: {round(distance, 2)}"
        )
        return coordinate_tuple, distance
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None
    except IndexError as e:
        print(f"Error: {e}")
        return None


print("=== Game Coordinate System ===\n")
origin = (0, 0, 0)


coordinate = (10, 20, 5)
x, y, z = coordinate
distance = math.sqrt((x - 0)**2 + (y - 0)**2 + (z - 0)**2)
print(f"Position created: {coordinate}")
print(f"Distance between {origin} and {coordinate}: {round(distance, 2)}\n")


coordinate_str = "3,4,0"
parse_coordinates(coordinate_str, origin)


print('\nParsing invalid coordinates: "abc,def,ghi"')
parse_coordinates("abc,def,ghi", origin)


print("\nUnpacking demonstration:")
coordinate_tuple = (3, 4, 0)
x, y, z = coordinate_tuple
print(f"Player at x={x}, y={y}, z={z}")
print(
    f"Coordinates: X={coordinate_tuple[0]},"
    f"Y={coordinate_tuple[1]},"
    f"Z={coordinate_tuple[2]}"
    )
