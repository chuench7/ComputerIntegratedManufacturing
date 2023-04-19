import bpy

# Create the box1
bpy.ops.mesh.primitive_cube_add(size=1)
box1 = bpy.context.object
box1.scale = (1, 1, 1)
box1.location = (0, 0, 0)

# Create the lid1
bpy.ops.mesh.primitive_cube_add(size=1)
lid1 = bpy.context.object
lid1.scale = (1.2, 1.2, 0.1)
lid1.location = (0, 0, 0.5)

# Create the box2
bpy.ops.mesh.primitive_cube_add(size=2)
box2 = bpy.context.object
box2.location = (3, 0, 0)

# Create the lid2
bpy.ops.mesh.primitive_cube_add(size=2)
lid2 = bpy.context.object
lid2.scale = (1.2, 1.2, 0.1)
lid2.location = (3, 0, 1)


# Join the box and the lid
bpy.ops.object.select_all(action='DESELECT')
box1.select_set(True)
lid1.select_set(True)
bpy.ops.object.join()

# Join the box and the lid
bpy.ops.object.select_all(action='DESELECT')
box2.select_set(True)
lid2.select_set(True)
bpy.ops.object.join()

# import pencilbox.obj file created using luma ai 
file_loc = r"C:\Users\xiaom\OneDrive\Desktop\bottle\mesh.obj"
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
pencilbox = bpy.context.selected_objects[0]
pencilbox.location = (6,0,0)
pencilbox.name = "bottle"