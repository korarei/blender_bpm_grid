bl_info = {
    "name": "BPM Grid",
    "description": "This addon creates a BPM grid on the timeline. The user can select the type of notes, the BPM, and whether to delete existing markers.",
    "author": "Korarei",
    "version": (1, 0, 0),
    "blender": (4, 2, 3),
    "support": "COMMUNITY",
    "category": "Animation",
    "location": "View3D > Sidebar",
    "warning": "",
    "tracker_url": "https://github.com/korarei/blender_bpm_grid/issues"
}

if "bpy" in locals():
    import imp
    imp.reload(bpm_grid)
else:
    from .operators import bpm_grid

import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty


class TIME_PT_BPMGridPanel(bpy.types.Panel):
    bl_label = "BPM Grid"
    bl_idname = "TIME_PT_bpm_grid"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BPM Grid"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "BG_bpm", text = "BPM:")
        layout.prop(scene, "BG_note", text = "Note:")
        layout.prop(scene, "BG_ck_remove", text = "Remove existing markers")
        layout.separator()
        layout.operator("time.create_bpm_grid") 


def init_props():
    scene = bpy.types.Scene
    scene.BG_bpm = FloatProperty(
        name = "BPM",
        description = "Set the BPM",
        default = 165,
        min = 0.0,
        max = 2048.0
    )
    scene.BG_note = IntProperty(
        name = "Note",
        description = "Set the note. For example, input 4 for quarter notes and 8 for eighth notes.",
        default = 16,
        min = 0,
        max = 1024
    )
    scene.BG_ck_remove = BoolProperty(
        name = "Remove existing markers",
        description = "Remove existing markers",
        default = True
    )


def clear_props():
    scene = bpy.types.Scene
    del scene.BG_bpm
    del scene.BG_note
    del scene.BG_ck_remove


classes = [
    TIME_PT_BPMGridPanel,
    bpm_grid.TIME_OT_CreateBPMGrid
]


def register():
    init_props()
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    clear_props()
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()