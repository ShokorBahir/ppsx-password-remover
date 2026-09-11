# ppsx-password-remover
A simple Python GUI tool to remove password protection from PowerPoint (.ppsx) files
📋 Copy This Into README.md:
🔐 PPSX Password Remover
A simple, lightweight desktop tool to remove password protection from PowerPoint Show (.ppsx) files.

Built with Python — no external dependencies required!

📋 About
Ever forgotten the password to your own PowerPoint presentation? This tool helps you regain access to your own protected files by removing the password protection layer.

✨ Features
✅ Modern GUI interface
✅ Select multiple files at once
✅ Keeps the original filename
✅ No duplicate file selection
✅ Real-time progress log
✅ Error handling — won't crash on bad files
✅ 100% offline — your files never leave your computer
🚀 Getting Started
🖥️ Screenshot
App Screenshot
Requirements
Python 3.6 or higher
No additional libraries needed
Installation
Clone or download this repository
Run the program:
python ppsx_unlocker.py
How to Use
Click 📂 Select PPSX Files and choose your protected file(s)
Click 🔓 Unlock All
Done! Your files are now password-free
🛠️ How It Works
PowerPoint files (.ppsx) are ZIP archives containing XML files. The password protection is stored inside ppt/presentation.xml. This tool:

Opens the file as a ZIP archive
Finds and removes the password tag
Repackages everything back
⚠️ Disclaimer
This tool is intended only for recovering access to your own files that you've forgotten the password for. Please use responsibly.
