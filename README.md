# Python Cross Platform Compatibility
Workarounds for platform dependent Python code (WIP). 

## Library Wrappers

### winsound
Code body should replace `import winsound` line.

Supports:
- [Beep](https://docs.python.org/3/library/winsound.html#winsound.Beep)
- [PlaySound](https://docs.python.org/2/library/winsound.html#winsound.PlaySound) (partial)
- ~~[MessageBeep](https://docs.python.org/2/library/winsound.html#winsound.MessageBeep)~~

See [winsound-wrapper.py](winsound-wrapper.py)