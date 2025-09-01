import bpy
import bmesh
import mathutils
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create icosahedron
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=0, radius=2, location=(0, 0, 0))
bit_mesh = bpy.context.active_object
bit_mesh.name = "TRON_Bit"

# Switch to Edit mode to access vertices
bpy.context.view_layer.objects.active = bit_mesh
bpy.ops.object.mode_set(mode='EDIT')

# Get the mesh data
bm = bmesh.from_mesh(bit_mesh.data)
bm.faces.ensure_lookup_table()
bm.verts.ensure_lookup_table()

# Store original vertex positions
original_positions = [v.co.copy() for v in bm.verts]

# Update mesh and return to Object mode
bmesh.to_mesh(bm, bit_mesh.data)
bm.free()
bpy.ops.object.mode_set(mode='OBJECT')

# Add material for crystalline look
material = bpy.data.materials.new(name="Bit_Material")
material.use_nodes = True
nodes = material.node_tree.nodes
links = material.node_tree.links

# Clear default nodes
nodes.clear()

# Add shader nodes
output_node = nodes.new(type='ShaderNodeOutputMaterial')
principled_node = nodes.new(type='ShaderNodeBsdfPrincipled')
emission_node = nodes.new(type='ShaderNodeEmission')
mix_node = nodes.new(type='ShaderNodeMixShader')

# Set material properties for crystalline look
principled_node.inputs['Base Color'].default_value = (0.0, 0.8, 1.0, 1.0)  # Cyan
principled_node.inputs['Metallic'].default_value = 0.8
principled_node.inputs['Roughness'].default_value = 0.1
principled_node.inputs['IOR'].default_value = 2.4  # Glass-like

# Add glow
emission_node.inputs['Color'].default_value = (0.0, 1.0, 1.0, 1.0)  # Cyan glow
emission_node.inputs['Strength'].default_value = 0.5

# Connect nodes
links.new(principled_node.outputs['BSDF'], mix_node.inputs[1])
links.new(emission_node.outputs['Emission'], mix_node.inputs[2])
links.new(mix_node.outputs['Shader'], output_node.inputs['Surface'])
mix_node.inputs['Fac'].default_value = 0.1

# Assign material to object
bit_mesh.data.materials.append(material)

# Set up animation - vertex morphing
frame_start = 1
frame_end = 120

# Set frame range
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end
bpy.context.scene.frame_set(frame_start)

print("Setting up vertex morphing animation...")

# Create shape keys for vertex morphing
bit_mesh.shape_key_add(name="Basis")  # Base shape
morph_key = bit_mesh.shape_key_add(name="Morph")  # Morphed shape

# Animate the shape key for breathing/morphing effect
morph_key.value = 0.0
morph_key.keyframe_insert(data_path="value", frame=frame_start)

morph_key.value = 1.0
morph_key.keyframe_insert(data_path="value", frame=frame_end // 2)

morph_key.value = 0.0
morph_key.keyframe_insert(data_path="value", frame=frame_end)

# Set interpolation to smooth
for fcurve in bpy.context.active_object.data.shape_keys.animation_data.action.fcurves:
    for keyframe in fcurve.keyframe_points:
        keyframe.interpolation = 'SINE'

# Modify the morph shape key vertices for breathing effect
bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_mesh(bit_mesh.data)
bm.verts.ensure_lookup_table()

# Move vertices outward for morphing effect
for i, vert in enumerate(bm.verts):
    # Calculate outward direction (normalized position)
    direction = vert.co.normalized()
    
    # Different oscillation per vertex for complex morphing
    offset_factor = 0.3 + 0.2 * math.sin(i * 0.8)  # Vary per vertex
    
    # Store morphed position in shape key
    morph_position = vert.co + direction * offset_factor
    
    # This will be applied to the shape key data
    morph_key.data[i].co = morph_position

bmesh.to_mesh(bm, bit_mesh.data)
bm.free()
bpy.ops.object.mode_set(mode='OBJECT')

# Add rotation animation
bit_mesh.rotation_euler = (0, 0, 0)
bit_mesh.keyframe_insert(data_path="rotation_euler", frame=frame_start)

bit_mesh.rotation_euler = (math.radians(360), math.radians(540), math.radians(180))
bit_mesh.keyframe_insert(data_path="rotation_euler", frame=frame_end)

# Set rotation interpolation to linear
if bit_mesh.animation_data and bit_mesh.animation_data.action:
    for fcurve in bit_mesh.animation_data.action.fcurves:
        if 'rotation_euler' in fcurve.data_path:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'LINEAR'

# Add lighting
bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
sun_light = bpy.context.active_object
sun_light.data.energy = 3
sun_light.data.color = (1.0, 1.0, 1.0)

# Add fill light
bpy.ops.object.light_add(type='AREA', location=(-3, -3, 5))
fill_light = bpy.context.active_object
fill_light.data.energy = 2
fill_light.data.color = (0.5, 0.8, 1.0)  # Slightly blue

# Set up camera
bpy.ops.object.camera_add(location=(0, -8, 3))
camera = bpy.context.active_object
camera.rotation_euler = (math.radians(70), 0, 0)

# Set camera as active
bpy.context.scene.camera = camera

# Set render settings for preview
bpy.context.scene.render.engine = 'EEVEE'
bpy.context.scene.eevee.use_bloom = True
bpy.context.scene.eevee.bloom_intensity = 0.5

# Set background to dark
world = bpy.context.scene.world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.01, 0.01, 0.05, 1.0)

print("TRON Bit created successfully!")
print("- Icosahedron with 12 vertices, 20 faces")
print("- Vertex morphing animation using shape keys")
print("- Crystalline material with glow")
print("- 120 frame animation loop")
print("Press SPACE to play animation!")