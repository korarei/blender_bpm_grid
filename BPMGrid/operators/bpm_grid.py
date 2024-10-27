from math import ceil

import bpy


class TIME_OT_CreateBPMGrid(bpy.types.Operator):
    bl_idname = "time.create_bpm_grid"
    bl_label = "Create"
    bl_description = "Create a BPM grid on the timeline."
    bl_option = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        st = scene.frame_start
        ed = scene.frame_end
        fps = scene.render.fps
        count = [1, 1] # It keeps track of the measure and the number of note.

        bpm = scene.BG_bpm
        note = scene.BG_note
        ck_remove = scene.BG_ck_remove # Indicates whether to delete the marker.


        nps = bpm * note / 240 # Notes per second.
        d = fps / nps
        current_frame = st

        if ck_remove:
            for marker in scene.timeline_markers:
                marker_lst = marker.name.split(' ')
                if len(marker_lst) == 5 and marker_lst[1] == '+' and marker_lst[3] == '/':
                    scene.timeline_markers.remove(marker)


        while ceil(current_frame) < ed:
            scene.timeline_markers.new(f"{count[0]} + {count[1]} / {note}", frame = ceil(current_frame))
    
            if count[1] == note:
                count[0] += 1
                count[1] = 1
            else:
                count[1] += 1
    
            current_frame += d


        return {'FINISHED'}
    