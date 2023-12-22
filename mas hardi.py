# # Dimensions of the container yard
# yard_width = 240  # meters
# yard_length = 1200  # meters

# # Dimensions of the containers
# container_width = 2.4  # meters
# container_length = 1.2  # meters

# # Initialize the yard with empty spaces
# yard = [[' ' for _ in range(yard_width)] for _ in range(yard_length)]

# # List to store the locations of containers
# container_locations = []

# # Function to check if a location is occupied by a container
# def is_occupied(x, y):
#     for container_id, cx, cy in container_locations:
#         if x >= cx and x < cx + int(container_width * 10) and y >= cy and y < cy + int(container_length * 10):
#             return True
#     return False

# # Function to place a container sequentially in the yard
# def place_container(container_id):
#     for y in range(yard_length):
#         for x in range(yard_width):
#             if not is_occupied(x, y):
#                 # Check if there's enough space for the container
#                 if x + int(container_width * 10) <= yard_width:
#                     for i in range(int(container_length * 10)):
#                         for j in range(int(container_width * 10)):
#                             yard[y + i][x + j] = container_id
#                     # Record container location
#                     container_locations.append((container_id, x, y))
#                     return


# # Simulasi pengisian lapangan kontainer secara berurutan
# num_containers = (yard_length * yard_width) // (container_width * container_length)
# for container_id in range(1, int(num_containers + 1)):
#     # Coba tempatkan kontainer
#     place_container(container_id)

#     # Jika tidak ada lagi ruang di lapangan untuk kontainer, keluar dari loop
#     if len(container_locations) == num_containers:
#         break

#     # Cetak lapangan kontainer setelah menempatkan setiap kontainer
#     print("Lapangan Setelah Menempatkan Kontainer", container_id)
#     for row in yard:
#         # Konversi container_id menjadi string sebelum mencetak
#         print(' '.join(str(cell) for cell in row))

#     # Cetak lokasi kontainer setelah menempatkan setiap kontainer
#     print("Lokasi Kontainer:")
#     for container_id, x, y in container_locations:
#         print(f"Kontainer {container_id} berada di (x={x}, y={y})")

# # Cetak lapangan kontainer akhir
# print("Lapangan Kontainer Akhir:")
# for row in yard:
#     # Konversi container_id menjadi string sebelum mencetak
#     print(' '.join(str(cell) for cell in row))

# Dimensions of the container yard
yard_width = 240  # meters
yard_length = 1200  # meters

# Dimensions of the containers
container_width = 2.4  # meters
container_length = 1.2  # meters

# Initialize the yard with empty spaces
yard = [[' ' for _ in range(yard_width)] for _ in range(yard_length)]

# List to store the locations of containers
container_locations = []

# Function to place a container sequentially in the yard
def place_container(container_id):
    for y in range(yard_length):
        for x in range(yard_width):
            if yard[y][x] == ' ':
                # Check if there's enough space for the container
                if x + int(container_width * 10) <= yard_width:
                    for i in range(int(container_length * 10)):
                        for j in range(int(container_width * 10)):
                            yard[y + i][x + j] = container_id
                    # Record container location
                    container_locations.append((container_id, x, y))
                    return

# Simulate filling the container yard sequentially
num_containers = (yard_length * yard_width) // (container_width * container_length)
for container_id in range(1, int(num_containers + 1)):
    place_container(container_id)

# Print the container yard
for row in yard:
    print(' '.join(row))

# Print container locations
print("Container Locations:")
for container_id, x, y in container_locations:
    print(f"Container {container_id} is located at (x={x}, y={y})")

place_container(container_id)
