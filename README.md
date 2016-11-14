# Python Cross Platform Compatibility
Workarounds for platform dependent Python code (WIP). 

Inspired by students of [CSSE1001 @ The University of Queensland](https://csse1001.uqcloud.net/) submitting Python assignments with Windows only features that cause trouble for markers using Mac OS X/Linux.

## Library Wrappers

### winsound
Code body should replace `import winsound` line.

Supports:
- [Beep](https://docs.python.org/3/library/winsound.html#winsound.Beep)
- [PlaySound](https://docs.python.org/2/library/winsound.html#winsound.PlaySound) (partial)
- ~~[MessageBeep](https://docs.python.org/2/library/winsound.html#winsound.MessageBeep)~~

See [winsound-wrapper.py](winsound-wrapper.py)