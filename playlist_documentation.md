# Code Documentation

## Analysis
# Playlist Information Extraction and Management

This document provides an overview of the `playlist.py` file, which is responsible for extracting and managing playlist information, including video details and playlist metadata. It leverages `yt-dlp` for data extraction and provides utilities for displaying and filtering playlist content.

## Classes

### VideoInfo

A dataclass representing detailed information about a single video within a playlist.

**Attributes:**

*   `id` (str): The unique identifier of the video.
*   `title` (str): The title of the video.
*   `url` (str): The URL of the video.
*   `duration` (int): The duration of the video in seconds.
*   `index` (Optional[int]): The sequential index of the video in the playlist (default: `None`).
*   `status` (str): The current status of the video (e.g., 'pending', 'completed', 'failed') (default: 'pending').
*   `error` (Optional[str]): An error message if the video processing failed (default: `None`).

### Playlist

Manages playlist information, including fetching, processing, and displaying video and playlist metadata.

**Constructor:**

`__init__(self, url: str, theme: Theme)`

Initializes a new Playlist instance.

*   **Parameters:**
    *   `url` (str): The URL of the playlist.
    *   `theme` (Theme): An object providing theming capabilities for UI elements.

**Attributes:**

*   `url` (str): The URL of the playlist.
*   `theme` (Theme): The theme object used for UI.
*   `status` (Status): An instance of `Status` for displaying status messages.
*   `progress` (Progress): An instance of `Progress` for displaying progress.
*   `videos` (List[VideoInfo]): A list of `VideoInfo` objects representing the videos in the playlist.
*   `metadata` (Dict): A dictionary containing overall playlist metadata (e.g., title, video count, total duration, creator).
*   `_loaded` (bool): Internal flag indicating if the playlist information has been loaded.

**Methods:**

#### `fetch_info(self) -> bool`

Extracts comprehensive playlist information using `yt-dlp`. This method populates the `videos` list and `metadata` dictionary.

*   **Returns:**
    *   `bool`: `True` if the information was fetched successfully, `False` otherwise.

#### `select_range(self, start: int, end: int) -> List[VideoInfo]`

Filters and returns a sub-list of videos based on a specified start and end index (1-based). If the playlist information hasn't been loaded, it attempts to fetch it first.

*   **Parameters:**
    *   `start` (int): The starting index (1-based) of the video range.
    *   `end` (int): The ending index (1-based) of the video range.
*   **Returns:**
    *   `List[VideoInfo]`: A list of `VideoInfo` objects within the specified range. Returns an empty list if fetching information fails.

#### `get_failed(self) -> List[VideoInfo]`

Returns a list of videos that have a 'failed' status.

*   **Returns:**
    *   `List[VideoInfo]`: A list of `VideoInfo` objects with a 'failed' status.

#### `get_successful(self) -> List[VideoInfo]`

Returns a list of videos that have a 'completed' status.

*   **Returns:**
    *   `List[VideoInfo]`: A list of `VideoInfo` objects with a 'completed' status.

#### `get_pending(self) -> List[VideoInfo]`

Returns a list of videos that have a 'pending' status.

*   **Returns:**
    *   `List[VideoInfo]`: A list of `VideoInfo` objects with a 'pending' status.

#### `display_info(self) -> None`

Prints formatted playlist information to the console. If the playlist information hasn't been loaded, it attempts to fetch it first.

*   **Returns:**
    *   `None`

#### `list_videos(self) -> None`

Prints a formatted list of all videos in the playlist, including their index, title, duration, URL, and any associated error messages. If the playlist information hasn't been loaded, it attempts to fetch it first.

*   **Returns:**
    *   `None`

#### `_extract_playlist_title(self) -> str`

*(Private Method)* Extracts the playlist title using `yt-dlp`.

*   **Returns:**
    *   `str`: The title of the playlist, or "Unknown Playlist" if not found or an error occurs.

#### `_extract_playlist_creator(self) -> str`

*(Private Method)* Extracts the playlist creator using `yt-dlp`.

*   **Returns:**
    *   `str`: The creator of the playlist, or "Unknown Creator" if not found or an error occurs.


## Explanation
This code performs...