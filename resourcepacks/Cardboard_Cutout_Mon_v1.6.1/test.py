import os
import shutil


def filter_unique_folders(folder1_path, folder2_path):
    """
    Compare folders in folder2 with folder1 and keep only those in folder2 that don't exist in folder1.

    Args:
        folder1_path (str): Path to the first folder (reference)
        folder2_path (str): Path to the second folder (to be filtered)
    """
    # Get list of folders in both directories
    folders_in_1 = [
        d
        for d in os.listdir(folder1_path)
        if os.path.isdir(os.path.join(folder1_path, d))
    ]
    folders_in_2 = [
        d
        for d in os.listdir(folder2_path)
        if os.path.isdir(os.path.join(folder2_path, d))
    ]

    print(f"Found {len(folders_in_1)} folders in Folder 1")
    print(f"Found {len(folders_in_2)} folders in Folder 2 initially")

    # Find folders in folder2 that are also in folder1
    duplicates = set(folders_in_2) & set(folders_in_1)

    if not duplicates:
        print("No duplicate folders found. Nothing to remove.")
        return

    print(f"Found {len(duplicates)} duplicate folders to remove")

    # Remove duplicate folders from folder2
    for folder in duplicates:
        folder_path = os.path.join(folder2_path, folder)
        try:
            shutil.rmtree(folder_path)
            print(f"Removed: {folder_path}")
        except Exception as e:
            print(f"Error removing {folder_path}: {e}")

    print("Operation completed.")
    remaining_folders = [
        d
        for d in os.listdir(folder2_path)
        if os.path.isdir(os.path.join(folder2_path, d))
    ]
    print(f"{len(remaining_folders)} folders remain in Folder 2")


# Example usage:
folder1 = "F:\Minecraft\ModrinthMinecraft\profiles\CKDM 4.15b\\resourcepacks\ATM 2.2 for MEGASHOWDOWN v9.0.0\\assets\cobblemon\\bedrock\pokemon\models"
folder2 = "F:\Minecraft\ModrinthMinecraft\profiles\CKDM 4.15b\\resourcepacks\Cardboard_Cutout_Mon_v1.6.1\\assets\cobblemon\\bedrock\species"
filter_unique_folders(folder1, folder2)
