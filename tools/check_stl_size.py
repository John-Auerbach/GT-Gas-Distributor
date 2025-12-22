#!/usr/bin/env python3
import struct
import sys

def read_stl_binary(filename):
    with open(filename, 'rb') as f:
        # Skip header (80 bytes)
        f.read(80)
        # Read number of triangles
        num_triangles = struct.unpack('I', f.read(4))[0]
        
        min_x, max_x = float('inf'), float('-inf')
        min_y, max_y = float('inf'), float('-inf')
        min_z, max_z = float('inf'), float('-inf')
        
        # Read triangles
        for _ in range(num_triangles):
            # Skip normal (3 floats)
            f.read(12)
            # Read 3 vertices (9 floats total)
            for _ in range(3):
                x, y, z = struct.unpack('fff', f.read(12))
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
                min_z, max_z = min(min_z, z), max(max_z, z)
            # Skip attribute byte count
            f.read(2)
        
        return min_x, max_x, min_y, max_y, min_z, max_z

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else '../models/FlowDomain_Rectangular_RevB.stl'
    min_x, max_x, min_y, max_y, min_z, max_z = read_stl_binary(filename)
    print(f'X range: {min_x:.6f} to {max_x:.6f}, size: {max_x-min_x:.6f}')
    print(f'Y range: {min_y:.6f} to {max_y:.6f}, size: {max_y-min_y:.6f}')
    print(f'Z range: {min_z:.6f} to {max_z:.6f}, size: {max_z-min_z:.6f}')
    print(f'Center: X={((min_x+max_x)/2):.6f}, Y={((min_y+max_y)/2):.6f}, Z={((min_z+max_z)/2):.6f}')
