import bpy

# Define the coordinates for each bone manually
bone_coordinates = {
    "hip_center": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],  # Example coordinates for Bone1
    "spine": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "shoulder_center": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "head": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "shoulder_left": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "elbow_left":[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "wrist_left": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "hand_left":[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "shoulder_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "elbow_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "wrist_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "hand_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "hip_left": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "knee_left": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "ankle_left": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "foot_left": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "hip_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "knee_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "ankle_right": [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    "foot_right":[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
     # Example coordinates for Bone2
    # Add more bones and their coordinates as needed
}


# Function to animate the bones
def animate_bones():
    Armature = bpy.data.objects.get("Armature")
    if Armature is None:
        print("Armature not found. Make sure you have a Armature named 'Armature'.")
        return
    
    Armature.animation_data_create()
    Armature.animation_data.action = bpy.data.actions.new(name="DanceAnimation")
    
    for bone_name, coordinates in bone_coordinates.items():
        bone = Armature.pose.bones.get(bone_name)
        if bone is None:
            print(f"Bone '{bone_name}' not found. Skipping.")
            continue
        
        # Set keyframes for each coordinate
        frame_num = 0
        for coord in coordinates:
            bone.location = coord
            bone.keyframe_insert(data_path="location", index=-1, frame=frame_num)
            frame_num += 10  # Increase frame number for next keyframe

# Call the function to animate the bones
animate_bones()