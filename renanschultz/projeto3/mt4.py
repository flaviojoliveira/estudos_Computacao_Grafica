  
import bpy

for i in range (-9, 10, 3):
    bpy.ops.mesh.primitive_cube_add(location=(i,0,0))
    bpy.ops.mesh.primitive_uv_sphere_add(location=(i,0,3))
