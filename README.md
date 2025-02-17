# blender_bpm_grid
This add-on creates a BPM grid on the timeline. The user can select the type of notes, the BPM, and whether to delete existing markers.

## Download
Download this add-on from Github Release page.

## Installation
1. Open the Preferences window and select the Add-ons tab.
2. Click the "Install..." button. Then, select the zip file of this add-on.
3. Click the checkbox next to the title "BPM Grid".

## Usage
1. Open the 3D viewport UI (displayed by pressing the 'N' key). The panel of this add-on is in it.
2. Open the "BPM Grid" tab.
3. Enter the bar range and click the "Apply" button.
4. Click the "Create" button.

- BPM: Enter the BPM.
- Note: Enter the type of notes. For example, input 4 for quarter notes and 8 for eighth notes.
- Remove existing markers: Check this box to delete added markers.

> [!WARNING]
> If you check "Remove existing markers", all markers with names consisting of five words, with the second word being '+' and the fourth word being '/', will be deleted first, and then new markers will be added according to the specified method. Therefore, please be cautious if there are any other markers.

- Bar Start: First bar of the rendering range.
- Bar End: Final bar of the rendering range.

## License
Distributed under the [GPLv3](LICENSE) License.

## Change Log 
- **v1.1.0**
  - Add a function to delete only the grid when Note = 0.
  - Add a function to calculate the output range based on the bar number.

- **v1.0.1**
  - Improve the delete function.

- **v1.0.0**
  - Release
