#!/usr/bin/env python3
"""
YouTube MP3 Downloader

A CLI script to download YouTube videos as MP3 audio files.
"""

import os
import sys
import argparse
import subprocess
from typing import List, Optional

def create_output_directory(directory: str) -> None:
    """Create the output directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created output directory: {directory}")

def download_single_video(url: str, output_dir: str) -> bool:
    """
    Download a single YouTube video as MP3.
    
    Args:
        url: YouTube video URL
        output_dir: Directory to save the MP3 file
        
    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        # Ensure output directory exists
        create_output_directory(output_dir)
        
        # Prepare yt-dlp command
        command = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--output", f"{output_dir}/%(title)s.%(ext)s",
            url
        ]
        
        # Execute the command
        print(f"Downloading: {url}")
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully downloaded: {url}")
            return True
        else:
            print(f"Failed to download {url}. Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def download_from_file(file_path: str, output_dir: str) -> None:
    """
    Download YouTube videos from a file containing URLs.
    
    Args:
        file_path: Path to the file containing YouTube URLs (one per line)
        output_dir: Directory to save the MP3 files
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return
    
    # Read URLs from file
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    if not urls:
        print(f"No URLs found in {file_path}")
        return
    
    print(f"Found {len(urls)} URLs in {file_path}")
    
    # Download each URL
    successful = 0
    for i, url in enumerate(urls, 1):
        print(f"Processing {i}/{len(urls)}: {url}")
        if download_single_video(url, output_dir):
            successful += 1
    
    print(f"Download complete: {successful}/{len(urls)} successful")

def check_dependencies() -> bool:
    """Check if yt-dlp is installed."""
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def main():
    """Main function to parse arguments and execute the downloader."""
    parser = argparse.ArgumentParser(description="Download YouTube videos as MP3 files")
    
    # Create a mutually exclusive group for input methods
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-u", "--url", help="Single YouTube URL to download")
    input_group.add_argument("-f", "--file", help="File containing YouTube URLs (one per line)")
    
    # Output directory
    parser.add_argument("-o", "--output-dir", default="mp3", 
                        help="Output directory for MP3 files (default: 'mp3')")
    
    args = parser.parse_args()
    
    # Check if yt-dlp is installed
    if not check_dependencies():
        print("Error: yt-dlp is not installed. Please install it with: pip install yt-dlp")
        return 1
    
    # Process based on input method
    if args.url:
        download_single_video(args.url, args.output_dir)
    elif args.file:
        download_from_file(args.file, args.output_dir)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
