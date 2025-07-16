# Mapping of polyhedron name to number of faces
faces_map = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

# Read input
n = int(input())
total_faces = 0

# Loop through each polyhedron and sum the faces
for _ in range(n):
    polyhedron = input().strip()
    total_faces += faces_map[polyhedron]

# Output the total number of faces
print(total_faces)
