import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_smooth()
esfera1= bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,5))
esfera2 = bpy.context.object

material=bpy.data.materials.new('brilhante')
material.diffuse_color=(0,1,0)
material.specular_color=(0,1,0)
material.diffuse_intensity=0.5
material.specular_intensity=0.5

esfera1.data.materials.append(material)
esfera2.data.materials.append(material)
