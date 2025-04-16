import bpy
import csv
from mathutils import Vector

# === Path to your CSV file ===
csv_file_path = r'D:\blender files\bharatanatyam_315_500_coordinates.csv'

# === Read CSV ===
def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

keyframe_data = read_csv(csv_file_path)

# === Setup armature in Pose Mode ===
bpy.ops.object.mode_set(mode='OBJECT')
armature = bpy.data.objects['Armature']
bpy.context.view_layer.objects.active = armature
armature.select_set(True)
bpy.ops.object.mode_set(mode='POSE')

# === Bones mentioned in CSV ===
bones_in_csv = set()
for key in keyframe_data[0].keys():
    if '_' in key and key != 'frame':
        bones_in_csv.add(key.rsplit('_', 1)[0])

# === Scale for visibility ===
scale = 10.0

# === Animate Each Frame ===
for frame_data in keyframe_data:
    frame = int(frame_data['frame'])

    # Get hip_center as dynamic origin
    try:
        hip_x = float(frame_data.get('hip_center_x', 0))
        hip_y = float(frame_data.get('hip_center_y', 0))
        hip_z = float(frame_data.get('hip_center_z', 0))
        hip_center = Vector((hip_x, hip_y, hip_z))
    except:
        print(f"Skipping frame {frame} due to hip_center error.")
        continue

    for bone_name in bones_in_csv:
        bone = armature.pose.bones.get(bone_name)
        if bone is None:
            continue

        try:
            x = float(frame_data.get(f'{bone_name}_x', 0))
            y = float(frame_data.get(f'{bone_name}_y', 0))
            z = float(frame_data.get(f'{bone_name}_z', 0))

            # === Convert to relative position to hip_center ===
            world_coord = (Vector((x, y, z)) - hip_center) * scale

            # === Convert to armature (object) space ===
            coord_in_armature = armature.matrix_world.inverted() @ (armature.matrix_world @ world_coord)

            # === Convert to local bone space ===
            if bone.parent:
                local_coord = bone.parent.matrix.inverted() @ coord_in_armature
            else:
                local_coord = coord_in_armature

            # === Set position and keyframe ===
            bone.location = local_coord
            bone.keyframe_insert(data_path="location", frame=frame)

        except Exception as e:
            print(f"Error at frame {frame}, bone {bone_name}: {e}")

# === Done ===
bpy.ops.object.mode_set(mode='OBJECT')
print("All bones animated with hip_center as origin.")
